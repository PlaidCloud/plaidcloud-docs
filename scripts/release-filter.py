"""Filter monthly bundle data to surface customer-facing signal."""
import json
import re
import sys
from pathlib import Path

BUNDLES = Path("/tmp/release-bundles")

NOISE_PATTERNS = [
    r"Update [A-Z][a-zA-Z ]+ Image",
    r"\bRc \d",
    r"^\* Update ",
    r"^\* Bump ",
    r"^\* Pin ",
    r"\bESO\b", r"\bExternalSecret", r"\bVault\b", r"\bvault\b",
    r"crossplane", r"crowdsec", r"coraza", r"argocd?\b", r"argo[-:]",
    r"helm[-: ]", r"kubeconform", r"yamllint", r"kustomize",
    r"^ci[: /]", r"chore\(", r"chore:", r"build:", r"deps:", r"test:",
    r"databend-meta", r"postgres-secrets", r"pgbackrest", r"keycloak",
    r"perimeter", r"wireguard\b", r"\bvpn\b",
    r"falcosidekick", r"\bgke\b", r"\bgcs\b",
    r"tenant-config", r"plaid-config", r"namespace ",
    r"\bRBAC\b", r"\brbac\b",
    r"PreSync", r"presync", r"sync hook",
    r"address (review|round-\d|second-pass|third-pass)",
    r"review feedback",
    r"fix typo", r"fix key", r"fix link",
    r"^revert ", r"rollback",
    r"prevent drift", r"drift[ -]detection", r"drift[ -]check", r"leader-enforcer",
    r"role-", r"deployment-template", r"external-secret-",
    r"docs: (lock|clarify|fix stale|rollout)", r"docs/rollout",
    r"harden against",
    r"raft-dir", r"split-brain",
    r"^\* tenants:", r"^\* controlplane:",
    r"stomp", r"traefik\b", r"envoy-gateway", r"ingress controller",
    r"chart cleanup", r"obsolete", r"deprecate cron",
]

SIGNAL_PATTERNS = [
    r"self-service", r"signup", r"trial",
    r"Stripe",
    r"ai assistant", r"ai agent", r"\bMCP\b", r"plaid-mcp",
    r"personal temp drive", r"temp drive",
    r"qooxdoo ingress.*redirect", r"deprecate cp-frontend",
    r"app\.<domain", r"redirect legacy",
    r"lakehouse v2", r"\bstarrocks\b",
    r"\bAI\b", r"chat",
    r"vulnerability", r"\bCVE\b", r"security advisory",
    r"add (new|stripe|self|api|cli|connector|workflow|allocation|dimension|dashboard|panel|ai)",
    r"new (feature|connector|workflow|allocation|api)",
    r"deprecat",
    r"public access", r"public ip",
    r"AI Assistant", r"PlaidLink", r"PlaidXL",
    r"workflow_run_history",
    r"replace [A-Za-z]+ with [A-Za-z]+",
]

NOISE_RE = re.compile("|".join(f"(?:{p})" for p in NOISE_PATTERNS), re.IGNORECASE)
SIGNAL_RE = re.compile("|".join(f"(?:{p})" for p in SIGNAL_PATTERNS), re.IGNORECASE)


def extract_pr_titles(commits):
    titles = set()
    for c in commits:
        m = re.match(r"^(.+?)\s*\(#\d+\)\s*$", c["subject"])
        if m:
            titles.add(m.group(1).strip())
        for line in c["body"].splitlines():
            line = line.strip()
            if line.startswith("* "):
                t = re.sub(r"\s*\(#\d+\)\s*$", "", line[2:]).strip()
                if t and len(t) > 5:
                    titles.add(t)
    return titles


def classify(titles):
    signal, noise, neutral = [], [], []
    for t in titles:
        if SIGNAL_RE.search(t):
            signal.append(t)
        elif NOISE_RE.search(t):
            noise.append(t)
        else:
            neutral.append(t)
    return signal, neutral, noise


def main():
    month = sys.argv[1] if len(sys.argv) > 1 else None
    files = sorted(BUNDLES.glob("*.json")) if not month else [BUNDLES / f"{month}.json"]
    for f in files:
        b = json.loads(f.read_text())
        titles = extract_pr_titles(b["commits"])
        signal, neutral, noise = classify(titles)
        print(f"\n=== {b['month']} | {len(b['tenant_tags'])} tags | {len(titles)} titles | sig:{len(signal)} neut:{len(neutral)} noise:{len(noise)} ===")
        for t in b["tenant_tags"]:
            print(f"  tag: {t['version']} ({t['date']})")
        if signal:
            print(f"  SIGNAL:")
            for s in sorted(signal):
                print(f"    + {s[:200]}")
        if neutral:
            print(f"  NEUTRAL:")
            for n in sorted(neutral):
                print(f"    ~ {n[:200]}")


if __name__ == "__main__":
    main()
