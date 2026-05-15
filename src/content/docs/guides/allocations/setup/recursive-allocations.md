---
title: Recursive Allocations
description: Set up recursive allocations in PlaidCloud to handle multi-pass cost distribution where allocated costs feed subsequent rounds.
sidebar:
  order: 2
---

Recursive allocations handle the case where a target of one allocation becomes a *source* of the next. Common when modeling shared services that consume each other — IT serves HR, but HR also serves IT.

## When you need recursion

- **Reciprocal services** — two cost pools that consume each other.
- **Layered spreads** — divisional costs cascade through a hierarchy and the lower levels need to absorb the upper levels before re-allocating.
- **Iterative balance** — the model needs to converge after multiple passes (cost pool A allocates some to B, B allocates some back, repeat until stable).

## How recursion works in PlaidCloud

Configure the allocation step with:

- **Source table** — where the values start
- **Driver table** — the basis for spreading
- **Recursion mode** — direct (one pass), reciprocal (resolve mutual dependencies), or iterative (loop until convergence)
- **Convergence tolerance** — for iterative mode, how close residuals must be to zero before the loop stops
- **Maximum iterations** — safety cap so a non-converging model doesn't loop forever

The output table includes a generation or iteration column so downstream consumers can see which pass each row came from.

## Reciprocal vs iterative

- **Reciprocal** — solves a simultaneous equation in one mathematical pass. Use when relationships are well-defined and finite.
- **Iterative** — runs allocations repeatedly until each round produces a residual smaller than your tolerance. Use when you want explicit control over how many passes happen, or when the relationship isn't easily inverted.

## Tips

- Start with **direct** (single-pass) allocations and confirm the simple model behaves as expected before introducing recursion.
- For iterative models, log the residual at each pass while tuning. If residuals don't shrink, the model has a circular dependency the engine can't resolve cleanly.
- Recursive allocations can be expensive on large datasets. Test on a slice before running across the full source.

## Related

- [Configure an allocation](/guides/allocations/setup/configure-an-allocation/) — base configuration
- [Allocation split step](/reference/workflow-steps/allocation/allocation-split/) — workflow step for split allocations
- [Troubleshooting allocations](/guides/allocations/results/troubleshooting-allocations/) — when residuals don't make sense
