---
title: Solver
description: Solve LP and MIP optimization problems from workflow table data.
sidebar:
  order: 6
---

The Solver step solves linear programming and mixed-integer programming problems from PlaidCloud tables. Use it when a workflow needs to choose values that minimize or maximize an objective while satisfying linear constraints.

Solver runs in a workflow job pod and writes results back to project tables.

## Inputs

Configure four input tables. Each input has a source table, data mapping, and filters. PlaidCloud translates those settings into the database query used to read each input, so selection happens before Solver receives the rows.

### Variables

One row per decision variable.

| Column | Description |
| --- | --- |
| `variable_id` | Unique variable name used by the other input tables. |
| `lower_bound` | Minimum value. Leave blank for no lower bound. |
| `upper_bound` | Maximum value. Leave blank for no upper bound. |
| `type` | `continuous`, `integer`, or `binary`. Binary variables use bounds `0` and `1`. |

### Objective

One row per variable with a non-zero objective coefficient.

| Column | Description |
| --- | --- |
| `variable_id` | Variable from the Variables input. |
| `coefficient` | Objective coefficient for that variable. |

Variables missing from this table use coefficient `0`.

### Constraints

One row per linear constraint.

| Column | Description |
| --- | --- |
| `constraint_id` | Unique constraint name used by the Coefficients input. |
| `lower_bound` | Minimum allowed activity. Leave blank for no lower bound. |
| `upper_bound` | Maximum allowed activity. Leave blank for no upper bound. |

Set the same lower and upper bound for an equality constraint.

### Coefficients

Sparse matrix of constraint coefficients.

| Column | Description |
| --- | --- |
| `constraint_id` | Constraint from the Constraints input. |
| `variable_id` | Variable from the Variables input. |
| `coefficient` | Coefficient for that variable in that constraint. |

## Solver Options

| Option | Description |
| --- | --- |
| Objective Direction | Choose Minimize or Maximize. |
| Time Limit | Optional runtime limit in seconds. |
| MIP Gap | Optional relative MIP gap for mixed-integer problems. |
| Enable Presolve | Let the solver simplify the model before solving. |
| Use Custom Resources | Set CPU cores and memory for the job pod. |

## Outputs

Solver writes three output tables.

### Solution Table

Contains one row per variable with the solved value, bounds, variable type, objective coefficient, and reduced cost when available.

### Constraint Results Table

Contains one row per constraint with activity, bounds, slack, and dual value when available.

### Summary Table

Contains one row with solver status, objective value, runtime, MIP gap, MIP dual bound, node count, iteration count, variable count, constraint count, and message.

## Status Behavior

An optimal solve completes the step successfully. If the solver returns a usable solution with a non-optimal status, the step finishes with a warning and still writes the output tables. If no usable solution is available, the step fails with the solver status message.
