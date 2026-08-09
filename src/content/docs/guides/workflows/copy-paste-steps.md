---
title: "Copy & Paste steps"
description: Copy and paste workflow steps between PlaidCloud workflows to reuse step configurations and speed up workflow development.
sidebar:
  order: 4
---

## Copy Steps


It is often useful to copy steps instead of starting from scratch each time. PlaidCloud allows copying steps within workflows as well as between workflows, and even in other projects. You can select multiple steps to copy at once. Select the workflow steps within the hierarchy and click the **Copy Selected Steps** button at the top of the table.



This will place the selected steps in the clipboard and allow pasting within the current workflow or another one.

The clipboard is held in your browser, so it survives reloading the page and is shared by every PlaidCloud tab you have open. Copy from a project in one tab, switch to a project in another, and paste there. It is not shared between different browsers, between browsers on different machines, or with anyone else, and switching workspace clears it.

One clipboard serves both versions of the workflow steps screen — the current one and the older one you reach by holding Ctrl (or Cmd) as you open a workflow — so you can copy in either and paste in either.



Copying a step will make a duplicate step within the project. If you want to place the same step in more than one location in a workflow, use the **Add Step** menu option to add a reference to the same step rather than a clone of the original step.



## Paste Steps


After selecting steps to copy and placing them on the clipboard, you can paste those steps into the same workflow or another workflow, even in another project. There are two options when pasting the steps into the workflow:


* Append to the end of the workflow
* Insert after last selected row

The append option will simply append the steps to the end of the selected workflow. The insert option will insert the copied steps after the selected row. Note that if multiple steps have been copied to the clipboard from multiple areas in a workflow, that pasting them will paste them in order but will not have any nested hierarchy information from when they were copied. The pasting will be a flat list of steps to insert only. This might be unexpected but is safer than creating all of the directory structure in the target workflow that existed in the source workflow.


## Paste as a Linked Step


**Paste → Add Linked Steps (Advanced)** places the *same* step in the target workflow rather than a copy of it. Both placements are the one step: edit it in either workflow and both change, because there is only one step to change.


A linked step can only be pasted into the project it was copied from. Linking is a second placement of a step that a project owns, so it has no meaning outside that project — paste into a different project and PlaidCloud declines and tells you to use **Append** or **Insert** instead, which copies the steps into the target project as steps of their own.
