---
title: Data Engineering Learning Path
description: What to read before the PlaidCloud Data Engineering Practitioner and Expert labs, and what each lab asks you to do.
sidebar:
  label: Data Engineering
---

The Data Engineering track is about building workflows that are correct, driven by variables, and fast. Start with the [Foundations](/guides/certification/foundations/) path. For how labs work, see [PlaidCloud Certification](/guides/certification/).

## Practitioner

### Read in This Order

1. [Create Workflow](/guides/workflows/create-workflow/)
2. [Workflow Steps](/reference/workflow-steps/), in particular [Table Inner Join](/reference/workflow-steps/tables/table-inner-join/) and [Table Extract](/reference/workflow-steps/tables/table-extract/)
3. [Manage Workflow Variables](/guides/workflows/manage-workflow-variables/)
4. [Reuse Your Work: Variables, Macros, and UDFs](/get-started/tutorials/reuse-variables-macros-udfs/)
5. [Run a Workflow](/guides/workflows/run-a-workflow/)
6. [Viewing Workflow Log](/guides/workflows/viewing-workflow-log/)

### What the Lab Asks

The lab is called *Data Engineering: monthly sales build*.

Three raw tables are loaded: sales lines, stores and products. In the lab's workflow, you build a monthly summary with one row per region and product category, with units and revenue, for the sold lines of one month. The month comes from a project variable, not from a value typed into a step: the lab changes the variable and runs the workflow again. Use standard steps only, with no SQL or code steps.

The lab checks that the workflow runs, that it uses only standard steps, and that the summary is right for the month and again for another month.

## Expert

The Expert lab is timed: you have 4 hours from the moment you start it.

### Read in This Order

1. [Debug a Workflow](/get-started/tutorials/debug-a-workflow/)
2. [Viewing Workflow Log](/guides/workflows/viewing-workflow-log/)
3. [Managing Step Errors](/guides/workflows/managing-step-errors/)
4. [Preview Step Data](/guides/workflows/preview-step-data/)
5. [Optimize a Workflow](/guides/workflows/optimize-a-workflow/)
6. [Workflow Steps](/reference/workflow-steps/), in particular [Table Inner Join](/reference/workflow-steps/tables/table-inner-join/)

### What the Lab Asks

The lab is called *Data Engineering Expert: fix and speed up the nightly build*.

A nightly workflow has stopped running, and before that it was far too slow. You read the run log, find every cause, and fix the workflow so that it succeeds, produces the right summary, and finishes in a small fraction of its old time. Rows with no account are left out, and accounts listed twice must not inflate the counts. Use standard steps only, and leave the input tables as they are.

The lab checks that the workflow runs, that it uses only standard steps, that the summary is right, that the input tables are unchanged, and that the workflow is fast enough.
