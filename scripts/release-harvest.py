"""
Harvest release data from plaid-tenant-infrastructure for /releases/ pages.

Walks tenant-v* tags in the last 24 months, buckets by calendar month,
collects all commit subjects + bodies + PR titles. Outputs one JSON
bucket per month for downstream summarization.

Usage:
    python3 scripts/release-harvest.py
    # Produces /tmp/release-bundles/YYYY-MM.json files
"""
from __future__ import annotations

import json
import os
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

INFRA_REPO = Path("/Users/inviscid/Projects/plaid-tenant-infrastructure")
OUTPUT_DIR = Path("/tmp/release-bundles")
WINDOW_MONTHS = 24


def run(cmd: list[str], cwd: Path = INFRA_REPO) -> str:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=True).stdout


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Get all tenant-v* tags with their creator dates
    raw = run(["git", "for-each-ref", "refs/tags/tenant-v*",
               "--format=%(refname:short)\t%(creatordate:short)"])
    tags = []
    cutoff = datetime.now() - timedelta(days=WINDOW_MONTHS * 31)
    for line in raw.strip().splitlines():
        name, date_s = line.split("\t")
        d = datetime.strptime(date_s, "%Y-%m-%d")
        if d >= cutoff:
            tags.append((name, d))
    tags.sort(key=lambda x: x[1])

    # Bucket by YYYY-MM
    by_month: dict[str, list[tuple[str, datetime]]] = defaultdict(list)
    for name, d in tags:
        by_month[d.strftime("%Y-%m")].append((name, d))

    # For each month, walk commits between (last tag of prev month, last tag of this month)
    months = sorted(by_month.keys())
    all_tags_ordered = sorted(tags, key=lambda x: x[1])
    prev_end = None

    for month in months:
        month_tags = by_month[month]
        last_tag = month_tags[-1][0]

        # The start point is whichever tag preceded the first tag this month
        first_tag = month_tags[0][0]
        prev_idx = next((i for i, t in enumerate(all_tags_ordered) if t[0] == first_tag), 0)
        if prev_idx > 0:
            start = all_tags_ordered[prev_idx - 1][0]
            commit_range = f"{start}..{last_tag}"
        else:
            commit_range = last_tag

        # Harvest commits in the range
        try:
            commits_raw = run([
                "git", "log",
                "--pretty=format:===%n%H%n%s%n%b",
                commit_range,
            ])
        except subprocess.CalledProcessError:
            commits_raw = ""

        commits = []
        for chunk in commits_raw.split("===\n"):
            if not chunk.strip():
                continue
            lines = chunk.strip().split("\n", 2)
            if len(lines) < 2:
                continue
            commits.append({
                "sha": lines[0][:12],
                "subject": lines[1],
                "body": lines[2] if len(lines) > 2 else "",
            })

        bundle = {
            "month": month,
            "tenant_tags": [
                {"name": n, "version": n.removeprefix("tenant-"), "date": d.strftime("%Y-%m-%d")}
                for n, d in month_tags
            ],
            "commit_count": len(commits),
            "commits": commits,
        }

        out = OUTPUT_DIR / f"{month}.json"
        out.write_text(json.dumps(bundle, indent=2))
        print(f"{month}: {len(month_tags)} tags, {len(commits)} commits  -> {out}")


if __name__ == "__main__":
    main()
