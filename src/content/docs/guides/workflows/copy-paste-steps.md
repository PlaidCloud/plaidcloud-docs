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

One clipboard serves every place you copy a step — the steps table, the older table you reach by holding Ctrl (or Cmd) as you open a workflow, and the Advanced workflow canvas — so you can copy in any of them and paste in any of them. Copy a few steps from a table and paste them onto an Advanced canvas, or the reverse; it is the same clipboard.



Copying a step makes a duplicate step within the project — a new step with its own configuration, independent of the original.

A step can appear at most once in any given workflow's structure. **Append** and **Insert** always paste in a fresh duplicate, so they never run into this. Pasting a *reference* to a step you already placed — see **Paste as a Linked Step** below — is different: it's the same step, so pasting it into a workflow that already contains it, including the workflow you copied it from, is refused with a message naming the step. Link it into a *different* workflow instead.



## Paste Steps


After selecting steps to copy and placing them on the clipboard, you can paste those steps into the same workflow or another workflow, even in another project. There are two options when pasting the steps into the workflow:


* Append to the end of the workflow
* Insert after last selected row

The append option will simply append the steps to the end of the selected workflow. The insert option will insert the copied steps after the selected row. Note that if multiple steps have been copied to the clipboard from multiple areas in a workflow, that pasting them will paste them in order but will not have any nested hierarchy information from when they were copied. The pasting will be a flat list of steps to insert only. This might be unexpected but is safer than creating all of the directory structure in the target workflow that existed in the source workflow.


## Paste as a Linked Step


**Paste → Add Linked Steps (Advanced)** places the *same* step in the target workflow rather than a copy of it. Both placements are the one step: edit it in either workflow and both change, because there is only one step to change.


A linked step can only be pasted into the project it was copied from. Linking is a second placement of a step that a project owns, so it has no meaning outside that project — paste into a different project and PlaidCloud declines and tells you to use **Append** or **Insert** instead, which copies the steps into the target project as steps of their own.

A linked step also can't be placed into a workflow that already contains it — that would be the same step twice in one workflow's structure, which PlaidCloud refuses. This is most likely to come up if a link operation seems to fail and you try it again: the first attempt actually went through, and the retry is refused rather than corrupting the workflow. The error names the step so you can confirm it's already there.


## Copy & Paste on the Advanced canvas


On an Advanced workflow you can copy and paste steps directly on the canvas with the keyboard, and the links between them come along.


Select the steps you want — drag a box around them, or click one and Shift- or Ctrl/Cmd-click to add more — and press **Ctrl/Cmd+C**. Move to the workflow you want them in, whether in this project or another, point at where they should go, and press **Ctrl/Cmd+V**. The steps are copied in, arranged the way they were, and left selected so you can drag them into place. The same actions are on the right-click menu as **Copy N Steps** and **Paste N Steps Here**.


**A group comes across as a group.** Click a group's header and the group and all of its steps are selected together; copy, and the group box and its members paste in as one. A box drawn around a whole group in the marquee selects it the same way.


**The links between the copied steps come with them; links to steps you didn't copy do not.** A step in your selection that was fed by a step you left behind arrives without that incoming link — there is nothing on the other end to connect to. The paste tells you when this has happened, so a dropped connection is never silent.


**Pasting into the same workflow** offsets the copies slightly so they don't land exactly on top of the originals. Pasting into a workflow that isn't Advanced — an ordinary steps table — drops the canvas arrangement and the links, and simply adds the steps; the paste tells you it has done so.


**A large paste is done in batches automatically.** Nothing is capped and nothing is silently dropped — a paste of hundreds of steps simply shows its progress as it works, and you can cancel it. If a paste can't finish, the steps it had already added are removed again so you are not left with a half-pasted workflow; in the rare case some of them can't be removed automatically, the message says so and names how many remain rather than claiming a clean rollback.


**To undo a paste,** press **Ctrl/Cmd+Z** right after it — the pasted steps are removed. Once a collaborator has changed the workflow, or you've reloaded it, that one-step undo steps aside rather than risk removing work that is no longer just yours.


Steps are copied as new steps of their own. Pasting the *same* step into more than one place — the linked-step behavior above — is a steps-table action; on the canvas, use **Add Step** to place a reference in a workflow that doesn't already contain that step.
