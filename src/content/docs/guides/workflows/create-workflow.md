---
title: Create Workflow (Guide)
description: Create a new workflow in PlaidCloud to define a sequence of data processing steps for loading, transforming, and exporting data.
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
   - **Remediation workflow** — optional; see below
5. Click **Create**.

The workflow appears in the Workflows tab and is ready to have steps added to it. Double-click it to open the [Workflow Explorer](/guides/workflows/workflow-explorer/) and start building.

## About Remediation Workflows

If the new workflow ends in an error, PlaidCloud can automatically run a **remediation workflow** in response. This is useful for:

- Sending a notification to a Slack channel, email distribution list, or webhook so someone investigates
- Triggering a rollback or cleanup workflow that restores a known-good state
- Logging the failure to an audit table

A remediation workflow is optional. You can leave it blank now and configure it later if needed. The remediation workflow only fires on terminal failures, not on per-step warnings.

## Next Steps

- [Workflow explorer](/guides/workflows/workflow-explorer/) — add steps to your new workflow
- [Run a workflow](/guides/workflows/run-a-workflow/) — execute the workflow once it has steps
- [Managing step errors](/guides/workflows/managing-step-errors/) — debugging failures
