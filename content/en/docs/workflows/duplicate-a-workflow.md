---
title: Duplicate or Clone a Workflow
slug: duplicate-a-workflow
weight: 3.0
description: Duplicate or clone PlaidCloud workflows — including across projects — with a configurable name prefix and suffix.
date: 2022-01-25T07:40:20
---


Copying a workflow is useful when planning major changes or replicating a process with different options. Cloned workflows are completely separate from the original and can be modified without impacting it.

Two actions are available from the **Actions** menu of the **Workflows** table:

* **Duplicate Selected Workflows** — fast in-place copy that appends *Copy* to the name.
* **Clone Workflow(s)** — full clone with a configurable name prefix/suffix and an optional target project.


## Duplicate Selected Workflows

1. Open the project's **Workflows** table
2. Select one or more workflows
3. Click `Duplicate Selected Workflows` in the toolbar

The clones land in the same project. Each name has *Copy* appended.


## Clone Workflow(s)

Use this when you want control over the new names or want to clone into a different project.

1. Open the project's **Workflows** table
2. Select one or more workflows
3. Open the **Actions** menu and click `Clone Workflow(s)`
4. In the dialog, optionally set:
    * **Prefix** — text prepended to each new workflow name
    * **Suffix** — text appended to each new workflow name
    * **Target Project** — destination project (defaults to the current project)
5. Click `Clone`

If you leave both prefix and suffix blank and clone into the same project, the dialog appends *Copy* to avoid name collisions.

{{< note >}}
Cloning across projects copies the workflow definition and step configuration. Project-scoped resources referenced by the workflow (tables, dimensions, connections) must already exist in the target project, or you must clone them separately.
{{< /note >}}

