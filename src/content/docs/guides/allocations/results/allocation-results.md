---
title: Allocation Results
description: Analyze PlaidCloud allocation results including reviewing output data, verifying distributions, and validating allocation accuracy.
sidebar:
  order: 1
---

After running an allocation step, the output is a result table you can inspect, verify, and feed into downstream steps.

## What the result table contains

A typical allocation result row includes:

- **Source identifier** — the row in the source table this allocation came from
- **Target identifier** — the row in the target dimension or table that received the spread
- **Allocated amount** — the share of the source amount assigned to this target
- **Driver value** — the driver number that justified the spread (e.g., the headcount, the revenue, the hours)
- **Allocation rate** — driver share as a proportion of the total
- **Source amount** — the original total being spread (carried for auditability)
- **Pool / tag / rule reference** — if rule-based tagging was used, which rule produced this row

The exact columns depend on the allocation step type and your configuration.

## Verification checklist

Before relying on the results:

1. **Reconciliation** — sum of allocated amounts equals sum of source amounts (within floating-point tolerance). If not, something didn't spread.
2. **No orphaned source rows** — every source row produced at least one allocation row. Orphans usually mean no driver data matched the source's tag or dimension member.
3. **No orphaned targets** — if you expected every target to receive something, check that every target dimension member appears in the results.
4. **Reasonable rates** — allocation rates should sum to 1.0 (100%) per source pool. Rates significantly off-target indicate driver data issues.
5. **Spot-check totals** — pick a high-value source row and verify its allocation matches what you'd compute by hand.

## Common patterns to look for

- **Zero allocations** — a target that received nothing usually means the driver row was missing or had a zero value
- **Mass concentration** — most of the spread landing on one target usually means the driver column has one very large value (often a data quality issue upstream)
- **Negative drivers** — depending on the allocation step, negative driver values may produce inverted spreads. Verify intent.

## Next steps

- [Troubleshooting allocations](/guides/allocations/results/troubleshooting-allocations/) — what to do when reconciliation fails
- [Publishing data](/guides/data/publish/) — once you trust the results, publish them for dashboards and downstream consumers
