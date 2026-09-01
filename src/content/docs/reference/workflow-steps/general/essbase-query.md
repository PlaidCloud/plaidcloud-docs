---
title: Essbase Query
description: Run a live MDX query against an Oracle Essbase cube and land the result grid in a workflow table, with columns derived from the grid and row access applied to the result.
sidebar:
  order: 12
---

## Description

The **Essbase Query** step runs an MDX `SELECT` against an Oracle Essbase cube and writes the returned grid to a target table. It is a **true live query** — the step sends the MDX and reads the resulting grid synchronously, so each run reflects the cube's current numbers. It is not an extract or a poll: there is no staging job to wait on and no snapshot that goes stale between runs.

Use it to pull a specific slice of a cube — a set of accounts by period, a scenario comparison, a driver set for an allocation — into a PlaidCloud table you can then transform, join, or report on alongside the rest of your data.

## Prerequisites

- An [Oracle Essbase connection](/reference/connectors/erp/oracle-essbase/) pointing at Essbase 21c+ or Oracle Analytics Cloud (OAC), with a service account that can read the application and cube you want to query.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 120" role="img" aria-label="Flow from an Essbase connection through the chosen application and cube, an MDX query, and the returned grid into a target table." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="eq-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="70" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Connection</text>
<rect x="176" y="42" width="130" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="241" y="63" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Application</text><text x="241" y="78" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">/ Cube</text>
<rect x="352" y="42" width="120" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="412" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">MDX SELECT</text>
<rect x="518" y="42" width="80" height="42" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="558" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Grid</text>
<rect x="632" y="42" width="80" height="42" rx="8" fill="var(--sl-color-accent)" stroke="var(--sl-color-accent)" /><text x="672" y="68" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Table</text>
<path d="M130 63 L172 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M306 63 L348 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M472 63 L514 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" /><path d="M598 63 L628 63" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#eq-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">The MDX runs live against the cube; the returned grid lands in the target table with columns derived from the grid itself.</figcaption>
</figure>

## Configuration

- **Connection** — an Oracle Essbase connection. The edit shortcut beside the picker opens the connection editor for viewing or editing.
- **Application** — the Essbase application to query. The picker lists the applications the connection's service account can see; if the connection sets a default application, it is pre-selected.
- **Cube (Database)** — the cube within the chosen application to query against.
- **MDX** — the MDX `SELECT` statement to run. Build it with the guided member selection, or write it directly (see below).
- **Target Table** — the table the returned grid is written to.

## Building the Query

You can produce the MDX two ways:

- **Guided member selection.** Browse the cube's dimensions and members and pick what goes on columns and on rows; the step assembles the MDX for you. Members load one level at a time as you expand them, so a large outline stays responsive.
- **Raw MDX.** Write or paste an MDX `SELECT` directly — the escape hatch for anything the guided picker doesn't cover, such as calculated members, functions, or set operators.

Both paths produce the same `MDX` value that the step runs; the guided picker is a starting point you can always edit by hand.

## Results and Schema-on-Read

The grid Essbase returns is written to the target table with its **columns derived from the returned grid** — schema-on-read. You don't declare a column list up front:

- Column names come from the grid's header rows. A header cell that spans nothing (the corner above the row labels) becomes `column_1`, `column_2`, and so on; duplicate names are made unique with a numeric suffix.
- A column whose data cells are all numeric is typed as numeric; anything else is typed as text. Empty Essbase cells land as nulls.

Because the shape follows the query, changing what the MDX puts on columns changes the table's columns on the next run — keep that in mind for downstream steps that reference specific column names.

## Row Access

[Row-level security](/administration/access/managing-security-groups-and-assignments/#managing-row-access) applies to the landed table exactly as it does to any other PlaidCloud table. Governance is enforced on the result the step writes, so a reader with a row restriction sees only the rows their security group allows — the query runs with the connection's service account, but the table it produces is governed like the rest of your data.

## Example

This MDX puts two measures on columns and two products on rows:

```mdx
SELECT
  {Sales, COGS} ON COLUMNS,
  {[100-10], [200-10]} ON ROWS
FROM Sample.Basic
```

Running it against a cube that returns those four numbers lands a table like:

| column_1 | Sales | COGS |
|---|---|---|
| 100-10 | 678.0 | 271.0 |
| 200-10 | 551.0 | 235.0 |

The row-label column has no header in the grid, so it becomes `column_1` (text); `Sales` and `COGS` are all-numeric and land as numeric columns.

## Related

- [Oracle Essbase Connector](/reference/connectors/erp/oracle-essbase/) — create and test the connection this step uses.
- [REST Request](/reference/workflow-steps/general/rest-request/) — the general-purpose step for other live HTTP requests.
