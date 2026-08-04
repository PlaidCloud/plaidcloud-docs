---
title: Set Workflow Variable Values from Table
description: Read values out of a project table and assign them to workflow variables, so later steps branch or filter on data rather than on hard-coded values.
sidebar:
  order: 16
---

## Description

Reads values out of a project table and assigns them to workflow variables. Use it to drive a workflow from its own data — read the latest closed period, a row count, or a file path out of a control table and let downstream steps reference it.

The variables set here live for the workflow run. To set values that persist across workflows in the project, use [Set Project Variable Values from Table](/reference/workflow-steps/workflow-control/set-project-variable-from-table/).

## Configuration

### Source Columns

Map each source column to the workflow variable it populates. The step reads a single row, so narrow the table to one row before it runs.

### Select Subset of Data

A filter expression that narrows the source rows — typically to the one row holding the values you want.

### Apply Secondary Filter to Result Data

A `HAVING`-style filter applied after aggregation, for when the value comes from a grouped calculation.

### Final Data Table Slicing (Limit)

Off by default, and limited to one row when on. Turn it on with an explicit ordering when the source could return several candidate rows and you want a specific one.

## Related

- [Workflow control steps](/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable](/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table](/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
