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

Your role also decides whether you can change a step. If you can open a workflow but not modify it, the step form opens read-only — its fields are disabled and its **Save** button is hidden — so you can read a step's configuration without being able to alter it. This applies wherever the form opens: the workflow table's edit (pencil) icon, the Visual Canvas, the project **Steps** grid, and the **New Step** menu.

## Next Steps

- [Workflow explorer](/guides/workflows/workflow-explorer/) — what to do inside an open workflow
- [Create a workflow](/guides/workflows/create-workflow/) — start a new one
- [Run a workflow](/guides/workflows/run-a-workflow/) — execute end-to-end
