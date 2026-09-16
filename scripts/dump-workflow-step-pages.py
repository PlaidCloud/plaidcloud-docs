#!/usr/bin/env python3
"""Emit the workflow-step page manifest that plaid's docs-link test checks against.

`flow_details.step_map` carries each step's docs path, and
`plaid/tests/unit/app/analyze/test_flow_details_docs.py` verifies every one of
them resolves. That test needs to know which pages exist, and this repo is the
only thing that knows. Run from the repo root after adding or renaming a
workflow-step page:

    python3 scripts/dump-workflow-step-pages.py > \\
        ../plaid/plaid/app/analyze/utility/docs_step_pages.json
"""
import json
import os
import sys
from glob import glob

ROOT = 'src/content/docs/reference/workflow-steps'


def main():
    if not os.path.isdir(ROOT):
        sys.exit(f'run from the repo root — {ROOT} not found')
    pages, areas = set(), set()
    for path in glob(os.path.join(ROOT, '*', '*')):
        if not path.endswith(('.md', '.mdx')):
            continue
        area = os.path.basename(os.path.dirname(path))
        slug = os.path.basename(path).rsplit('.', 1)[0]
        if slug == 'index':
            areas.add(f'{area}/')
        else:
            pages.add(f'{area}/{slug}')
    json.dump({'pages': sorted(pages), 'areas': sorted(areas)}, sys.stdout, indent=2)
    sys.stdout.write('\n')


if __name__ == '__main__':
    main()
