---
title: Troubleshooting PlaidXL
description: Fixes for common PlaidXL problems — the add-in missing from the ribbon, a sign-in pop-up that doesn't open, missing workspaces or projects, tables shown in red, slow retrieves, errors in PlaidXL formulas and metrics, typed values that aren't written, and saves that stop.
sidebar:
  label: Troubleshooting
  order: 7
---

## The PlaidCloud Tab Isn't on the Ribbon

- Close every Excel window and reopen Excel. A newly installed add-in often appears only after a restart.
- Open **Insert → My Add-ins** and select **PlaidCloud**.
- Check that you're using desktop Excel for Microsoft 365, or Excel 2021 or later. See [Install PlaidXL](/reference/cli/plaidxl/install/).
- If your organization manages add-ins, ask your Microsoft 365 administrator whether the **PlaidCloud** add-in is deployed to you.

## The Sign-In Pop-Up Doesn't Open

When you click **Sign In**, Excel asks whether to show a pop-up window. Allow it. If you dismissed the prompt, click **Sign In** again.

If the pop-up opens but you can't finish signing in, try signing in to PlaidCloud in your browser with the same email. A problem there — an expired password or a two-factor device you no longer have — needs to be fixed in PlaidCloud first. See [Member Authentication](/administration/access/member-authentication/).

## A Workspace Isn't Listed

**Select a workspace** lists the workspaces your email address belongs to. If one is missing, check that you typed the same email you use for that workspace, then ask a workspace administrator to confirm you're a member. See [Managing Workspace Members](/administration/access/overview/managing-workspace-members/).

To move to another workspace you belong to, open the account menu and choose **Switch workspace**.

## A Project, Table or Dimension Is Missing

PlaidXL shows what your account can see in PlaidCloud. If a project is missing, ask its owner to give you access. If a table is missing, check that it exists in the selected project and has been loaded with data — a table that's never been written shows **Unable to get table metadata** when you select it.

Folders in the project, table and dimension lists start collapsed. Type part of the name in the filter box at the top of the list to find an item inside a folder.

## A Table Shows in Red

The table has more rows or columns than an Excel worksheet holds, or PlaidCloud can't report its size. You can retrieve it, and rows that don't fit continue on further sheets, but a table split across sheets can't be saved. Select **Advanced** to filter the rows, and clear the columns you don't need, until it fits. See [Tables Shown in Red](/reference/cli/plaidxl/retrieve/#tables-shown-in-red).

## A Retrieve Is Slow

Excel is slowest with wide tables. Clear the check boxes of columns you don't need, and filter the rows with **Advanced**. Retrieving only the data you work with is faster and makes a smaller workbook.

Large tables retrieve and refresh much faster in Excel on the web and in current desktop Excel. Older versions of Excel still work, just without the speed-up.

If the pane says **PlaidXL was updated — reload the pane**, close the task pane, open it again, and retrieve again. After PlaidXL is updated, the pane picks up the new version the next time it loads.

If a pull says **This PlaidCloud workspace needs an update for PlaidXL**, ask your administrator to update the workspace to a current PlaidCloud release.

## A Formula Shows an Error

| What you see | What to check |
|---|---|
| `#SPILL!` | Something is in the cells the result needs. Clear the cells below or beside the formula. |
| `#NAME?` | Excel doesn't recognize the function. Check that PlaidXL is installed — the **PlaidCloud** tab is on the ribbon — and check the spelling against [the function list](/reference/cli/plaidxl/functions/). |
| An error from a `PLAIDXL` function | Check that you're signed in and the right project is selected, then check every table, column, dimension and node name against PlaidCloud — names must match exactly. |
| `CELL` reports that a filter column isn't found | The first argument of `DIMENSION_REPR` is a column of the table, not a dimension. Use the table's column name exactly. See [Values](/reference/cli/plaidxl/functions/#values). |
| `#VALUE!` from `METRIC` or `METRIC_BREAKDOWN` | Hover over the cell to read the reason. See [Metric Errors](/reference/cli/plaidxl/functions/#metric-errors). |
| `#VALUE!` from a metric: **This PlaidCloud workspace can't combine an alternate hierarchy with other members yet. Ask your administrator to update the workspace.** | The workspace needs updating before a metric can mix an alternate-hierarchy member with other members. Ask your administrator. Other cells in the same recalculation still answer. |
| `#VALUE!` from `CELL` or `CELLS` | Hover over the cell to read the reason PlaidCloud gave, such as an unknown column, a node that doesn't exist or has no members, or a problem computing the value. Check the names against PlaidCloud. |
| `CELL` returns an unexpected total | A node rolls up only on a column linked to its dimension; on any other column it must match a value exactly. Check each filter's column and node. |
| Values don't change after the data or project changes | Click **Recalculate PlaidXL formulas** in the ribbon's **Refresh** menu. |
| `MEASURE_TYPE` returns an error | Use one of `sum`, `mean`, `median`, `min`, `max`, `std` or `var`, in lowercase. |

## Formulas Return Another Project's Data

PlaidXL functions read from the project linked to the workbook. Open the task pane in that workbook, choose the project the report was built for, then click **Recalculate PlaidXL formulas** in the ribbon's **Refresh** menu. Each workbook has its own project, so choosing one in another workbook doesn't change this one. See [The Project Belongs to the Workbook](/reference/cli/plaidxl/retrieve/#the-project-belongs-to-the-workbook).

## Tables From Another Workspace Are Skipped

After you switch workspace, **Refresh All Tables** says that tables or dimensions from another workspace in this workbook were not refreshed, and they aren't listed under **On this sheet**. Retrieve each table again in the current workspace to link it.

## A Typed Value Isn't Written

When you type over a `CELL`, the task pane says what it wrote and lists anything it didn't, with the reason. See [Type Values Into PlaidCloud](/reference/cli/plaidxl/write-values/).

| What you see | What to do |
|---|---|
| Only a cell holding just one `PLAIDXL.CELL` takes a typed value | Type over a cell whose formula is a single `CELL`, optionally multiplied, divided or negated. |
| An argument can't be read here | The `CELL`'s arguments must be cells or text, not other calculations. |
| A spread method, shape or hold applies to sums only | Codes such as `E1200`, `1200 like FY2025` and `H` work only on **sum** cells. Type a plain number on others. |
| All members held | Release a hold with `H`, then type the value again. |
| The workspace doesn't take values typed in Excel yet | Ask your administrator to update the workspace. |

## A Save Is Refused or Stopped

A save writes straight away and rarely stops. It does when:

| What you see | What to do |
|---|---|
| The header row no longer matches the retrieved columns | Put the header back as it was retrieved, or retrieve the table again. |
| A value can't be converted | Nothing is written and the rows are listed. Correct the values to match the column's data type. |
| The table continues on other sheets | A table split across sheets can't be saved. Retrieve it with a filter so it fits on one sheet. |
| The table was retrieved with a filter Save can't keep to | Retrieve it again with a filter of **equal** and **in** rules joined by **AND**, or none. |
| Rows are outside your row access | Nothing is saved. Remove those rows, then save again. |
| Columns hold text longer than an Excel cell's 32,767 characters | Excel shows the text cut, and saving would cut it in PlaidCloud too, so Save is off for this table. Retrieve the table without those columns to save it. |
| The table was only partly written | Excel refused part of the last refresh. Refresh the table, then save it. |
| The sheet isn't linked to a table | Retrieve the table to the sheet first. Only tables retrieved into the active sheet are listed under **On this sheet**. |

To undo a save, click **Undo** in the message or **Undo last write** on the ribbon. Each save keeps its own restore point for 7 days, so you can undo any save for up to 7 days after you made it. See [Save a Table to PlaidCloud](/reference/cli/plaidxl/retrieve/#save-a-table-to-plaidcloud).

## Related

- [Install PlaidXL](/reference/cli/plaidxl/install/)
- [Sign In to PlaidXL](/reference/cli/plaidxl/connect/)
- [Getting Help](/guides/support/getting-help/) — open a support ticket
