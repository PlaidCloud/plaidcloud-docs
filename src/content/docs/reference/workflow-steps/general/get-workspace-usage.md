---
title: Get Workspace Usage
description: Write workspace usage into a project table as activity, members, content or trends, so you can report adoption or feed a downstream step.
sidebar:
  order: 12
---

## Description

Writes how your workspace is used into a project table. Use it to track adoption over time, to report usage by department or team, to build your own dashboards, or to flag a drop in activity in a scheduled workflow. The figures come from the same usage data as [Usage Reports](/administration/access/usage-reports/), and every dataset covers all areas.

**Activity** and **Members** hold member identity (user ID, user name, email, first and last name and security groups). The target table is an ordinary project table, so anyone with access to the project can read it: treat it as you would any member list. Each run that writes the table is recorded in the Security Log.

## Configuration

### Usage Data

**Dataset** chooses what each row holds. The text under it describes the rows and names the main columns of the one you choose.

| Dataset | Value | One row for each | Holds identity |
|---|---|---|---|
| **Activity** (default) | `activity` | Day, member, action and item | Yes |
| **Members** | `members` | Member, including members with no activity | Yes |
| **Content** | `content` | Dashboard, app and notebook, including dashboards and apps nobody used | No |
| **Trends** | `trends` | Day, week and month of the range | No |

The values are what a step holds when you create or edit it through the API or an AI assistant. A step saved with a dataset that isn't in this list fails when it runs, naming the four datasets: open it, choose a **Dataset** and save it. A **Members** or **Content** step saved before keeps running and writes the columns below, and a step that was limited to one area now covers all areas. In **Content**, `subject` is now `item_id` and `type` holds `Dashboard`, `App` or `Notebook`.

### Columns

Dates and days land as timestamps at midnight UTC.

#### Member Columns

**Activity** and **Members** include these columns:

| Column | Holds |
|---|---|
| `user_id` | The member's ID. |
| `user_name` | The member's user name. |
| `email` | The member's email address, in lowercase. |
| `first_name` | First name. |
| `last_name` | Last name. |
| `is_active` | True when the member is active, false when deactivated. |
| `groups` | The member's security groups, separated by `; `. |

`groups` lists the top-level groups the member belongs to directly.

#### Activity

| Column | Holds |
|---|---|
| `day` | The day. |
| The member columns | As above. |
| `member` | The member's first and last name, or their user name when neither is set. |
| `area` | `PlaidCloud app`, `Dashboards`, `Apps` or `Notebooks`. |
| `action` | `Opened app`, `Opened screen`, `Opened step`, `Saved step`, `Used palette action`, `Viewed dashboard`, `Used chart`, `Opened notebook` or `Saved notebook`. |
| `item_type` | `App area`, `Screen`, `Step`, `Palette action`, `Dashboard`, `Chart`, `App` or `Notebook`. |
| `item_id` | The item's ID. For a notebook, its path. |
| `item_name` | The item's name: a screen or app area in words, such as `Members List`; the step type; the dashboard, chart or app name; or the notebook's path. When a name can't be found, the item's ID. |
| `events` | How many times the member did it that day. |
| `source` | The area's key, as the [Usage Reports](/administration/access/usage-reports/) exports name it. |
| `event` | The action's key, as the exports name it. |

`member` and the member columns depend on who did it:

- Activity no member can be linked to has `Unattributed` in `member` and blank member columns.
- A member deleted since keeps only `user_id`, and `member` is `Deleted user`.
- Any other account, such as a service account or agent, keeps only `user_id`, and `member` is its user name.

`Used chart` counts once per member and chart in each 5-minute window, so it measures use, not queries.

#### Members

| Column | Holds |
|---|---|
| The member columns | As above. |
| `member` | The member's first and last name, or their user name when neither is set. |
| `created` | The day the member was added to the workspace, when known. |
| `status` | `Active` when the member was active in the range, `Dormant` when they used PlaidCloud before but not in the range, `Never active` when there is no use on record by the end of the range. |
| `first_seen` | The first day on record that the member used PlaidCloud, whatever the range. |
| `last_seen` | The member's last day of activity in the range. |
| `active_days` | Days with activity in the range. |
| `events` | Activity events in the range. |
| `active_minutes` | Minutes of activity in the range. |
| `session_minutes` | Minutes in sessions in the range. |
| `app_open_minutes` | Minutes the member had Panel apps open in the range. Studio previews aren't counted. |

Every member has a row, deactivated members included, except members whose usage was erased. Service accounts and agents aren't listed. A member with no activity in the range has no `last_seen`, and their other activity columns are blank.

#### Content

| Column | Holds |
|---|---|
| `type` | `Dashboard`, `App` or `Notebook`. |
| `item_id` | The dashboard's or app's ID, or the notebook's path. |
| `name` | The dashboard or app name, or the notebook's path. Blank when the item has been deleted or names can't be read. |
| `deleted` | True when the dashboard or app has since been deleted. |
| `unused` | True for a dashboard or app nobody used in the range. |
| `users` | Members who used it in the range. |
| `opens` | Times it was opened in the range, including opens no member can be linked to. |
| `last_used` | The last day it was used in the range. For an unused item, the last day it was opened before the range ended, or blank. |
| `app_open_minutes` | Minutes a Panel app was open in the range. Blank for dashboards, notebooks, and Dash and WASM apps. |

Each notebook path has its own row. The rows list what was used first, most users first, then the dashboards and apps nobody used. Those are the published dashboards and apps that already existed when the range began. They are listed only when the range starts within the daily data that is kept, usage of that kind of item was being collected by then, and names can be read. Studio previews of apps are left out.

#### Trends

| Column | Holds |
|---|---|
| `period` | `Day`, `Week` or `Month`. |
| `period_start` | The period's first day. Weeks start on Monday. |
| `active_members` | Members active in the period, within the range. |
| `events` | Activity events in the period. |
| `active_minutes` | Minutes of activity in the period. |
| `session_minutes` | Minutes in sessions in the period. |
| `active_members_7d` | On a `Day` row, members active in the 7 days ending that day. |
| `active_members_28d` | On a `Day` row, members active in the 28 days ending that day. |
| `stickiness` | On a `Day` row, `active_members` divided by `active_members_28d`. |
| `complete` | False for today, for a week or month that holds today, and for a week or month the range cuts. |

Every day of the range, from where the kept daily data begins, has a row, even with no usage, and so does every week and month those days fall in. `active_members_7d`, `active_members_28d` and `stickiness` are blank on `Week` and `Month` rows, and on a `Day` row whose 7 or 28 days reach before the daily data that is kept. `stickiness` is also blank when `active_members_28d` is 0. A month that starts before the kept daily data and lies wholly in the range comes from the monthly summaries: it has `active_members` but blank events and minutes, and `complete` says whether the summary covered the whole month.

### Example: Active Minutes by Department

**Activity** and **Members** carry the member's `email`, in lowercase, so you can join them to a table of your own, such as an HR or org master table, and report by department.

1. Add a **Get Workspace Usage** step with **Dataset** set to **Members**, and a target table such as `usage_members`.
2. Add a **Table: Inner Join** step that joins `usage_members` to your org table where the lowercase `email` columns match. Keep the department from your table and the `active_minutes` and `events` columns from `usage_members`.
3. In the same step, aggregate by department and sum `active_minutes`.

The result is active minutes by department. Members who aren't in your org table drop out of an inner join, so use a left join if you want to see them. Repeat with a second step on **Activity** and sum `events` by department and `item_name` to report who uses which dashboards and apps.

### Date Range

**Range** chooses the days to read:

| Range | Value | Reads |
|---|---|---|
| **Last number of days** (default 30) | `last_days` | The most recent days, today included. |
| **Previous month** | `previous_month` | The last full calendar month. |
| **Month to date** | `month_to_date` | From the first of this month to today. |
| **Between dates** | `dates` | From **Start Date** to **End Date**. Leave **End Date** empty to read to today. |

Days and dates are UTC. **Days** takes a whole number. **Start Date** and **End Date** take a `YYYY-MM-DD` date or a [variable](/guides/workflows/manage-workflow-variables/) such as `{report_start}`. The start must not be after the end.

Daily data is kept for 180 days and monthly summaries for 25 months.

### Usage Target

**Target Table** receives the result. The step replaces whatever the table held, and always writes the dataset's columns, even when there are no rows.

## Warnings

These don't fail the step. It finishes with the warning and still replaces the table, with the columns of the dataset:

| Warning | Meaning |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | Usage collection isn't set up for the workspace yet. |
| "Usage data is not available right now: the usage database could not be reached." | The usage data couldn't be read. Run the step again later. |
| "No usage from *start* to *end*." | There was no usage in the range. |
| "Usage before *date* isn't kept, so the range was clipped to start there." | The range starts before the daily data that is kept, so activity is counted from *date*. **Trends** still has the whole months before it from the monthly summaries. |
| "This took too long to compute: narrow the date range." | The read ran out of time, so the table has no rows. Choose a shorter range. |
| "Some names are unavailable right now, so those items are named by their id." | **Activity** only. Some dashboard, chart or app names couldn't be read, so `item_name` holds the ID. |
| "Members could not be read right now, so they are named by their id." | **Activity** only. The member list couldn't be read, so `member` holds the member's ID and, of the member columns, only `user_id` is filled. |
| "Names are unavailable right now, so items nobody used are not listed." | **Content** only. Dashboard or app names couldn't be read, so only used items are listed. |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | **Content** only. The range starts before the daily data that is kept, so only used items are listed. |

When the member list can't be read, **Members** fails instead, and leaves the target table as it was.

## Security Log

Each run that writes the table adds an entry to the Security Log recording the dataset, the range, the target table and its project, the workflow, step and run, the number of rows written and, for **Activity** and **Members**, that the rows hold member identity.

## Related

- [General steps](/reference/workflow-steps/general/)
- [Usage Reports](/administration/access/usage-reports/)
- [Get Workspace Members](/reference/workflow-steps/general/get-workspace-members/)
