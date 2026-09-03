---
title: Create Workflow (Guide)
description: Create a workflow in PlaidCloud and choose its type — Standard Serial, Standard Parallel, or Advanced (DAG canvas) — to load, transform, and export data.
sidebar:
  order: 2
---

To create a new workflow, you need an existing project. If you don't have one yet, see [Manage projects](/guides/projects/managing-projects/).

## Steps

1. Open the project that should contain the workflow.
2. Switch to the **Workflows** tab.
3. Click **New Workflow** in the toolbar.
4. Fill in the form:
   - **Name** — short, descriptive (e.g., "Monthly close — load actuals")
   - **Memo** — optional longer description for context
   - **Workflow Type** — Standard Serial (default), Standard Parallel, or Advanced (DAG canvas). See [Choosing a workflow type](#choosing-a-workflow-type) below.
   - **Trigger Remediation Workflow on Error** — optional; enable it to pick a remediation workflow (see [About remediation workflows](#about-remediation-workflows) below).
5. Click **Create**.

The workflow appears in the Workflows tab and is ready to have steps added to it. Double-click it to open the [Workflow Explorer](/guides/workflows/workflow-explorer/) and start building.

## Choosing a Workflow Type

The **Workflow Type** you pick when creating a workflow determines how its steps are arranged and run. It defaults to **Standard Serial**, and you set it from the type selector in the New Workflow form.

| Type | How steps are arranged and run |
|------|--------------------------------|
| **Standard Serial** | Steps run from the **Steps list**, one at a time, in order. |
| **Standard Parallel** | Steps run from the **Steps list**, in parallel where their dependencies allow. |
| **Advanced (DAG canvas)** | Steps are laid out on a **visual canvas** and run in dependency order, with independent branches running in parallel. Advanced also unlocks breakpoints, containers, run-from-here, simulation, and real-time collaboration. |

A fourth type, **Macro** — a reusable, callable workflow with declared inputs and outputs — is coming soon and appears in the selector as disabled.

:::note
A step can only appear once in a workflow. Inserting, copying, cloning, or importing a step into a position that would place it in a workflow a second time is refused, naming the step — so you can't create this state going forward. If a workflow from before that fix still has one in two places, it fails a **Standard Serial** run immediately with an error naming the duplicated step — as it does a **Standard Parallel** run stopped at a chosen end step (see [Running a Range of Steps in a Workflow](/guides/workflows/running-a-range-of-steps-in-a-workflow/)), since running to an end point also runs sequentially. A **Standard Parallel** run to completion tolerates the duplicate and simply runs it once. Either way, delete the duplicate step to repair the workflow — removing steps is never restricted.
:::

Choose **Advanced (DAG canvas)** here if you want the [Visual Workflow Designer](/guides/workflows/advanced-workflows/) from the start. The choice isn't permanent: you can promote a Standard workflow later with **Convert to Advanced…** from the Workflows list.

## About Remediation Workflows

If the new workflow ends in an error, PlaidCloud can automatically run a **remediation workflow** in response. This is useful for:

- Sending a notification to a Slack channel, email distribution list, or webhook so someone investigates
- Triggering a rollback or cleanup workflow that restores a known-good state
- Logging the failure to an audit table

A remediation workflow is optional. You can leave it blank now and configure it later if needed. The remediation workflow only fires on terminal failures, not on per-step warnings.

## Next Steps

- [Workflow explorer](/guides/workflows/workflow-explorer/) — add steps to your new workflow
- [Advanced workflows](/guides/workflows/advanced-workflows/) — choose a workflow type and build on the visual canvas
- [Run a workflow](/guides/workflows/run-a-workflow/) — execute the workflow once it has steps
- [Managing step errors](/guides/workflows/managing-step-errors/) — debugging failures
