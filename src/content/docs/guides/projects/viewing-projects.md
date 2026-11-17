---
title: Viewing Projects
description: View and browse authorized PlaidCloud projects including project details, status, membership, and associated data resources.
sidebar:
  order: 1
---

## Description


Within **Analyze**, the Projects function provides a level of compartmentalization that makes controlling access and modifying privileges much easier. Projects are what provide the primary segregation of data within a workspace tab.



While Projects fall under Analyze, workflows fall under Projects, meaning that Projects contain workflows. Workflows, simply put, perform a wide range of tasks including data transformation pipelines, data analysis, and even ETL processes. More information on workflows can be found under the “Workflows” section.



## Accessing Projects


**To access Projects:**


1. Open Analyze
2. Select “Projects” from the top menu bar

This displays the Projects Hierarchy. From here, you will see a hierarchy of projects for which you have access. There may be additional projects within the workspace, but, if you are not an owner or assigned to the project, they will not be visible to you.


## The Activity Panel

The **Activity** panel on the right of the Projects window shows what ran in your projects, whether it worked, and who changed what. It lists the activity of every project you have access to, newest first, under a header for each day. It checks for new activity about every 15 seconds while the Projects window is the active window and your browser tab is visible.

Each day's header reads **Today**, **Yesterday** or the date, with a summary of that day's rows, such as "12 runs · 1 failed · 3 changes". The header of the day you are scrolling through stays at the top of the list.

### Runs

A workflow run has one row. An icon shows how it went, and hovering over the icon names the state: Succeeded, Failed, Warning, Stopped or Started. Rows with a failure or warning also have a colored bar along their left edge.

- **The first line** names the workflow and the time: "now", minutes or hours ago for today, or the clock time on an earlier day. Hover over the time to see the full date.
- **The second line** says who ran it and in which project, such as "mike ran · CFO Services", "Scheduled run · CFO Services" or "Sensor run · CFO Services". On the right is how long the run took, or **Failed** or **Stopped** with its duration. A stopped run names whoever stopped it.
- **A third line**, when there is one, shows what went wrong. When a step failed or warned during the run, it shows the step's name and its message, with "+2 more" when other steps had issues too. Click that line to open the workflow at that step.

While a run is in progress, it is listed under [Running Now](#running-now). Once it ends, its row shows the outcome. A workflow run by another workflow, through a Workflow: Run step or as a macro, has no row of its own, and a step issue inside it shows on the row of the run that called it. A step issue whose run isn't in the list has a row of its own, such as "Step failed · CRM Pipeline · CFO Services".

Changes, such as to workflows, steps, tables, dimensions and projects, have a row each, such as "mike modified step · CFO Services" under the step's name.

Most rows open what they name when you click them or press Enter on them. A run, or a workflow that was created, modified, imported or exported, opens its project on the **Workflows** tab with the workflow selected. A step issue, or a step that was created, modified, deleted, copied or moved, opens the workflow at that step. A table that was created, renamed, published or unpublished opens in Table Explorer, a dimension that was created or modified opens for editing, and a project that was created, modified, imported, exported or backed up, or whose security changed, opens the project.

### Repeated Rows

Back-to-back edits of the same kind by the same person to the same object collapse into one row, and so do back-to-back successful runs of the same workflow, started the same way by the same person or schedule. Click **3 edits** or **4 runs** on the row to see each of them, and click it again to fold them away.

### Running Now

Workflows that are running now are listed under **Running now**, above the list, with who started them and how long they have been running. A paused run says **Paused**. Click a workflow's name to select it in its project's **Workflows** list, or click **Stop** to stop that run.

### Hover Actions

Hover over a run's row, or move to it with the keyboard, to show two icon buttons, whose tooltips read **Open log** and **Run workflow**:

- **Open log** opens the project's log, filtered to that workflow. A step issue's row has this button too.
- **Run workflow** runs the workflow again.

**Stop** and **Run workflow** are allowed for the same members as stopping and running the workflow from its own screens. **Run workflow** runs the whole workflow with its default settings, even when the run on the row was a single step, a range of steps, or a simulation.

### Issues and Filters

When the loaded activity has runs or steps that failed or warned, the panel's header shows a count such as **2 issues**, marked as an error when any of them failed. Click it to show only those rows.

The strip at the bottom of the panel chooses what the list shows:

| Choice | Shows |
|---|---|
| **All** | Everything |
| **Runs** | Workflow runs |
| **Changes** | Changes to workflows, steps, tables, dimensions, projects and more |
| **Issues** | Runs and steps that failed or warned |
| **Mine** | Your own runs and changes |

Type in **Filter** to show only the rows whose workflow, project, step, table, dimension or member name contains your text. The strip ends with how many events match, such as **12 events**. The panel remembers which choice you made, in this browser.

### New Since Your Last Visit

A **New since your last visit** line separates what arrived since your previous visit from what you had already seen. It shows when **All** is chosen and nothing is typed in **Filter**. A visit ends when you switch to another window or close the Projects window, and the line moves the next time you open the Projects window or reload the page.

### Show Earlier

The list starts with the last 7 days. Click **Show earlier** at the end of the list to load up to 500 more events from the 30 days before the oldest one loaded, and click it again to go further back. It disappears once a 30-day stretch has no activity.

### Keyboard

Press Tab to move to a row, then use the Up and Down arrow keys to move between rows and Enter to open the one you are on. Tab also moves to the row's hover actions.

### Limits

- **Your last visit is remembered per browser.** On another browser or device, the **New since your last visit** line reflects your last visit there.
- **Counts describe the activity loaded in the panel.** The issue count, **Issues** and the day summaries cover the newest 500 events of the last 7 days at first, and more as you use **Show earlier**. They aren't totals for your projects.
- **A queued run shows as Started**, and appears under **Running now** once it actually starts. Its duration counts from when it was queued.
- **Step issues from a macro inside a macro** don't show on the top-level run's row.
- **A workflow that runs often** has many rows. Successful runs next to each other collapse, but those of two workflows that run in turns don't.
- **Runs from before this panel was released** show as Started, without an outcome, and stops from before then don't appear.
- **An event recorded late**, after newer ones have already appeared, shows once you reload the page.
- **A Projects window left open and unused for more than 30 days** picks up from 30 days back.
- **With no activity in the last 7 days**, the panel says "No activity in the last 7 days." and **Show earlier** doesn't appear, so earlier activity can't be loaded.
