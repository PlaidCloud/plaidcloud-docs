---
title: Table In-Place Delete
description: Delete specific rows from a table in a PlaidCloud workflow step using filter conditions to remove targeted records in place.
sidebar:
  order: 9
---

## Description


Performs a delete on the table using the specified filter conditions. The operation is performed on the designated table directly so no additional tables are created. Only the rows that meet the filter criteria are deleted. This may be an effective approach when encountering concerns related to data size.

When the step runs, it checks its source table before it deletes anything, and stops with one error that names every problem it finds. See [When the Step Runs](/reference/workflow-steps/tables/table-extract/#when-the-step-runs).



## Delete Parameters


Select the **Source** table for deleting from the dropdown list. This list includes all *Project* and *Workflow* data tables.

![Table In-Place Delete](/images/table_inplace_table_selection.png)

## Data Filters for Delete

![Table In-Place Delete](/images/table_in-place_table_filter.png)




## Examples
