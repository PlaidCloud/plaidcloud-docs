# /// script
# dependencies = ["pyyaml"]
# ///
"""Fail when a bold UI label this branch removed from an English page is still on another English page.

    uv run scripts/check-removed-labels.py [REF]      (default origin/main)

A renamed or removed control gets fixed on the page that documents the change, while other pages keep sending
readers to it. For every `**label**` on an English line removed since the merge base with REF that no added line
brings back, this greps the English pages and snippets (locale dirs excluded) for `**label**` and fails on a hit.

A label that is still right where it remains (it moved, or another screen still has it): add a line
`labels-kept: <label>` to a commit message on the branch. A commit message, not the PR body, because CI reruns
on a push but not on a PR-body edit.
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from translate import LOCALES, ROOT  # noqa: E402

BOLD_RE = re.compile(r"\*\*([^*\n]+?)\*\*")
ENGLISH = (["src/content/docs", "src/snippets"]
           + [f":(exclude){d}/{lc}" for d in ("src/content/docs", "src/snippets") for lc in LOCALES])


def git(*args):
    return subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True).stdout


def main():
    ref = sys.argv[1] if len(sys.argv) > 1 else "origin/main"
    base = git("merge-base", "HEAD", ref).strip()
    removed, added = set(), set()
    for line in git("diff", "-U0", base, "--", *ENGLISH).splitlines():
        if line.startswith(("--- ", "+++ ")):
            continue
        if line.startswith("-"):
            removed.update(BOLD_RE.findall(line[1:]))
        elif line.startswith("+"):
            added.update(BOLD_RE.findall(line[1:]))
    kept = set(re.findall(r"^labels-kept:[ \t]*(.+?)[ \t]*$", git("log", "--format=%B", f"{base}..HEAD"), re.M))
    touched = git("diff", "--name-only", base, "--", *ENGLISH).split()
    live = [f for f in touched if (ROOT / f).is_file()]
    grep = lambda label, paths: subprocess.run(["git", "-C", str(ROOT), "grep", "-n", "-F", f"**{label}**", "--", *paths],
                                               capture_output=True, text=True).stdout.splitlines()
    bad = 0
    # A span with edge whitespace is a bold pairing cut by the diff, not a label. A label still on a page this branch
    # edits was seen and kept by its author, so it is skipped: over the last 40 merged PRs that took the flagged
    # labels from 21 to 10 (6 PRs), leaving mostly real stale references such as the renamed "AI Assistant".
    for label in sorted(l for l in removed - added - kept if l == l.strip()):
        if live and grep(label, live):
            continue
        hits = grep(label, ENGLISH)
        if hits:
            bad += 1
            print(f"**{label}** was removed but is still on {len(hits)} English line(s):")
            print("".join(f"  {h[:160]}\n" for h in hits[:10]), end="")
    print(f"{len(removed - added)} bold label(s) removed, {len(kept)} kept by labels-kept, {bad} still in use")
    if bad:
        print("Update those pages, or add `labels-kept: <label>` to a commit message if the label is still right there.")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
