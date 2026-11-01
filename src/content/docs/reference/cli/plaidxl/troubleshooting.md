---
title: Troubleshooting PlaidXL
description: Fixes for common PlaidXL problems — the add-in missing from the ribbon, a sign-in pop-up that doesn't open, missing workspaces or projects, tables shown in red, slow retrieves, and errors in PlaidXL formulas.
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

The table has more rows or columns than an Excel worksheet holds. Select **Advanced** to filter the rows, and clear the columns you don't need, until it fits. See [Tables Shown in Red](/reference/cli/plaidxl/retrieve/#tables-shown-in-red).

## A Retrieve Is Slow

Excel is slowest with wide tables. Clear the check boxes of columns you don't need, and filter the rows with **Advanced**. Retrieving only the data you work with is faster and makes a smaller workbook.

## A Formula Shows an Error

| What you see | What to check |
|---|---|
| `#SPILL!` | Something is in the cells the result needs. Clear the cells below or beside the formula. |
| `#NAME?` | Excel doesn't recognize the function. Check that PlaidXL is installed — the **PlaidCloud** tab is on the ribbon — and check the spelling against [the function list](/reference/cli/plaidxl/functions/). |
| An error from a `PLAIDXL` function | Check that you're signed in and the right project is selected, then check every table, column, dimension and node name against PlaidCloud — names must match exactly. |
| `CELL` reports that a filter column isn't found | The first argument of `DIMENSION_REPR` is a column of the table, not a dimension. Use the table's column name exactly. See [Values](/reference/cli/plaidxl/functions/#values). |
| `#VALUE!` from `CELL` or `CELLS` | Hover over the cell to read the reason PlaidCloud gave, such as an unknown column, a node that doesn't exist or has no members, or a problem computing the value. Check the names against PlaidCloud. |
| `CELL` returns an unexpected total | A node rolls up only on a column linked to its dimension; on any other column it must match a value exactly. Check each filter's column and node. |
| Values don't change after the data or project changes | Force a full recalculation — on Windows, **Ctrl+Alt+F9**. |
| `MEASURE_TYPE` returns an error | Use one of `sum`, `mean`, `median`, `min`, `max`, `std` or `var`, in lowercase. |

## Formulas Return Another Project's Data

PlaidXL functions read from the project linked to the workbook. Open the task pane in that workbook, choose the project the report was built for, then force a full recalculation. Each workbook has its own project, so choosing one in another workbook doesn't change this one. See [The Project Belongs to the Workbook](/reference/cli/plaidxl/retrieve/#the-project-belongs-to-the-workbook).

## Tables From Another Workspace Are Skipped

After you switch workspace, the task pane says how many tracked tables belong to another workspace and are skipped by **Refresh All Tables**. Retrieve each table again in the current workspace to link it.

## A Save Is Refused or Stopped

| What you see | What to do |
|---|---|
| Rows are empty inside the table | A single empty row is skipped. Two or more empty rows in a row, with data below them, stop a save. Delete the empty rows or fill them, then save again. |
| The table changed since you retrieved it | Someone else saved the table in PlaidCloud. Retrieve it again and reapply your edits. (PlaidCloud can check this only on some table types; where it can't, the confirmation warns that others' changes will be overwritten.) |
| A value can't be converted | Nothing is written and the rows are listed. Correct the values to match the column's data type. |
| The sheet isn't linked to a table | Retrieve the table to the sheet first. **Save to PlaidCloud…** appears only for tables retrieved into the active sheet. |

To undo a save, click **Restore previous version** in the confirmation message, or open the table in PlaidCloud and pick the version from before the save in the **As of** menu. The restore point is kept for 7 days. See [Save a Table to PlaidCloud](/reference/cli/plaidxl/retrieve/#save-a-table-to-plaidcloud).

## Related

- [Install PlaidXL](/reference/cli/plaidxl/install/)
- [Sign In to PlaidXL](/reference/cli/plaidxl/connect/)
- [Getting Help](/guides/support/getting-help/) — open a support ticket
