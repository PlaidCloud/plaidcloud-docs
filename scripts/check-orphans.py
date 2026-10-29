#!/usr/bin/env python3
"""Fail if any built page is unreachable by following links from the home page.

Lychee checks that the links we *have* resolve. Nothing checked that a page is
linked at all — and the Reference sidebar is deliberately top-level only (see
CLAUDE.md), so a reference page missing from its category `index.md` is
reachable by search alone. That is how 331 pages went stranded, including every
geospatial step.

Also fail if a page in a hand-listed sidebar section is missing from the
sidebar: guides are slug entries in `astro.config.mjs`, so a new page shows up
in the menu only when someone adds it there.

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
#: Sections whose every page must appear in the sidebar.
SIDEBAR_SECTIONS = ('/get-started/', '/guides/', '/integrations/', '/administration/')


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

    failed = 0
    orphans = sorted(set(pages) - seen - ALLOWED)
    if orphans:
        failed = 1
        print(f'{len(orphans)} unreachable page(s) — add a link from the parent '
              f'category index (see CLAUDE.md, "Sidebar architecture"):\n')
        for url in orphans:
            print(f'  {url}')
    else:
        print(f'orphan check: {len(pages)} pages, all reachable')

    # The sidebar is identical on every page that has one (splash pages, like
    # the home page, don't); read it from the guides overview.
    with open(pages['/guides/'], encoding='utf8') as fh:
        html = fh.read()
    start = html.index('id="starlight__sidebar"')
    in_sidebar = {h if h.endswith('/') else h + '/'
                  for h in ANCHOR.findall(html[start:html.index('</nav>', start)])}
    missing = sorted(u for u in pages if u.startswith(SIDEBAR_SECTIONS) and u not in in_sidebar)
    if missing:
        failed = 1
        print(f'\n{len(missing)} page(s) missing from the sidebar — add the slug to '
              f'`sidebar` in astro.config.mjs:\n')
        for url in missing:
            print(f'  {url}')
    else:
        print('sidebar check: every guide, integration and admin page is in the sidebar')
    return failed


if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))
