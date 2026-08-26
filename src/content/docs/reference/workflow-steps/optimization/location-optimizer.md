---
title: Location Optimizer
description: Choose K sites from a set of candidates that minimize total or weighted distance to a set of demand points.
sidebar:
  order: 7
---

The Location Optimizer step chooses **K** sites from a table of candidate locations that minimize the total or weighted distance to a table of demand points — a p-median facility-location model solved as a mixed-integer program on PlaidCloud's HiGHS solver.

Location Optimizer runs in a workflow job pod, the same job image [Solver](/reference/workflow-steps/optimization/solver/) uses, and writes results back to project tables.

## Inputs

### Candidate Sites

The table of possible site locations, mapped with the same source/target column mapping, filters, and aggregation every table-mapped input uses.

### Demand Points

The table of points whose distance to the nearest selected site is minimized, mapped the same way.

### Distance Table (Optional)

A precomputed table of candidate-to-demand distances. Leave unset to have the step compute distances itself.

### K

The number of sites to select from Candidate Sites.

## Solver Options

| Option | Description |
| --- | --- |
| Time Limit | Optional runtime limit in seconds. |
| MIP Gap | Optional relative MIP gap. |
| Enable Presolve | Let the solver simplify the model before solving. Enabled by default. |
| Use Custom Resources | Set CPU cores and memory for the job pod. |

A **Time Limit** or **MIP Gap** stop returns the best solution found within that limit rather than the true optimum — the same trade-off [Solver](/reference/workflow-steps/optimization/solver/#status-behavior) makes on a non-optimal status. Leave both unset to solve to full optimality.

## Outputs

Location Optimizer writes three output tables, which must all be named distinctly.

### Selected Sites Output Table

One row per chosen site.

### Assignment Output Table

One row per demand point, naming the selected site it was assigned to.

### Summary Output Table

One row with solver status, objective value, and run details.

## Limits and Caveats

This step is a **p-median** model: it always minimizes total (optionally weighted) distance from demand points to their nearest selected site. It does not express a gravity-style score, a custom scoring formula, or any objective where a higher score is better rather than a lower distance. A site-selection problem that needs one of those belongs in a hand-built [Solver](/reference/workflow-steps/optimization/solver/) model instead.

## Related

- [Solver](/reference/workflow-steps/optimization/solver/) — general linear and mixed-integer optimization, for a site-selection objective this step's fixed p-median model doesn't cover.
- [Alteryx Conversion Matrix](/reference/alteryx-conversion-matrix/) — the Alteryx Location Optimizer tool converts to this step only for its linear distance-minimization case; a gravity kernel or custom scoring macro still refuses.
