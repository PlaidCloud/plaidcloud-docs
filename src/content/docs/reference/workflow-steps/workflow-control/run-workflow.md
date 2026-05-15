---
title: Run Workflow
description: Run an existing workflow from a PlaidCloud workflow step to chain workflow execution and build multi-workflow processing pipelines.
sidebar:
  order: 2
---

## Description

Triggers another workflow as part of the current workflow's execution. Use this to chain workflows together when one process logically depends on another — for example, a "month-end close" workflow that calls a "load actuals" workflow, then a "run allocations" workflow, then a "publish dashboards" workflow.

The called workflow runs independently — it can be in the same project or a different one. By default the calling workflow continues without waiting; set the **Wait until processing completes** option if the next steps in the caller depend on the called workflow finishing first.



## Workflow to Run


First, select the Project which contains the workflow to be run from the **Project** dropdown menu.



Next, select the particular workflow to be run from the **Workflow** dropdown menu.



Additionally, there is an option to **Wait until processing completes before continuing.** Selecting this checkbox will defer execution of the current workflow until the called workflow is completed with its execution. By default, this option is disabled, meaning that the current workflow in which this transform resides will continue processing in parallel along with the called workflow.







## Examples

No examples yet...
