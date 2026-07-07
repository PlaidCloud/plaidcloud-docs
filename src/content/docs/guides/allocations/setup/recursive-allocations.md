---
title: Recursive and Reciprocal Allocations
description: Model multi-pass and reciprocal cost distribution in PlaidCloud by chaining allocation steps into explicit staged passes.
sidebar:
  order: 2
---

Some cost models need the target of one allocation to become a *source* of the next — for example shared services that consume each other (IT serves HR, but HR also serves IT). PlaidCloud models this by **chaining allocation steps into explicit, staged passes**, not through a single automatic solver.

## When You Need Multiple Passes

- **Reciprocal services** — two cost pools that consume each other.
- **Layered spreads** — divisional costs cascade through a hierarchy, and the lower levels must absorb the upper levels before re-allocating.
- **Iterative balance** — the model approaches a stable result after several passes (pool A allocates some to B, B allocates some back, and so on).

## How to Model It

PlaidCloud has **no built-in "recursion mode" and no automatic convergence solver**. You build the recursion yourself by adding a separate [allocation split step](/reference/workflow-steps/allocation/allocation-split/) for each pass and wiring them in sequence:

1. Run the first pass as a normal allocation split.
2. For the next pass, build a source that includes the previous pass's output — typically by unioning or joining the prior result back into the pool — and allocate again.
3. Repeat for as many passes as your model needs.

Because each pass is an explicit step, **you decide how many passes run**. The engine does not solve the reciprocal relationship as a single simultaneous equation, and there is no tolerance setting that stops the loop automatically. Add passes until the residual still to be re-allocated is small enough for your purposes.

## Tips

- Start with a **single-pass** allocation and confirm the simple model behaves as expected before adding passes.
- After each pass, check the remaining unallocated residual. If it isn't shrinking pass over pass, revisit the driver relationships — a genuine circular dependency won't settle no matter how many passes you add.
- Every pass reprocesses its source, so recursion is expensive on large datasets. Test on a slice before running across the full source.

## Related

- [Configure an Allocation](/guides/allocations/setup/configure-an-allocation/) — base configuration
- [Allocation Split Step](/reference/workflow-steps/allocation/allocation-split/) — the workflow step you chain for each pass
- [Troubleshooting Allocations](/guides/allocations/results/troubleshooting-allocations/) — when residuals don't make sense
