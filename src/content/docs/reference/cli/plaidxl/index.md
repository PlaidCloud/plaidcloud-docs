---
title: PlaidXL
description: Use the PlaidXL Excel add-in to sign in to your PlaidCloud workspace, pull project tables and dimension hierarchies into worksheets, refresh them on demand, and build live reports with PlaidXL custom functions.
sidebar:
  label: PlaidXL
---

PlaidXL is the PlaidCloud add-in for Microsoft Excel. It connects a workbook to your PlaidCloud workspace so your models and reports read from authoritative project tables and dimensions, not from a copy that goes stale the next time a workflow runs.

You can work with PlaidXL in two ways, and most workbooks use both:

- **The task pane** — browse your projects, pick a table or dimension, choose columns and filters, and retrieve the data into a worksheet. **Refresh All Tables** pulls current data for every table you've retrieved.
- **Custom functions** — formulas such as `=PLAIDXL.TABLE.GET_TABLE("Sales")` and `=PLAIDXL.CELL(...)` that read PlaidCloud data straight into cells. Use them to list tables and dimensions, lay out a hierarchy, and calculate rolled-up values for a report.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="Excel holds the PlaidXL task pane and PlaidXL custom functions. Both send requests, signed in as you, to a project in your PlaidCloud workspace, which returns table rows, dimension hierarchies and rolled-up values into worksheet cells." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Excel workbook</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PlaidXL task pane</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">browse, filter, retrieve, refresh</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">PLAIDXL.* functions</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tables, hierarchies, values in cells</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">PlaidCloud workspace</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Project</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tables</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">dimensions and hierarchies</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">signed in as you</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">rows, nodes, values</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">The task pane and the custom functions both read from the project you select, with your own PlaidCloud permissions.</figcaption>
</figure>

PlaidXL reads data. It doesn't write anything back to PlaidCloud, so editing a retrieved sheet never changes a project table.

## Requirements

- Excel for Microsoft 365, or Excel 2021 or later, on Windows or Mac. The PlaidCloud ribbon tab and the task pane run in desktop Excel.
- A PlaidCloud account in at least one workspace, and access to the projects you want to read. PlaidXL shows only the projects, tables and dimensions your account can already see in PlaidCloud.

## Topics

- [Install](/reference/cli/plaidxl/install/) — add PlaidXL to Excel and open the task pane
- [Sign In](/reference/cli/plaidxl/connect/) — connect to your workspace, sign out, and switch workspaces
- [Work With Tables and Dimensions](/reference/cli/plaidxl/retrieve/) — pick a project, filter a table, retrieve it into a sheet, and refresh
- [Custom Functions](/reference/cli/plaidxl/functions/) — every `PLAIDXL` function, its arguments, and what it returns
- [Build a Report With Custom Functions](/reference/cli/plaidxl/build-a-report/) — lay out a hierarchy and fill it with rolled-up values
- [The PlaidCloud Ribbon](/reference/cli/plaidxl/ribbon/) — refresh, drill, and sanitize commands
- [Troubleshooting](/reference/cli/plaidxl/troubleshooting/) — fixes for the most common problems

New to PlaidXL? The [Work in Excel With PlaidXL](/get-started/tutorials/excel-with-plaidxl/) tutorial takes you from installing the add-in to a first report in about 20 minutes.

## Related

- [Projects](/guides/projects/) — what a project holds and how to find one
- [Tables and Views](/guides/data/tables-views/) — the tables PlaidXL retrieves
- [Using Dimensions](/guides/dimensions/dimensions/) — the hierarchies PlaidXL lays out and rolls up
