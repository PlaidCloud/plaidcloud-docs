---
title: Run a workflow
description: Run a PlaidCloud workflow manually or on demand, follow each step's status, and pause, stop, or resume a run from where it left off.
sidebar:
  order: 6
---

You can trigger a full workflow run by either clicking on the run icon from the **Workflows** hierarchy or by selecting **Run All** from the **Actions** menu within a specific workflow.



You can also click on the **Toggle Start/Stop** button at the top of the workflow table. This toggle button will stop a running workflow or start a workflow.

If you click **Run** on a workflow that's already running, PlaidCloud tells you so instead of starting a second run.

## Choose a Posting Mode

Every run carries an ERP posting mode, chosen when you start the run through the run API or the assistant. Runs started from the workflow toolbar use the project's cap, described below. An in-client mode selector is follow-on work.

| Mode | What happens |
|---|---|
| Live | Posting steps post exactly as they always have. This is the default. |
| Simulate | Every ERP posting step builds and validates exactly what it would post, then commits nothing and never contacts the ERP. The would-post entries are recorded in [ERP Post History](/guides/connections/erp-post-history/), marked simulated, so you can review them before running live. |
| Off | Posting steps are skipped entirely. |

A project also carries its own posting mode cap, set through the project API or the assistant by any member with write access to an unlocked project. The cap only ever makes a run safer, never more permissive: a run's effective mode is the more restrictive of the mode you chose and the project's cap, so a project capped to Simulate stays simulated even if you start the run as Live.

The mode carries through everything the run touches. A sub-workflow, a macro, and a **Run Model**, **Conditional Run Model**, or **Loop Model** step all inherit the parent run's mode, and so does a run you [resume](#pause-stop-and-resume) after a stop — a simulated run can't post for real anywhere inside itself.

:::caution
SAP posting, SAP attachment, and generic SAP RFC steps don't dry-run. Under Simulate or Off they're skipped outright, because SAP's own test flags still open a real connection to SAP — skipping the step is the only way a simulated run never reaches SAP.
:::

:::note
An individual ERP posting step also carries its own Validate Only setting (labeled Preview or Test Only Mode on some steps), independent of the run's posting mode above. The step editor always saves this explicitly. A step configuration written another way — the REST API, MCP, or a workflow bundle import — that leaves the setting out entirely now also defaults to a preview rather than a live post.
:::

## Follow a Step's Status

While a workflow runs, each step carries a status icon showing where it stands, alongside how long it has been running. Hover the icon for the message behind it.

| Status | What it means |
|---|---|
| Waiting | The step is queued and hasn't started yet. |
| Running | The step is working, and its duration counts up as it goes. |
| Completed | The step finished successfully. |
| Warning | The step finished, but flagged something worth reading in the [workflow log](/guides/workflows/viewing-workflow-log/). |
| Error | The step failed. See [Managing Step Errors](/guides/workflows/managing-step-errors/). |
| Skipped | The step was passed over — it's disabled, or its run conditions weren't met. See [Skip Steps in a Workflow](/guides/workflows/skip-steps-in-a-workflow/). |
| Continued | The step failed but is set to continue on error, so the workflow carried on. See [Continue on Error](/guides/workflows/continue-on-error/). |
| Stopped | The run was stopped before the step could finish. |
| Abandoned | The step's execution was interrupted, so it will never finish. Resume the run, or re-run the workflow. |

An open workflow view refreshes on its own as a run progresses, so the statuses you're looking at stay current without reloading the page.

### Abandoned Steps

A step is marked **abandoned** when whatever was executing it went away mid-run — most often because someone pressed **Stop**, or because platform maintenance interrupted the run. The step's duration stops climbing and the status tooltip explains what happened.

An abandoned step did not complete and produced no output. It is not a slow step, and it is not a problem with your data or your configuration.

To pick the work back up, either [**Resume**](#pause-stop-and-resume) the run — the abandoned step runs again — or re-run the whole workflow. Both are safe.

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

When you Resume a workflow that ran as a **nested child** of another — one a **Run Model** step in a parent invoked — PlaidCloud offers **Resume from top of chain**. Resuming the child on its own cannot continue the parent's orchestration, so this option resumes the top-level parent instead — the root of the chain — and continues the whole chain from where it stopped. Resuming a top-level workflow is unchanged. The top of the chain is resolved within the same project: a chain that crosses into another project resumes from the top of the in-project portion.

Resume always continues the **original** run. It re-runs every step from that run that did not finish successfully — a step that failed or was abandoned is re-run, not treated as complete — and re-running an individual step on its own in the meantime does not change what Resume picks up next.

A resumed run is recorded as a **new run** in the workflow's run history, containing only the steps it re-ran. The original run keeps its own history entry.

:::note
A loop step matches its completed iterations by their variable values. If the data the loop iterates over changed between the original run and the resume, iterations it can no longer match are re-run rather than skipped.
:::
