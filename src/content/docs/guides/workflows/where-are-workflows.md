---
title: Where are the Workflows
description: Navigate to and manage PlaidCloud workflows within your projects using the workflow interface and project navigation tools.
sidebar:
  order: 1
---

Workflows live inside projects. To find them:

1. From the top menu, open **Projects**.
2. Click the project that contains the workflows you're looking for.
3. Switch to the **Workflows** tab.

You'll see every workflow in the project, organized in a folder-style hierarchy.

## What You'll See for Each Workflow

- **Status** — running, completed normally, or finished with a warning or error
- **Created** and **last updated** timestamps, plus the names of the people responsible
- **Folder organization** — workflows can be grouped in nested folders for easier management in large projects

Double-click a workflow to open the **Workflow Explorer**, where you can view steps, run the whole workflow, run a single step, or pick a range.

## Why a Workflow Might Not Be Visible

The workflows you can see depend on two things:

- **Project access** — your workspace administrator grants you access to specific projects. If you expect to see a project but don't, ask a project owner to add you.
- **Viewing role** — within a project you're assigned one of three roles:
  - **Architect** — can see and edit everything
  - **Manager** — can see and run workflows but not modify them
  - **Explorer** — limited visibility; some workflows may be hidden

If you expect to see specific workflows and don't, your role may be filtering them out. A project Architect can confirm what you should see.

Your role also decides whether you can change a step. If you can open a workflow but not modify it, the step form opens read-only — its fields are disabled and its **Save** button is hidden — so you can read a step's configuration without being able to alter it. This applies wherever the form opens: the workflow table's gear icon and right-click menu, the Visual Canvas, the project **Steps** grid, and the **New Step** menu.

## Unsaved Changes in a Step Window

A step window marks unsaved changes with a **•** in its title. Closing the window with **Esc**, the **X**, **Cancel**, or its tab button asks **Discard unsaved changes?** so an edit isn't lost by accident. Choose **Discard** to close without saving, or go back to keep editing.

## A Step Changed Since You Opened It

**Save** in a step form never writes over a change saved after you opened the form, whether Weave made it or someone else did. Nothing is saved: the form stays open with your edits, and a warning titled **Update failed** says *This step changed since you opened it. Reload to see the latest version; your unsaved edits will be lost.* Choose **Reload** to show the step as it is now, then make your edits again. Adding or removing one of the step's labels doesn't count as a change. If other saves keep landing on the step while yours is written, an **Update failed** message says *This step kept changing while it was being saved. Try again.* and nothing is saved; save again once they stop.

Through the REST API, `GET /rest/v1/analyze/projects/{project_id}/transform/{step_id}` returns the step with its `_etag`. Send it back as `if_match` on `PUT` to the same path, and a save over a newer change is refused with `412` and nothing is written. Without it, the last save wins. A `PUT` that other saves keep overtaking is refused with `503` and the same *This step kept changing while it was being saved. Try again.*, and nothing is written. When a `PUT` carries `labels` and only they couldn't be written, it answers `503` with *The step was saved, but its labels were not: they kept changing as they were written. Set the labels again.* AI assistants connected over MCP get the same check by passing the `_etag` from `step_describe` as `if_match` to `step_upsert`.

## Next Steps

- [Workflow explorer](/guides/workflows/workflow-explorer/) — what to do inside an open workflow
- [Create a workflow](/guides/workflows/create-workflow/) — start a new one
- [Run a workflow](/guides/workflows/run-a-workflow/) — execute end-to-end
