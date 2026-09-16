#!/usr/bin/env python3
"""Fail if any built page is unreachable by following links from the home page.

Lychee checks that the links we *have* resolve. Nothing checked that a page is
linked at all — and the Reference sidebar is deliberately top-level only (see
CLAUDE.md), so a reference page missing from its category `index.md` is
reachable by search alone. That is how 331 pages went stranded, including every
geospatial step.

Run after `npm run build`, against `dist/`.
"""
import os
import posixpath
import re
import sys
from collections import defaultdict
from glob import glob

ANCHOR = re.compile(r'<a[^>]+href="([^"]+)"')
SKIP_PREFIX = ('http', 'mailto:', '#', '//', 'javascript:', 'data:')
#: Pages with no inbound link by design.
ALLOWED = {'/', '/404/'}


def page_url(path, root):
    rel = os.path.dirname(os.path.relpath(path, root))
    return '/' if rel == '' else f'/{rel}/'


def main(root='dist'):
    files = glob(os.path.join(root, '**', 'index.html'), recursive=True)
    if not files:
        sys.exit(f'no built pages under {root}/ — run `npm run build` first')

    pages = {page_url(p, root): p for p in files}
    links = defaultdict(set)
    for path in files:
        src = page_url(path, root)
        with open(path, encoding='utf8', errors='ignore') as fh:
            html = fh.read()
        for href in set(ANCHOR.findall(html)):
            if href.startswith(SKIP_PREFIX):
                continue
            target = href.split('#')[0].split('?')[0]
            if not target:
                continue
            if not target.startswith('/'):
                target = posixpath.normpath(posixpath.join(src, target))
            if not target.endswith('/'):
                target += '/'
            if target in pages:
                links[src].add(target)

    seen, stack = {'/'}, ['/']
    while stack:
        for target in links[stack.pop()]:
            if target not in seen:
                seen.add(target)
                stack.append(target)

    orphans = sorted(set(pages) - seen - ALLOWED)
    if not orphans:
        print(f'orphan check: {len(pages)} pages, all reachable')
        return 0

    print(f'{len(orphans)} unreachable page(s) — add a link from the parent '
          f'category index (see CLAUDE.md, "Sidebar architecture"):\n')
    for url in orphans:
        print(f'  {url}')
    return 1


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
