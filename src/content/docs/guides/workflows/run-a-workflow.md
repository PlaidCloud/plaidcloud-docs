---
title: Run a workflow
description: Run a PlaidCloud workflow manually or on demand, and pause, stop, or resume a run from where it left off.
sidebar:
  order: 6
---

You can trigger a full workflow run by either clicking on the run icon from the **Workflows** hierarchy or by selecting **Run All** from the **Actions** menu within a specific workflow.



You can also click on the **Toggle Start/Stop** button at the top of the workflow table. This toggle button will stop a running workflow or start a workflow.

## Pause, Stop, and Resume

While a workflow is running you can **Pause** it, so that in-flight steps finish and new steps wait, or **Stop** it, which cancels the steps that were queued.

**Resume** picks a paused, stopped, or failed run back up from where it left off instead of starting over. It is available whenever a workflow's last run ended in a paused, stopped, or error state.

What "where it left off" means depends on how the workflow runs:

| Execution | On resume |
|---|---|
| Serial | Restarts at the step that was running when the run ended, and continues from there. |
| Parallel | Re-runs every step that had not yet finished successfully, and leaves completed steps alone. |
| Advanced (graph) | Re-runs the node that failed and everything still waiting on it, and leaves completed nodes alone. |

Steps that call another workflow — **Run Model**, **Conditional Run Model**, and **Loop Model** — resume the workflow they call rather than restarting it, through however many levels of nesting you have. A loop step resumes the iteration that was interrupted and skips the iterations that already completed.

A resumed run is recorded as a **new run** in the workflow's run history, containing only the steps it re-ran. The original run keeps its own history entry.

:::note
A loop step matches its completed iterations by their variable values. If the data the loop iterates over changed between the original run and the resume, iterations it can no longer match are re-run rather than skipped.
:::
