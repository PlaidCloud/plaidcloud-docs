---
title: Set Project Variable Values from Table
description: Read values out of a project table and assign them to project variables that persist across workflow runs.
sidebar:
  order: 17
---

## Description

Reads values out of a project table and assigns them to *project* variables. Unlike [Set Workflow Variable Values from Table](/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/), the values persist beyond the run — every workflow in the project sees them until something changes them again.

Use it for state that outlives a single run: the last period successfully loaded, a watermark timestamp, or a current-scenario name.

## Configuration

### Source Columns

Map each source column to the project variable it populates. The step reads a single row, so narrow the table to one row before it runs.

### Select Subset of Data

A filter expression that narrows the source rows.

### Apply Secondary Filter to Result Data

A `HAVING`-style filter applied after aggregation.

### Final Data Table Slicing (Limit)

Off by default, and limited to one row when on. Turn it on with an explicit ordering when the source could return several candidate rows.

## Related

- [Workflow control steps](/reference/workflow-steps/workflow-control/)
- [Set Project Variable](/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table](/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
