---
title: Manage Workflow Variables
description: Manage workflow variables in PlaidCloud to store and pass dynamic values between steps for flexible data processing logic.
sidebar:
  order: 14
---

PlaidCloud allows variables at both the project scope and workflow scope. This allows for setting project wide variables or being able to pass information easily between workflows. The variables and values are viewed by clicking on the variables icon in the **Workflows** hierarchy.



From the variables table you can view the variables, the current values, and edit the values. You can also add new variables or delete existing ones.

## Built-in Variables

Step settings and expressions can use these built-in variables without defining them:

| Variable | Value |
|---|---|
| `{project}`, `{model}` | The IDs of the project and the workflow the step runs in. |
| `{cloud}` | The workspace name. |
| `{date}` | The run's current UTC time in long form, such as `Wednesday, 11 November 2026 10:30PM UTC +0`. |
| `{date_iso}` | The same moment in ISO 8601, such as `2026-11-12T22:49:56+00:00`. |

Use `{date_iso}` when an expression needs to read part of the date. Taking its first 7 characters gives the month (`2026-11`) and its first 10 gives the day (`2026-11-12`). `{date_iso}` works everywhere `{date}` does, including notification email templates, and Forecast, Parity and Solver steps.
