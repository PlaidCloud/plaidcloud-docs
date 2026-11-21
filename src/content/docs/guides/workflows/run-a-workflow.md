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

Every run carries an ERP posting mode. To choose one in PlaidCloud, use **Run With Posting Mode** in a workflow's right-click menu, or the run-mode button on the workflow canvas; a plain **Start Workflow** or **Run Workflow** asks for Live, still subject to the project's cap described below. You can also choose the mode when you start a run through the run API or the assistant.

| Mode | What happens |
|---|---|
| Live | Posting steps post exactly as they always have. This is the default. |
| Simulate | Every ERP posting step builds and validates exactly what it would post, then commits nothing and never contacts the ERP. The would-post entries are recorded so you can review them before running live: a **Post Documents** step's in the [Posting Register](/guides/connections/posting-register/) as **Would post** (see [Post Documents to ERP Systems](/guides/connections/post-documents/)), a system's own posting step's in [ERP Post History](/guides/connections/erp-post-history/), marked simulated. |
| Off | Posting steps are skipped entirely. |

A project also carries its own posting mode cap, set through the project API or the assistant by any member with write access to an unlocked project. The cap only ever makes a run safer, never more permissive: a run's effective mode is the more restrictive of the mode you chose and the project's cap, so a project capped to Simulate stays simulated even if you start the run as Live.

A [scheduled event](/administration/scheduled-events/event-scheduler/#erp-posting-mode) keeps its own posting mode, so a schedule set to Simulate runs simulated every time it fires.

The mode carries through everything the run touches. A sub-workflow, a macro, and a **Run Model**, **Conditional Run Model**, or **Loop Model** step all inherit the parent run's mode, and so does a run you [resume](#pause-stop-and-resume) after a stop — a simulated run can't post for real anywhere inside itself.

:::caution
SAP posting, SAP attachment, and generic SAP RFC steps don't dry-run. Under Simulate or Off they're skipped outright, because SAP's own test flags still open a real connection to SAP — skipping the step is the only way a simulated run never reaches SAP.
:::

:::note
An individual ERP posting step also carries its own Validate Only setting (labeled Preview or Test Only Mode on some steps), independent of the run's posting mode above. The step editor always saves this explicitly. A step configuration written another way — the REST API, MCP, or a workflow bundle import — that leaves the setting out entirely now also defaults to a preview rather than a live post. The **Post Documents** step has no such setting: the run's mode and its system's own mode decide whether it posts — see [Post Documents to ERP Systems](/guides/connections/post-documents/).
:::

## Authorize the Project to Post

A workflow run posts to an ERP as the project, not as the person who started it. Before a run can post, the project needs an authorization for each ERP connection and environment its posting steps use. Without one, the step fails with "This project isn't authorized to post to connection …", naming the connection and environment. The **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** and **Call SAP RFC** steps don't need one.

To authorize a project, open its home page and select **ERP Write Authorizations** under **ERP Posting**. Each row is one connection in one environment. Tick **Authorized** to let the project post there, or clear it to stop. **Authorized By** and **Authorized At** show who last authorized it and when.

- The button is shown to the project's Architects and to workspace admins, but only an Architect can change an authorization, and only while the project is unlocked. A workspace admin who isn't an Architect can add themselves as one first.
- Selecting a row to authorize or clear it doesn't reload the list: the scroll position and any column sort you chose stay where they are. The window can be resized, and the note about public projects wraps in full.
- To authorize a connection, you also need write access to it yourself: you own it, or it is shared with you by name or through one of your security groups. A connection set to **All Workspace Members** doesn't count.
- A project set to **All Workspace Members** is authorized like any other. Every member is an Architect of it, so any member with write access to a connection can authorize the project for it. Once it's authorized, any member can post to that connection from the project's workflows, and the window says so above the grid.
- A new copy that is private to you, made with table data or dimension members, keeps the source's authorizations that you could grant yourself, and arrives in Simulate if the source was Live — see [ERP Write Authorizations in the Copy](/guides/projects/managing-projects/#erp-write-authorizations-in-the-copy). Any other copy, or a project created from a project archive, starts with no authorizations. Authorize it before it posts.

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

### Interrupted Steps

If the server running a step is lost mid-run, PlaidCloud re-runs the step automatically when it is safe to repeat: a step that replaces its output ends up with the same result as a single clean run, so you have nothing to check. The step's log shows a warning where the second attempt starts: "Restarted: the server running this step stopped before it finished (e.g. out of memory or a restart); running it again from the start."

A step that can't be repeated safely isn't re-run. It fails once with an **interrupted** message, because running it a second time could duplicate what the first attempt already wrote. Steps that write outputs with `{date}` or `{date_iso}` in the name or path count as not safe to repeat, since a re-run could land on a different date. To recover, check the step's target for what the first attempt wrote, clean it up if needed, then [re-run the step](/guides/workflows/running-one-step-in-a-workflow/) or **Resume** the run.

### Steps That Never Start

While a step waits for a worker, its status message reads "Waiting for a worker… N min. No import worker has picked this step up yet." (the kind of worker matches the step, such as import or export). The message clears once the work starts.

If a step's job can never start, the step fails with the reason instead of waiting forever:

| Cause | Fails after about |
|---|---|
| No worker picks up an import or dimension step's job | 40 minutes |
| The step's pod is stuck Pending | 20 minutes |
| The step's image can't be pulled | 5 minutes |
| No pod is created for the step | 20 minutes |
| No runner picks up a connector (Singer) sync | 30 minutes |

The connector sync message names the sync. If a worker started the job and then went away, the step also fails, with a message saying the worker stopped. The import and dimension messages say "Use Run from here to retry."

### Runs That Stop Responding

A run never stays **Running** after the work behind it has gone. If the server running the workflow is lost, the run ends as failed. A run can last at most 12 hours: one still running at that point fails with "Run failed: still running at the 12-hour limit. Re-run the workflow."

## Run Insight

Run Insight shows where one run of a workflow spent its time, and which steps took longer or less time than they usually do. It judges each step against that step's own recent runs, so a step that is always slow isn't singled out.

### Open Run Insight

- On the canvas, click **History** in the toolbar. See [Visual Workflow Designer](/guides/workflows/advanced-workflows/).
- On the **Workflows** tab, select one workflow and choose **Run insight** from the **Actions** menu or the right-click menu.
- On Home, choose **Open latest run** on a workflow card.
- In the run history dialog, pick a run in the **Runs** table with **Open in Insight**, or open its row.
- In an in-app Weave message about a slow run, click **Open the run**. See [Being told when a run ends](/guides/ai-assistant/weave-findings/#being-told-when-a-run-ends).

The dialog is titled **Run History** followed by the workflow's name. Its **Insight** and **Runs** buttons switch between this view and the table of past runs. A step's own run history, opened from the Inspector, shows only the table.

### Read the Headline and the Attention List

The headline gives the run's outcome in one line: **Took** *time*, **Running for** *time* while it runs, **Stopped after** *time* for a latest run that was stopped, or **Failed in** the workflow where it failed. A sentence under it says what stands out, such as the steps that ran slower than usual, time spent waiting, or that every step with history ran within its usual range. Below that come the start time and the number of workflows and steps, and, when some steps have too little history to judge, how many. When anything needs a look, a count marked **to look at** appears beside the headline.

A strip of recent runs sits beside the headline. Click a run in the strip to open it. A failed run is marked, and so is a run that ran fewer steps than most recent runs, because it can't be compared with a full run.

**What needs attention** lists, in this order, failures first, then time beyond the usual, then waiting. Click an item to select it in the view.

### Flow, Timeline, and Table

Choose a view from the **View** menu.

| View | What it shows |
|---|---|
| **Flow** | Blocks whose height is time. Amber is time beyond a step's usual. Where a step called other workflows, a **Call overhead** slice is the step's own time outside those workflows. Where no step was running, a **Waiting** slice shows the gap; a workflow that ran in parallel doesn't draw one. |
| **Timeline** | Clock time from the start of the run. A dashed outline is how long the block took in the compared run. |
| **Table** | Everything in call order, with the columns **Name**, **This run**, **Usually**, **Extra**, **Compared run** and **Status**. |

A workflow that called other workflows shows them inside it. Double-click a workflow block, or choose **Zoom in**, to work inside it, and use the trail above the view or **Zoom out** in the **Actions** menu to come back. When several on-pace steps sit together, **Flow** folds them into one **N on pace** block; click it, or choose **Show all blocks** in the **Actions** menu, to open them. **Fold on-pace blocks** folds them again.

Select a block to see its detail panel, with whichever of **This run**, **Usually**, **History**, **Beyond the usual** and **Compared run** apply, and with **Show in its workflow**, **Show its steps** or **Zoom in**, **Open workflow** and **View run log**. **Open workflow** opens the workflow on the canvas and **View run log** opens its [log](/guides/workflows/viewing-workflow-log/).

### What the Marks Mean

| Mark | Meaning |
|---|---|
| **Failed** | A step ended in an error. The panel shows its message, unless your role can't see the step's name. |
| **Slower than usual** | The step took longer than its usual range. |
| **Slower throughout** | Every step in the workflow ran about the same amount slower, which points at something the whole workflow shares rather than at one step. Its steps show **Part of a shared slowdown**. |
| **Has slow steps** | A workflow with **Slow steps inside** it. |
| **On pace** | The step ran within its usual range. |
| **Faster** | The step ran faster than its usual range. |
| **Not enough history** | The step hasn't run often enough to have a usual range, so it isn't judged. |
| **Error, continued** | The step failed but is set to [continue on error](/guides/workflows/continue-on-error/). |
| **Skipped** | The step was passed over. |
| **Running** | The step hasn't finished. |

A step whose recent runs were already slow or vary a lot may not be flagged. A run at period end, compared with ordinary days, can show as slower throughout. An older stopped run shows as a short run, not as stopped.

The panel can also explain a mark. **Waiting** is time when no step was running, so no step is to blame for it. On a step that ran slower than usual, **Rows written** compares its output with its usual count, and is left out when row-level security filters what you can read, and **Saved since its last run** says the step was saved after its previous run and before this one started; the record shows a save, not what changed. **Different work** counts the steps that didn't run and the steps that ran with none, measured against each step's history or, when you compare with another run, against that run. **Ran in parallel** means the parts of the workflow ran at the same time, so their times add up to more than the clock. **Caller not certain** means the history can't show which step called a workflow. **Name hidden** marks a step or workflow whose name your role can't see, shown as **Hidden step** or **Hidden workflow**.

### Compare To

**Compare to** sets what a run is measured against, and its button reads **Compare to: Usual**, **Compare to: Previous run** or **Compare to: Chosen run**. **Usual** uses each step's recent runs. **Usual + previous run** and **Usual + a chosen run** also add that run's time for each step, which the **Timeline** outlines and the **Table** shows under **Compared run**. The chosen run is picked from the recent runs.

### One Workflow Inside a Larger Run

When you open a workflow that another workflow called, Insight shows only that workflow's part of the run. **Open the whole run** switches the same dialog to the workflow that started the run.

### Live Runs

A run that is still going is read again every 30 seconds while the dialog is visible. Your zoom, selection and view stay as they are. Leaving Insight for **Runs** stops the updates, and returning to Insight reads the run again and resumes. The Refresh button, the circular arrows at the right of the toolbar, reloads the run from scratch, resets the zoom and selection, and folds on-pace blocks again.

### For AI Assistants and the REST API

The same profile is available outside the dialog:

- REST: `GET /rest/v1/analyze/workflow/run-insight` with `project_id` and `workflow_id`. `run_id` picks the run (the latest when left out), and `baseline` is `typical`, `previous` or `run:<id>`.
- MCP: `workflow_describe` with `include=['run_insight']`, and optional `run_id` and `baseline`.

Each workflow and step comes back with its time, its place in the run, a verdict against its own history, and the reasons. A run that doesn't exist, or has no step rows, returns no profile and a warning instead of an error.

## Pause, Stop, and Resume

While a workflow is running you can **Pause** it, so that in-flight steps finish and new steps wait, or **Stop** it, which cancels the steps that were queued and any import or export jobs that are still running, along with the warehouse query an export was reading. Import and dimension steps that were still queued are cancelled cleanly, so they don't hold up later imports and dimension loads in the workspace. Stop also stops the workflow's queued or running connector (Singer) syncs, so a sync doesn't keep running after the workflow has stopped.

A macro can be running in several places at once, called by other workflows or by a **Macro: Concurrent Run** step. Stopping the macro stops every running copy of it. Stopping one copy stops only that copy and what it started, and leaves the workflow that called it running, as does a **Macro Concurrent** step that gives up on a copy that stopped responding. A macro that's running only inside other workflows shows as **Running** in the workflow list, with **Stop** available, and opening it shows each step's status, start and end time from its latest run.

**Resume** picks a paused, stopped, or failed run back up from where it left off instead of starting over. It is available whenever a workflow's last run ended in a paused, stopped, or error state.

What "where it left off" means depends on how the workflow runs:

| Execution | On resume |
|---|---|
| Serial | Restarts at the step that was running when the run ended, and continues from there. If that step is inside a group, Resume picks up the whole top-level group holding it: steps in the group that already finished successfully are left alone, the others run, and the run continues after the group. |
| Parallel | Re-runs every step that had not yet finished successfully, and leaves completed steps alone. |
| Advanced (graph) | Re-runs the node that failed and everything still waiting on it, and leaves completed nodes alone. |

Steps that call another workflow — **Run Model**, **Conditional Run Model**, and **Loop Model** — resume the workflow they call rather than restarting it, through however many levels of nesting you have. A loop step resumes the iteration that was interrupted and skips the iterations that already completed.

When you Resume a workflow that ran as a **nested child** of another — one a **Run Model** step in a parent invoked — PlaidCloud offers **Resume from top of chain**. Resuming the child on its own cannot continue the parent's orchestration, so this option resumes the top-level parent instead — the root of the chain — and continues the whole chain from where it stopped. Resuming a top-level workflow is unchanged. The top of the chain is resolved within the same project: a chain that crosses into another project resumes from the top of the in-project portion.

Resume always continues the **original** run. It re-runs every step from that run that did not finish successfully — a step that failed or was abandoned is re-run, not treated as complete — and re-running an individual step on its own in the meantime does not change what Resume picks up next. That holds for a child workflow too: if you re-ran one of its steps on its own, resuming the parent still runs everything the child had left, not just that step.

A resumed run is recorded as a **new run** in the workflow's run history, containing only the steps it re-ran. The original run keeps its own history entry. When one run calls the same child workflow more than once, each call has its own entry in the child's run history. The iterations of a loop step count as one call.

:::note
A loop step matches its completed iterations by their variable values. If the data the loop iterates over changed between the original run and the resume, iterations it can no longer match are re-run rather than skipped.
:::
