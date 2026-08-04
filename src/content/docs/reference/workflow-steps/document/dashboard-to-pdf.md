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

### Dashboard Filters

Map columns from a source table to the dashboard's filters. The step renders one PDF per row of that table, applying that row's values — leave it empty to render the dashboard once, unfiltered.

### Source Filter

A filter expression narrowing which rows of the filter table are rendered.

### Options

- **Thread count** — how many renders run at once. Defaults to 8; lower it if the dashboard is heavy enough that parallel renders time out.
- **Render wait (seconds)** — how long to let the dashboard finish loading before capturing it. Defaults to 10; raise it for dashboards whose queries are slow, or the PDF captures a half-drawn page.

## Related

- [Document steps](/reference/workflow-steps/document/)
- [Dashboards (guide)](/guides/dashboards/)
- [Report steps](/reference/workflow-steps/reports/)
