---
title: Convert Dashboard to PDF
description: Render a PlaidCloud dashboard to a PDF in a document account, optionally once per row of a filter table.
sidebar:
  order: 22
---

## Description

Renders a dashboard to a PDF and writes it to a document account. Use it to put a dashboard on a schedule — a month-end pack, a distribution to people who do not log in, or an archived snapshot of what the numbers looked like on a given day.

Supply a filter table and the step renders once per row, so one step can produce a per-region or per-entity set of PDFs in a single run.

## Configuration

### Dashboard

The dashboard to render.

### Output Path

The document account and folder the PDFs are written to.

### Source Columns

Each source column is marked with a **kind**:

- **Filter** — the column feeds a dashboard filter, named by the filter column you map it to.
- **Filename** — the column supplies the output PDF's file name. Without one, the step warns and generates names automatically.

The step renders one PDF per row of the source table, applying that row's filter values. Leave the filter columns unmapped to render the dashboard once, unfiltered.

### Dashboard Filters

The dashboard-side filters the mapped source columns drive.

### Source Filter

A filter expression narrowing which rows of the source table are rendered.

### Options

- **Thread count** — how many renders run at once. Defaults to 8; lower it if the dashboard is heavy enough that parallel renders time out.
- **Render wait (seconds)** — present in the step configuration but **not currently applied** by the workflow runner. Setting it has no effect today.

## Related

- [Document steps](/reference/workflow-steps/document/)
- [Dashboards (guide)](/guides/dashboards/)
- [Report steps](/reference/workflow-steps/reports/)
