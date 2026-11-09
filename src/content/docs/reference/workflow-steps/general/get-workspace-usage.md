---
title: Get Workspace Usage
description: Write workspace usage totals from Usage Reports into a project table, by day or month, so you can chart adoption or feed a downstream step.
sidebar:
  order: 12
---

## Description

Writes how your workspace is used into a project table. Use it to track adoption over time, to report usage by department or team, to build your own dashboards, or to flag a drop in activity in a scheduled workflow. The figures are the same ones [Usage Reports](/administration/access/usage-reports/) shows.

Three datasets hold totals only: no row names a member, and notebook paths are replaced with `*`. The other four (**Members**, **Daily per member**, **Content** and **Content per member**) are built for reporting. **Members**, **Daily per member** and **Content per member** hold member identity (user ID, user name, email, first and last name and security groups), so treat the target table as you would any member list. Each run of the step is recorded in the Security Log.

## Configuration

### Usage Data

**Dataset** chooses what each row holds:

| Dataset | Value | One row for each | Holds identity |
|---|---|---|---|
| **Daily per item** | `daily_item` | Day, area, event and subject | No |
| **Monthly per item** | `monthly_item` | Month, area, event and subject | No |
| **Monthly totals** (default) | `monthly_tenant` | Month and area | No |
| **Members** | `members` | Person in the workspace | Yes |
| **Daily per member** | `daily_user` | Person, day and area | Yes |
| **Content** | `content` | Dashboard, app or notebook | No |
| **Content per member** | `content_user` | Person and item | Yes |

**Area** limits the rows to one area. Leave it on **All areas** to include all of them.

| Area | Value |
|---|---|
| **All areas** (default) | `""` |
| **PlaidCloud app** | `plaidclient` |
| **Dashboards** | `superset` |
| **Apps** | `panel` |
| **App visits** | `panel_visit` |
| **Notebook servers** | `jupyterhub` |
| **Notebooks** | `jupyter` |

The values are what a step holds when you create or edit it through the API or an AI assistant.

### Columns

#### Daily Per Item

`day`, `source`, `event`, `subject`, `events`.

#### Monthly Per Item

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Monthly Totals

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` is true for a month that history doesn't cover in full, and `coverage_start` is the date collection began. A month is included 3 days after it closes, once its figures have settled.

#### Member Columns

**Members**, **Daily per member** and **Content per member** begin with the same seven columns:

| Column | Holds |
|---|---|
| `user_id` | The member's ID. |
| `user_name` | The member's user name. |
| `email` | The member's email address, in lowercase. |
| `first_name` | First name. |
| `last_name` | Last name. |
| `is_active` | True when the member is active, false when deactivated. |
| `groups` | The member's security groups, separated by `; `. |

`groups` lists top-level groups only. Subgroups aren't expanded.

#### Members

The member columns, then:

| Column | Holds |
|---|---|
| `first_seen` | The first day the member ever used PlaidCloud, whatever the date range. When you set an **Area**, it is the first day in that area. |
| `last_seen` | The member's last day of activity within the range. |
| `active_days` | Days with activity in the range. |
| `events` | Activity events in the range. |
| `active_minutes` | Minutes of activity. Overlapping minutes across areas are counted once. |
| `session_minutes` | Minutes in sessions. |
| `app_open_minutes` | Minutes the member had Panel apps open. |

Every member has a row, except members whose usage was erased. Service accounts and agents aren't listed. A member with no activity in the range has blank values after `groups`. Totals match [Usage Reports](/administration/access/usage-reports/), except for members deleted since.

#### Daily Per Member

The member columns, then `day`, `source` (the area), `events`, `active_minutes`, `session_minutes`, `first_at` and `last_at` (the first and last activity times that day).

#### Content

| Column | Holds |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` or `notebook`. |
| `subject` | The item's ID. All notebooks share one row, with `*` here. |
| `name` | The item's name, or `*` for notebooks. |
| `deleted` | True when the item has since been deleted. |
| `users` | Members who opened it. |
| `opens` | Times it was opened. |
| `last_used` | When it was last used. |
| `app_open_minutes` | Minutes Panel apps were open. |

#### Content by Member

The member columns, then `type`, `subject`, `name` (as in **Content**), `opens` (times this member opened the item) and `last_day` (the member's last day of use).

### Notes on the Member Datasets

- Activity from agents, service accounts and members deleted since has blank identity columns. A deleted member keeps the `user_id` and nothing else.
- Opens in **Content** can exceed the sum of opens in **Content per member**. The difference is opens that can't be attributed to a member, such as embedded or guest views of a dashboard. **Content** counts them, and **Content per member** can't.

### Example: Active Minutes by Department

**Members** and **Content per member** carry the member's `email`, in lowercase, so you can join them to a table of your own, such as an HR or org master table, and report by department.

1. Add a **Get Workspace Usage** step with **Dataset** set to **Members**, and a target table such as `usage_members`.
2. Add a **Table: Inner Join** step that joins `usage_members` to your org table where the lowercase `email` columns match. Keep the department from your table and the `active_minutes` and `events` columns from `usage_members`.
3. In the same step, aggregate by department and sum `active_minutes`.

The result is active minutes by department. Members who aren't in your org table drop out of an inner join, so use a left join if you want to see them. Repeat with a second step on **Content per member** and sum `opens` by department to report who uses which dashboards and apps.

### Date Range

**Range** chooses the days to read:

| Range | Value | Reads |
|---|---|---|
| **Last number of days** (default 30) | `last_days` | The most recent days, today included. |
| **Previous month** | `previous_month` | The last full calendar month. |
| **Month to date** | `month_to_date` | From the first of this month to today. |
| **Between dates** | `dates` | From **Start Date** to **End Date**. Leave **End Date** empty to read to today. |

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
