#!/usr/bin/env python3
"""
Pull a monthly insights report for docs.plaidcloud.com.

Combines Cloudflare Web Analytics (RUM) and Google Search Console into a
single Markdown report intended for review by a human or a Claude agent.
Output goes to stdout by default; pass --output PATH to write to a file
under a gitignored directory.

REQUIRED environment variables
------------------------------
  CF_ACCOUNT_TAG            CF account ID (visible in CF dashboard URL)
  CF_SITE_TAG               CF Web Analytics site tag (Settings → Sites tab)
  CF_API_TOKEN              CF API token with Analytics:Read on the zone
  GSC_PROPERTY              GSC property string, e.g.
                            "sc-domain:plaidcloud.com" for domain property
                            or "https://docs.plaidcloud.com/" for URL property
  GSC_SERVICE_ACCOUNT_JSON  Path to a Google Cloud service-account JSON key
                            with Search Console API enabled. The service
                            account email must be added as a Full user on
                            the GSC property.

OPTIONAL flags
--------------
  --days N           Look-back window. Default 30.
  --output PATH      Write report here instead of stdout.
  --no-gsc           Skip Search Console (useful if creds aren't set up yet).
  --no-cf            Skip Cloudflare.
  --top N            Top-N truncation for each table. Default 20.

USAGE
-----
  # Standard monthly run
  python3 scripts/insights.py > /tmp/insights-2026-05.md

  # Or via an agent
  CF_ACCOUNT_TAG=xxx CF_SITE_TAG=yyy CF_API_TOKEN=zzz \\
  GSC_PROPERTY=sc-domain:plaidcloud.com \\
  GSC_SERVICE_ACCOUNT_JSON=/secrets/gsc.json \\
  python3 scripts/insights.py --days 30

DEPENDENCIES
------------
  python3 -m pip install google-auth google-api-python-client

Only google-auth + google-api-python-client are required.
Cloudflare uses stdlib only.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any


CF_GRAPHQL = "https://api.cloudflare.com/client/v4/graphql"

AI_ASSISTANT_REFERRERS = {
    # Hostname → display label
    "chat.openai.com": "ChatGPT",
    "chatgpt.com": "ChatGPT",
    "claude.ai": "Claude",
    "perplexity.ai": "Perplexity",
    "www.perplexity.ai": "Perplexity",
    "you.com": "You.com",
    "phind.com": "Phind",
    "kagi.com": "Kagi",
    "duckduckgo.com": "DuckDuckGo",
    "bing.com": "Bing",
    "www.bing.com": "Bing",
}

AI_BOT_UAS = {
    "GPTBot",
    "OAI-SearchBot",
    "ChatGPT-User",
    "ClaudeBot",
    "Claude-Web",
    "anthropic-ai",
    "PerplexityBot",
    "Perplexity-User",
    "Google-Extended",
    "Applebot-Extended",
    "Bytespider",
    "CCBot",
    "cohere-ai",
}


# --------------------------------------------------------------------------- #
# Cloudflare Web Analytics
# --------------------------------------------------------------------------- #

def cf_query(token: str, query: str, variables: dict) -> dict:
    """POST to the CF GraphQL endpoint and return `data` or raise."""
    req = urllib.request.Request(
        CF_GRAPHQL,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        data=json.dumps({"query": query, "variables": variables}).encode(),
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        raise RuntimeError(f"CF HTTP {e.code}: {body[:500]}") from None
    if payload.get("errors"):
        raise RuntimeError(f"CF GraphQL errors: {payload['errors']}")
    return payload["data"]


def cf_pageviews_by_path(token: str, account_tag: str, site_tag: str,
                        date_gte: str, date_lt: str, limit: int = 100) -> list[dict]:
    """Top pages by view count over the window."""
    q = """
    query($accountTag: String!, $siteTag: String!, $dateGte: Date!, $dateLt: Date!, $limit: Int!) {
      viewer {
        accounts(filter: { accountTag: $accountTag }) {
          rumPageloadEventsAdaptiveGroups(
            filter: { siteTag: $siteTag, date_geq: $dateGte, date_lt: $dateLt }
            orderBy: [count_DESC]
            limit: $limit
          ) {
            count
            sum { visits }
            dimensions { metric { requestPath } }
          }
        }
      }
    }
    """
    data = cf_query(token, q, {
        "accountTag": account_tag, "siteTag": site_tag,
        "dateGte": date_gte, "dateLt": date_lt, "limit": limit,
    })
    rows = data["viewer"]["accounts"][0]["rumPageloadEventsAdaptiveGroups"]
    return [{
        "path": r["dimensions"]["metric"]["requestPath"],
        "views": r["count"],
        "visits": r["sum"]["visits"],
    } for r in rows]


def cf_referrers(token: str, account_tag: str, site_tag: str,
                date_gte: str, date_lt: str, limit: int = 100) -> list[dict]:
    """Top referrer hostnames."""
    q = """
    query($accountTag: String!, $siteTag: String!, $dateGte: Date!, $dateLt: Date!, $limit: Int!) {
      viewer {
        accounts(filter: { accountTag: $accountTag }) {
          rumPageloadEventsAdaptiveGroups(
            filter: { siteTag: $siteTag, date_geq: $dateGte, date_lt: $dateLt }
            orderBy: [count_DESC]
            limit: $limit
          ) {
            count
            dimensions { metric { refererHost } }
          }
        }
      }
    }
    """
    data = cf_query(token, q, {
        "accountTag": account_tag, "siteTag": site_tag,
        "dateGte": date_gte, "dateLt": date_lt, "limit": limit,
    })
    rows = data["viewer"]["accounts"][0]["rumPageloadEventsAdaptiveGroups"]
    return [{
        "host": r["dimensions"]["metric"]["refererHost"] or "(direct)",
        "views": r["count"],
    } for r in rows]


def cf_countries(token: str, account_tag: str, site_tag: str,
                date_gte: str, date_lt: str, limit: int = 30) -> list[dict]:
    q = """
    query($accountTag: String!, $siteTag: String!, $dateGte: Date!, $dateLt: Date!, $limit: Int!) {
      viewer {
        accounts(filter: { accountTag: $accountTag }) {
          rumPageloadEventsAdaptiveGroups(
            filter: { siteTag: $siteTag, date_geq: $dateGte, date_lt: $dateLt }
            orderBy: [count_DESC]
            limit: $limit
          ) {
            count
            dimensions { metric { countryName } }
          }
        }
      }
    }
    """
    data = cf_query(token, q, {
        "accountTag": account_tag, "siteTag": site_tag,
        "dateGte": date_gte, "dateLt": date_lt, "limit": limit,
    })
    rows = data["viewer"]["accounts"][0]["rumPageloadEventsAdaptiveGroups"]
    return [{
        "country": r["dimensions"]["metric"]["countryName"] or "(unknown)",
        "views": r["count"],
    } for r in rows]


def cf_devices(token: str, account_tag: str, site_tag: str,
              date_gte: str, date_lt: str) -> list[dict]:
    q = """
    query($accountTag: String!, $siteTag: String!, $dateGte: Date!, $dateLt: Date!) {
      viewer {
        accounts(filter: { accountTag: $accountTag }) {
          rumPageloadEventsAdaptiveGroups(
            filter: { siteTag: $siteTag, date_geq: $dateGte, date_lt: $dateLt }
            orderBy: [count_DESC]
            limit: 10
          ) {
            count
            dimensions { metric { deviceType } }
          }
        }
      }
    }
    """
    data = cf_query(token, q, {
        "accountTag": account_tag, "siteTag": site_tag,
        "dateGte": date_gte, "dateLt": date_lt,
    })
    rows = data["viewer"]["accounts"][0]["rumPageloadEventsAdaptiveGroups"]
    return [{
        "device": r["dimensions"]["metric"]["deviceType"] or "(unknown)",
        "views": r["count"],
    } for r in rows]


# --------------------------------------------------------------------------- #
# Search Console
# --------------------------------------------------------------------------- #

def gsc_client(json_key_path: str):
    """Build an authenticated Search Console API client."""
    try:
        from google.oauth2 import service_account  # type: ignore
        from googleapiclient.discovery import build  # type: ignore
    except ImportError:
        raise RuntimeError(
            "google-auth and google-api-python-client are required for GSC. "
            "Run: pip install google-auth google-api-python-client"
        )
    creds = service_account.Credentials.from_service_account_file(
        json_key_path,
        scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
    )
    return build("searchconsole", "v1", credentials=creds, cache_discovery=False)


def gsc_query(client, property_url: str, dimensions: list[str],
              start: str, end: str, row_limit: int = 1000) -> list[dict]:
    body = {
        "startDate": start,
        "endDate": end,
        "dimensions": dimensions,
        "rowLimit": row_limit,
        "dataState": "all",
    }
    resp = client.searchanalytics().query(siteUrl=property_url, body=body).execute()
    return resp.get("rows", [])


# --------------------------------------------------------------------------- #
# Report formatting
# --------------------------------------------------------------------------- #

def md_table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return "_No data._\n"
    cols = [headers] + [[str(c) for c in r] for r in rows]
    widths = [max(len(c) for c in col) for col in zip(*cols)]
    def fmt(row):
        return "| " + " | ".join(c.ljust(widths[i]) for i, c in enumerate(row)) + " |"
    out = [fmt(headers), fmt(["-" * w for w in widths])]
    for r in cols[1:]:
        out.append(fmt(r))
    return "\n".join(out) + "\n"


def section(title: str, body: str) -> str:
    return f"## {title}\n\n{body}\n"


def render_report(args, cf_data: dict | None, gsc_data: dict | None) -> str:
    lines = []
    lines.append(f"# Docs insights — {args.start} to {args.end} ({args.days} days)\n")
    lines.append(f"_Generated {dt.datetime.utcnow().isoformat()}Z_\n")

    # --- Cloudflare ---
    if cf_data:
        total = sum(p["views"] for p in cf_data["pages"])
        total_visits = sum(p["visits"] for p in cf_data["pages"])
        lines.append(section("Traffic — Cloudflare Web Analytics",
            f"- **Total page views:** {total:,}\n"
            f"- **Total visits:** {total_visits:,}\n"
        ))

        lines.append(section(f"Top {args.top} pages by views",
            md_table(["Page", "Views", "Visits"],
                [[p["path"], f"{p['views']:,}", f"{p['visits']:,}"]
                 for p in cf_data["pages"][:args.top]])))

        # AI assistant referrers vs everyone else
        ai_views = 0
        ai_breakdown = []
        other_refs = []
        for r in cf_data["referrers"]:
            label = AI_ASSISTANT_REFERRERS.get(r["host"])
            if label:
                ai_views += r["views"]
                ai_breakdown.append([label, r["host"], f"{r['views']:,}"])
            else:
                other_refs.append(r)
        lines.append(section("AI assistant / search referrers",
            f"_Traffic from LLM-powered tools and general-purpose search._\n\n" +
            md_table(["Source", "Host", "Views"], ai_breakdown[:args.top])))

        lines.append(section(f"Top {args.top} non-AI referrers",
            md_table(["Host", "Views"],
                [[r["host"], f"{r['views']:,}"] for r in other_refs[:args.top]])))

        lines.append(section("Geography",
            md_table(["Country", "Views"],
                [[c["country"], f"{c['views']:,}"] for c in cf_data["countries"][:args.top]])))

        lines.append(section("Device split",
            md_table(["Device", "Views"],
                [[d["device"], f"{d['views']:,}"] for d in cf_data["devices"]])))

    # --- Search Console ---
    if gsc_data:
        lines.append(section("Search Console — overall",
            f"- **Total impressions:** {gsc_data['totals']['impressions']:,}\n"
            f"- **Total clicks:** {gsc_data['totals']['clicks']:,}\n"
            f"- **Average CTR:** {gsc_data['totals']['ctr']:.1%}\n"
            f"- **Average position:** {gsc_data['totals']['position']:.1f}\n"
        ))

        lines.append(section(f"Top {args.top} queries (by impressions)",
            md_table(["Query", "Impressions", "Clicks", "CTR", "Position"],
                [[q["query"], f"{q['impressions']:,}", f"{q['clicks']:,}",
                  f"{q['ctr']:.1%}", f"{q['position']:.1f}"]
                 for q in gsc_data["top_queries"][:args.top]])))

        # High-impression, low-CTR (optimization opportunities)
        opt = [q for q in gsc_data["top_queries"]
               if q["impressions"] >= 50 and q["ctr"] < 0.02][:args.top]
        lines.append(section("Title/description optimization candidates",
            "_Queries with ≥50 impressions and CTR < 2%. The page ranks but the snippet isn't earning clicks._\n\n" +
            md_table(["Query", "Impressions", "CTR", "Position"],
                [[q["query"], f"{q['impressions']:,}", f"{q['ctr']:.1%}", f"{q['position']:.1f}"]
                 for q in opt])))

        # Content gap signal: high-impression queries at low rank
        gaps = [q for q in gsc_data["top_queries"]
                if q["impressions"] >= 30 and q["position"] >= 10][:args.top]
        lines.append(section("Content gap candidates",
            "_Queries with ≥30 impressions but average position ≥ 10. We rank somewhere but not well — content may not match query intent._\n\n" +
            md_table(["Query", "Impressions", "Position"],
                [[q["query"], f"{q['impressions']:,}", f"{q['position']:.1f}"]
                 for q in gaps])))

        lines.append(section(f"Top {args.top} pages (by Search Console clicks)",
            md_table(["Page", "Impressions", "Clicks", "CTR", "Position"],
                [[p["page"], f"{p['impressions']:,}", f"{p['clicks']:,}",
                  f"{p['ctr']:.1%}", f"{p['position']:.1f}"]
                 for p in gsc_data["top_pages"][:args.top]])))

    # --- Cross-source synthesis (zero data here, but space for the analyzer) ---
    lines.append(section("Suggested next analyses for the agent",
        "1. Pages with high views (CF) but no Search Console clicks → traffic comes from referrers, not search.\n"
        "2. Pages with high Search Console impressions but missing from CF top-pages → user finds the link, doesn't click through, or bounces fast.\n"
        "3. Queries in the content-gap table → does a more specific page exist? If not, candidate for new content.\n"
        "4. AI referrer share of total → are LLMs sending users to us? Compare month-over-month.\n"
        "5. Pages with zero views in the window → audit for staleness, broken inbound links, or candidates for consolidation.\n"
    ))

    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--days", type=int, default=30)
    p.add_argument("--top", type=int, default=20)
    p.add_argument("--output", help="Write report to this path instead of stdout.")
    p.add_argument("--no-cf", action="store_true", help="Skip Cloudflare.")
    p.add_argument("--no-gsc", action="store_true", help="Skip Search Console.")
    args = p.parse_args(argv)

    today = dt.date.today()
    args.end = today.isoformat()
    args.start = (today - dt.timedelta(days=args.days)).isoformat()

    cf_data = None
    gsc_data = None

    # Cloudflare
    if not args.no_cf:
        token = os.environ.get("CF_API_TOKEN")
        acct = os.environ.get("CF_ACCOUNT_TAG")
        site = os.environ.get("CF_SITE_TAG")
        if not all([token, acct, site]):
            print("CF: missing CF_API_TOKEN / CF_ACCOUNT_TAG / CF_SITE_TAG — skipping CF section.",
                  file=sys.stderr)
        else:
            try:
                cf_data = {
                    "pages":      cf_pageviews_by_path(token, acct, site, args.start, args.end),
                    "referrers":  cf_referrers(token, acct, site, args.start, args.end),
                    "countries":  cf_countries(token, acct, site, args.start, args.end),
                    "devices":    cf_devices(token, acct, site, args.start, args.end),
                }
            except Exception as e:
                print(f"CF pull failed: {e}", file=sys.stderr)

    # Search Console
    if not args.no_gsc:
        property_url = os.environ.get("GSC_PROPERTY")
        key_path     = os.environ.get("GSC_SERVICE_ACCOUNT_JSON")
        if not all([property_url, key_path]):
            print("GSC: missing GSC_PROPERTY / GSC_SERVICE_ACCOUNT_JSON — skipping GSC section.",
                  file=sys.stderr)
        else:
            try:
                client = gsc_client(key_path)
                top_queries_rows = gsc_query(client, property_url, ["query"],
                                            args.start, args.end, row_limit=1000)
                top_pages_rows = gsc_query(client, property_url, ["page"],
                                          args.start, args.end, row_limit=1000)
                # The unfiltered totals call returns a single aggregated row
                totals_rows = gsc_query(client, property_url, [], args.start, args.end, row_limit=1)
                totals = totals_rows[0] if totals_rows else {"impressions": 0, "clicks": 0, "ctr": 0, "position": 0}
                gsc_data = {
                    "totals": totals,
                    "top_queries": [{"query": r["keys"][0], **{k: r[k] for k in ("impressions", "clicks", "ctr", "position")}}
                                    for r in top_queries_rows],
                    "top_pages": [{"page": r["keys"][0], **{k: r[k] for k in ("impressions", "clicks", "ctr", "position")}}
                                  for r in top_pages_rows],
                }
            except Exception as e:
                print(f"GSC pull failed: {e}", file=sys.stderr)

    if not cf_data and not gsc_data:
        print("No data sources succeeded. Check credentials and try again.", file=sys.stderr)
        return 1

    report = render_report(args, cf_data, gsc_data)

    if args.output:
        os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report written to {args.output}", file=sys.stderr)
    else:
        sys.stdout.write(report)

    return 0


if __name__ == "__main__":
    sys.exit(main())
