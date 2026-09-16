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

Every driver row must resolve to a different destination table, so include a driver column in the destination name — `results_{region}`, for example. Copy-out replaces the destination rather than appending to it, so two rows resolving to the same destination would leave only the second row's result; the step refuses that configuration before it launches anything. To combine the results into one table, add a step downstream that unions the per-row tables.

Copy-out is skipped for a stopped child invocation so partial results are not written into durable caller tables.

## When a Child Invocation Stops Responding

A child invocation reports its own result when it finishes, so a child whose machine stops without warning never reports anything at all. Rather than wait on it indefinitely, the step checks that each child it is still waiting on is alive.

- A child that has started is checked roughly once a minute, and only while it shows no sign of progress. A child working through a single long-running step shows no progress for as long as that step takes, and is left alone for as long as it is genuinely still running.
- A child that was accepted but has not started within 15 minutes is treated as never having started. That window covers scheduling and image pull, not the Macro's own work.

A child treated either way is stopped, its scratch schema is dropped, and the step fails at the end naming that invocation, the last state it reported, and when it last reported it.

**The other child invocations are unaffected.** They run to completion and their output tables are written as normal, so one unresponsive child out of many does not discard the rest. Only the invocations that could not complete are named in the failure.

If the check itself cannot be answered — while the platform is briefly unreachable, for instance — the child is treated as still running and checked again on the next pass.

## Stop Behavior

Stopping the parent Macro Concurrent step stops every active child Macro invocation and drops each active run schema. Children that have not started are not launched after the parent is stopped.

## Related

- [Create a Macro](/guides/workflows/create-a-macro/) — declare a workflow as a Macro and define its port contract.
- [Macro Run](/reference/workflow-steps/workflow-control/run-macro/) — invoke one Macro once.
