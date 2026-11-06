---
title: Get Workspace Usage
description: Write workspace usage totals from Usage Reports into a project table, by day or month, so you can chart adoption or feed a downstream step.
sidebar:
  order: 12
---

## Description

Writes a summary of how your workspace is used into a project table. Use it to track adoption over time, to build your own dashboards on usage, or to flag a drop in activity in a scheduled workflow. The figures are the same ones [Usage Reports](/administration/access/usage-reports/) shows.

The output holds totals only. No row names a member, and notebook paths are replaced with `*`. Members whose usage was erased are left out.

## Configuration

### Usage Data

**Dataset** chooses what each row holds:

| Dataset | One row for each | Columns |
|---|---|---|
| **Daily per item** | Day, area, event and subject | `day`, `source`, `event`, `subject`, `events` |
| **Monthly per item** | Month, area, event and subject | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Monthly totals** (default) | Month and area | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` is true for a month that history doesn't cover in full, and `coverage_start` is the date collection began.

**Area** limits the rows to one area: **PlaidCloud app**, **Dashboards**, **Apps**, **App visits**, **Notebook servers** or **Notebooks**. Leave it on **All areas** to include all of them.

### Date Range

**Range** chooses the days to read:

- **Last number of days** (default 30) reads the most recent days, today included.
- **Previous month** reads the last full calendar month.
- **Month to date** reads from the first of this month to today.
- **Between dates** reads from **Start Date** to **End Date**. Leave **End Date** empty to read to today.

Days and dates are UTC. **Days**, **Start Date** and **End Date** accept a [variable](/guides/workflows/manage-workflow-variables/) such as `{report_start}` as well as a number or a `YYYY-MM-DD` date. The start must not be after the end.

### Usage Target

**Target Table** receives the result. The step replaces whatever the table held, and always writes the dataset's columns, even when there are no rows.

## Warnings

These don't fail the step. It finishes with a warning that says what happened, and still writes the table:

- Usage collection isn't set up for the workspace yet.
- There was no usage in the range.
- The range starts before what is kept, so it was cut to start where history begins. Daily data is kept for 180 days and monthly data for 25 months.

## Security Log

Each run writes an entry to the Security Log recording the dataset, the range, the target table, the workflow, step and run, and the number of rows written.

## Related

- [General steps](/reference/workflow-steps/general/)
- [Usage Reports](/administration/access/usage-reports/)
- [Get Workspace Members](/reference/workflow-steps/general/get-workspace-members/)
