---
title: Optimize a Workflow
description: Make an Advanced workflow run faster by rebuilding its dependencies from data lineage and merging chains of extract steps, with every merge verified on your data before it is applied.
sidebar:
  order: 19.6
---

**Optimize** reviews an Advanced workflow and proposes changes that make it run faster. You see every change before anything happens, choose the ones you want, and can undo the result later.

Optimize works on Advanced (DAG) workflows. For a Standard workflow, choose **Convert to Advanced...** first; see [Advanced Workflows](/guides/workflows/advanced-workflows/#choose-the-workflow-type).

## Optimize a Workflow

1. In the **Workflows** list, right-click an Advanced workflow and choose **Optimize...**. The workflow must not be running or paused, and you need write access to it.
2. The **Optimize Workflow** window shows a headline such as *34 steps → 30 steps · 12 steps can run in parallel*. When the workflow has run history, it adds *~11 s faster per run*.
3. Below the headline is one row per change, each with a checkbox, the steps it touches, what it means for the workflow, and the time it saves. All are checked; clear the ones you don't want.
4. A **Can't optimize** list names the steps Optimize left alone and why.
5. Choose **Apply N changes**.

If the workflow has nothing left to improve, the window says so.

## The Two Kinds of Change

### Rebuild dependencies from data lineage

Optimize reads which tables each step reads and writes, and redraws the connections so a step waits only for the steps whose tables it uses. Steps that share no tables run in parallel.

- A step no longer waits for unrelated steps, so it no longer stops when an unrelated step fails. A failure cascades along the new dependencies.
- A partial run by step range, such as **Run From Here**, follows the new dependencies.
- The server still limits how many steps run at once.
- Optimize leaves this change out while a schedule or another workflow runs a range of this workflow's steps.

### Merge a chain of extract steps into one

A chain of Extract Data steps, each reading the table the one before wrote, becomes a single step that reads the first source and writes the last result.

Each merge is verified before it is applied. Optimize runs the original steps and the merged step on your current data into temporary scratch tables, and compares the two results row for row. It applies the merge only when they are identical. Your workflow and its tables aren't touched during verification.

- The tables in the middle of a merged chain are no longer written by the workflow. They are kept, not deleted, and the change names them.
- A merge whose results differ, or that can't be verified, is not applied, and the results say why. Merges need a source table with data; tables governed by row-level security, or too large to verify automatically, are listed under **Can't optimize**.

## Watch the Progress

After you apply, **Optimizing Workflow** shows the phase: *Verifying (3 of 6 runs)...*, *Comparing results...* and *Applying...*. When it finishes, the results list what was **Applied**, including how many rows each merge was verified on, and what was **Not applied**, with a reason for each.

If the workflow changed while Optimize was verifying, the affected changes are skipped and the window says how many. If an apply fails, the workflow is restored to how it was before.

A run that starts while the changes are being committed is delayed for a moment, not dropped.

## Undo an Optimization

Right-click the workflow and choose **Undo optimization...**, or use **Undo optimization** in the results. Confirm, and the workflow's steps, settings and layout return to how they were before the optimization. Changes you made to the workflow since are lost.

Undo needs restore points, which aren't available on every tenant. A tenant without them can't apply an optimization.

## Optimize Through the API and AI Assistants

Optimize is also available through the REST API and through the `workflow_optimize` tool for AI assistants, with the same preview, apply and undo steps.

## Next Steps

- [Advanced Workflows](/guides/workflows/advanced-workflows/) — the canvas, connections and run controls
- [Controlling Parallel Execution](/guides/workflows/controlling-parallel-execution/) — run steps at the same time
- [Run a workflow](/guides/workflows/run-a-workflow/) — running a workflow end to end
