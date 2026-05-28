---
title: Macro Run
description: Invoke a Macro workflow as an isolated sub-invocation with declared input/output port bindings — each call runs in its own scratch schema.
sidebar:
  order: 3
---

## Description

Invokes a [Macro](/guides/workflows/create-a-macro/) workflow as a run-isolated sub-invocation. Unlike [Run Workflow](/reference/workflow-steps/workflow-control/run-workflow/), every Macro Run call:

- Gets a fresh, unique `run_id`.
- Runs in its own ephemeral scratch schema (`macrorun_<run_id>`) in the project's catalog.
- Binds caller-side tables and variables to the Macro's declared input ports at copy-in.
- Copies the Macro's declared output tables back to caller-side destinations on success.
- Always drops the scratch schema when the call finishes (success, error, or stop).

This isolation makes the same Macro safe to call concurrently — from a parent loop, from independent workflows running at the same time, or recursively from another Macro — without intermediate-table-name collisions between runs.

The target workflow must be flagged as a Macro. A Macro Run step that targets a non-Macro workflow fails with a clear error message; conversely, a [Run Workflow](/reference/workflow-steps/workflow-control/run-workflow/) or [Workflow Loop](/reference/workflow-steps/workflow-control/workflow-loop/) step cannot target a Macro (those steps don't carry the per-run isolation lifecycle).

## Macro to Run

- **Project** — the project containing the Macro. Must be the same project as the caller in v1.
- **Macro** — the Macro workflow to invoke. The Macro's declared input and output ports populate the binding lists below once selected.

## Input Port Bindings

For each input port declared on the Macro, add a binding. Bindings are processed in two passes — scalar / dimension inputs first (written to the Macro's run-scoped variable overlay), then table inputs — so a table-input filter can reference the scalar inputs.

**Table input ports:**

- **Source** — a caller-side table (by name or id) whose contents are copied into the Macro's scratch schema under the port name.
- **Columns** — optional column projection. Pick a subset and rename if needed (`source` → `target`); the columns are quoted and applied at copy-in, so only the projected columns are materialized.
- **Filter** — optional `WHERE` clause applied at copy-in. May reference the Macro's input variables by name (resolved from the scalar bindings above). For example, `month = {month}` restricts copy-in to one month's slice of a multi-year table.

**Scalar / Dimension input ports:**

- **Variable** — the Macro-side variable name to set (matches a port declared on the Macro).
- **Value** — the value to bind, either a literal or a caller-side variable reference (resolved against the caller's variables before being written to the sub-invocation's overlay).

## Output Port Bindings

For each output port declared on the Macro, add a binding pointing at a caller-side destination table. The destination is created on the fly if it doesn't already exist. Output copy-out:

- Happens after the Macro completes successfully (state `done` or `warn`).
- Is **skipped** if the Macro is stopped manually mid-flight (`stop` state) — partial outputs would otherwise silently land in the caller's durable schema.
- Optional **columns** projection works the same way as on input bindings.

## Behavior on Failure

| Macro outcome           | Caller-side effect                                                    |
|-------------------------|-----------------------------------------------------------------------|
| `done` / `warn`         | Output tables copied to caller destinations; scratch schema dropped. |
| `stop` (manual stop)    | Copy-out skipped; scratch schema dropped; caller warning logged.      |
| Error mid-run           | Macro Run step errors; scratch schema dropped; outputs not written.   |

The scratch schema is always reclaimed in a `finally` block, so a failed or stopped Macro never leaks intermediate tables into the project schema.

## Examples

No examples yet…

## Related

- [Create a Macro](/guides/workflows/create-a-macro/) — declare a workflow as a Macro and define its port contract.
- [Run Workflow](/reference/workflow-steps/workflow-control/run-workflow/) — the non-isolated sub-workflow caller (cannot target a Macro).
