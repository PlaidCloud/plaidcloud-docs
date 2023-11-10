---
title: Copy & Paste steps
slug: copy-paste-steps
weight: 4.0
description: Copy and paste steps within and across workflows
date: 2022-01-25T07:40:21
---


## Copy Steps


It is often useful to copy steps instead of starting from scratch each time. PlaidCloud allows copying steps within workflows as well as between workflows, and even in other projects. You can select multiple steps to copy at once. Select the workflow steps within the hierarchy and click the **Copy Selected Steps** button at the top of the table.



This will place the selected steps in the clipboard and allow pasting within the current workflow or another one.



Copying a step will make a duplicate step within the project. If you want to place the same step in more than one location in a workflow, use the **Add Step** menu option to add a reference to the same step rather than a clone of the original step.



## Paste Steps


After selecting steps to copy and placing them on the clipboard, you can paste those steps into the same workflow or another workflow, even in another project. There are two options when pasting the steps into the workflow:


* Append to the end of the workflow
* Insert after last selected row

The append option will simply append the steps to the end of the selected workflow. The insert option will insert the copied steps after the selected row. Note that if multiple steps have been copied to the clipboard from multiple areas in a workflow, that pasting them will paste them in order but will not have any nested hierarchy information from when they were copied. The pasting will be a flat list of steps to insert only. This might be unexpected but is safer than creating all of the directory structure in the target workflow that existed in the source workflow.

