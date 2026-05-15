---
title: Allocations Quick Start
description: Quickly set up a basic cost allocation in PlaidCloud with this step-by-step guide covering sources, drivers, and target mapping.
sidebar:
  order: 1
---

This walkthrough takes you from raw cost data to a working allocation model in roughly 30 minutes.

## What You'll Need

- A project with at least two tables:
  - **Values to allocate** — the costs (or revenues, or volumes) you want to spread. One row per source unit, one column with the amount.
  - **Driver data** — the basis for spreading. Headcount, square footage, transaction counts, revenue — whatever you want to allocate *by*.
- A dimension that ties source and target together (cost centers, departments, products — whichever taxonomy fits your model).

If you don't have all of that yet, the [Tables and views](/guides/data/) and [Dimensions](/guides/dimensions/) guides cover loading the inputs.

## Steps

1. **Open the project** that holds your values and driver tables.
2. **Create a new workflow.** Allocations always run inside a workflow — they don't operate on tables directly outside of one.
3. **Add an Allocation step.** Inside the workflow, add a step from the **Allocation** category. The most common starting point is **Allocation Rules** for straightforward driver-based spreading.
4. **Configure the source.** Point the step at your values table and pick the column holding the amount to allocate.
5. **Configure the driver.** Point the step at the driver table and pick the column holding the driver values.
6. **Map the dimension.** Identify which column on each table represents the dimension members. The allocation step uses these to match source rows to driver rows.
7. **Run the step.** The output is a new table with one row per spread amount.
8. **Inspect results.** Check that the totals match what you expected — sum of allocated amounts should equal sum of source amounts (within rounding tolerance).

## Common Follow-Ups

- **Spreading recursively** — if a target itself contains drivers for further allocation, see [Recursive allocations](/guides/allocations/setup/recursive-allocations/).
- **Tagging rows for allocation** — to drive *which* rows allocate to which targets, see [Rule-based tagging](/guides/allocations/getting-started/rule-based-tagging/).
- **Investigating unexpected results** — if totals don't reconcile or specific rows look wrong, see [Troubleshooting allocations](/guides/allocations/results/troubleshooting-allocations/).

## Next Steps

- [Why are allocations useful?](/guides/allocations/getting-started/why-are-allocations-useful/) — when to use them
- [Configure an allocation](/guides/allocations/setup/configure-an-allocation/) — deeper configuration reference
- [Allocation step types](/reference/workflow-steps/allocation/) — every workflow step in the Allocation category
