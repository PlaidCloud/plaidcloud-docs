---
title: Macro Concurrent
description: Run one isolated Macro invocation per driver-table row, with a configurable concurrency limit.
sidebar:
  order: 4
---

## Description

Runs a [Macro](/guides/workflows/create-a-macro/) once for each selected row in a caller-side driver table. Each child invocation behaves like a [Macro Run](/reference/workflow-steps/workflow-control/run-macro/) step:

- It gets a fresh `run_id`.
- It runs in its own scratch schema (`macrorun_<run_id>`).
- It receives table, scalar, and dimension bindings from the caller.
- It copies declared output tables back to caller-side destinations when the child finishes with `done` or `warn`.
- It drops the scratch schema when the child finishes, fails, or is stopped.

Use Macro Concurrent when the same reusable process should run for many rows, such as one period, entity, customer, file batch, or region per driver-table row.

## Driver

- **Table** — the caller-side table that contains one row per Macro invocation.
- **Concurrent Runs** — the maximum number of child Macro invocations to keep active at once.

## Table Data Selection

Select the driver-table columns that each child invocation needs. These columns can be used by the Macro bindings and by the driver filter.

## Driver Filter

Optionally add filter rules for the driver table. Only matching rows launch child Macro invocations.

## Macro

- **Project** — the project containing the Macro. Must be the same project as the caller in v1.
- **Macro** — the Macro workflow to invoke for each selected driver row.

## Input Bindings

Input bindings connect caller-side data to the Macro's declared inputs.

**Table input bindings:**

- **Caller Source Table** — the table copied into the child invocation's scratch schema.
- **Macro Target Port** — the Macro input table name or port to receive the copied table.
- **Copy-In Filter** — optional `WHERE` clause applied during copy-in.
- **Columns JSON** — optional JSON column projection, when only selected columns should be copied.

**Scalar and dimension input bindings:**

- **Macro Variable** — the Macro-side variable to set for the child invocation.
- **Value** — the literal value, caller variable reference, or driver-column value to bind.

Scalar and dimension inputs are set before table copy-in, so table filters can reference those variables.

## Output Bindings

Output bindings copy Macro result tables back to caller-side destinations.

- **Macro Source Port** — the Macro output table name or port to copy from.
- **Caller Destination Table** — the caller-side table to copy into.
- **Columns JSON** — optional JSON column projection for copy-out.

Copy-out is skipped for a stopped child invocation so partial results are not written into durable caller tables.

## Stop Behavior

Stopping the parent Macro Concurrent step stops every active child Macro invocation and drops each active run schema. Children that have not started are not launched after the parent is stopped.

## Related

- [Create a Macro](/guides/workflows/create-a-macro/) — declare a workflow as a Macro and define its port contract.
- [Macro Run](/reference/workflow-steps/workflow-control/run-macro/) — invoke one Macro once.
