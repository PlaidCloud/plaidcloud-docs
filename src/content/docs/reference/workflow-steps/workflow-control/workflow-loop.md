---
title: Worklow Loop
description: Create a loop in a PlaidCloud workflow step to iterate over a set of values and repeat steps for each item in the collection.
sidebar:
  order: 9
---

## Description

Runs a target workflow once per row of a dataset, setting each row's column values as project variables before each iteration. Use this when you have a parameterized process that needs to run multiple times with different inputs — for example, "run the monthly close for every business unit in this table," or "load this report for every quarter listed."

Each loop iteration sees the variables as if they had been set manually, so the called workflow can reference them in expressions, filters, file paths, and table names using the standard `\{variable_name}` syntax. The loop is sequential by default; iterations don't run in parallel.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="A Workflow Loop over a dataset with rows Q1, Q2, and Q3. Each row's column values become project variables, then the target workflow runs — one pass per row, in sequence, not in parallel." style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">dataset</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">pass 1</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">pass 2</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">pass 3</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">sequential — one pass at a time, not in parallel</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Each row's columns become project variables, then the target workflow runs — one pass per row, in sequence. For isolated parallel fan-out instead, use a <a href="/guides/workflows/create-a-macro/">Macro</a>.</figcaption>
</figure>



## Workflow to Stop


First, select the Project which contains the workflow that will be run on each loop from the **Project** dropdown menu.



Next, select the particular workflow for running from the **Workflow** dropdown menu.

## Examples

Examples coming soon
