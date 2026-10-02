---
title: Convert Dashboard to PDF
description: Render a PlaidCloud dashboard to PDFs in a document account, once per row of a filters dataset, with each row's values applied as the dashboard's filters.
sidebar:
  order: 22
---

## Description

Renders a dashboard to PDFs and writes them to a document account. Use it to put a dashboard on a schedule — a month-end pack, a distribution to people who do not log in, or an archived snapshot of what the numbers looked like on a given day.

The step renders once per row of a filters dataset, applying that row's values as the dashboard's filters, so one step can produce a per-region or per-entity set of PDFs in a single run.

## Configuration

### Dashboard

The dashboard to render.

### Filters Dataset

The table whose rows drive the renders: one PDF per row.

### Output Path

The document account and folder the PDFs are written to.

### Options

- **Concurrent PDF Generation** — how many renders run at once. Defaults to 8; lower it if the dashboard is heavy enough that parallel renders time out.
- **Render Wait Time (seconds)** — present in the step configuration but **not currently applied** by the workflow runner. Setting it has no effect today.

### Dashboard Filters

The dashboard's own filters, each with its **Dashboard Filter ID**. They are read from the dashboard when you populate the mapping.

### Source Column Mapping

The filters dataset's columns, and how each one is used. Use **Inspect Source › Populate Mapping Table** to read the columns and the dashboard's filters; a column named like a dashboard filter is tagged as a filter on it. Populating again keeps the **Kind** and **Mapped Filter Column** you have already set on a column.

Set each column's **Kind**:

- **Column Filter** — the column's value sets the dashboard filter named in **Mapped Filter Column**, which must be one of the dashboard's filters.
- **File Name** — the column supplies each PDF's file name. Only one column can be the File Name. Without one, the step warns and generates names automatically.
- **No Filter** — the column isn't used.

At least one column must be a **Column Filter**.

## What's Checked When You Save

Saving the step is refused, naming the column, when:

- No column is a Column Filter with a Mapped Filter Column — *Tag at least one source column as a Column Filter, with the Mapped Filter Column it sets.*
- A Column Filter has no Mapped Filter Column, or names one that isn't among the dashboard's filters — *The Mapped Filter Column 'Region' for source column 'region' isn't one of the dashboard's filters.*
- More than one column is the File Name — *Only one source column can be the File Name; region, entity all are.*
- A Column Filter or File Name column has no data type — *Source column 'region' has no data type; inspect the source again to refresh it.* Some steps saved in the step form are missing their columns' types, and fail every run until they get them back. Run **Inspect Source › Populate Mapping Table** to restore them; your Column Filter and File Name tags are kept.

## Related

- [Document steps](/reference/workflow-steps/document/)
- [Dashboards (guide)](/guides/dashboards/)
- [Report steps](/reference/workflow-steps/reports/)
