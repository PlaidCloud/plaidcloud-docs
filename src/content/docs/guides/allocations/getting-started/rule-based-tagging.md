---
title: Rule Based Tagging
description: Configure rule-based tagging in PlaidCloud allocations to automatically categorize and label data records using defined criteria.
sidebar:
  order: 2
---

Rule-based tagging lets you mark source rows with metadata that the allocation engine uses to decide *where* those rows go. Use it when you need allocation behavior to vary by row — for example, when costs for one cost center should be spread by headcount but costs for another should be spread by revenue.

## When to Use It

- A flat allocation rule doesn't capture how cost should actually be spread (different rules for different cost types).
- You want to direct certain source rows to specific targets while leaving others to spread normally.
- You're modeling a multi-pool allocation where each pool uses a different driver.

## How Tagging Works

1. **Tag the source.** The values table gets one or more tag columns that classify each row.
2. **Reference tags in the allocation rule.** When configuring the allocation step, you express rules in the form *"if source tag X = value Y, allocate using driver D and target dimension T."*
3. **The engine routes rows.** Each source row is matched against rules in order; the first matching rule decides the allocation behavior.

## Tag-Friendly Source Patterns

- A column named `cost_category` with values like `payroll`, `facilities`, `it`, `marketing`
- A column named `pool` that names the allocation pool the row belongs to
- A boolean column like `is_overhead` that triggers different treatment

## Example

A cost table with `cost_center` and `cost_category`:

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

You can configure two allocation rules:

- **Payroll rows** spread by headcount driver
- **IT rows** spread by user-count driver

Both rules run against the same source table; tags decide which one applies to each row.

## Related

- [Allocations Quick Start](/guides/allocations/getting-started/allocations-quick-start/) — basic flow before adding tagging
- [Configure an allocation](/guides/allocations/setup/configure-an-allocation/) — full step reference
- [Allocation rules step](/reference/workflow-steps/allocation/allocation-rules/) — workflow step that consumes tagged data
