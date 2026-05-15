---
title: Worklow Loop
description: Create a loop in a PlaidCloud workflow step to iterate over a set of values and repeat steps for each item in the collection.
sidebar:
  order: 9
---

## Description

Runs a target workflow once per row of a dataset, setting each row's column values as project variables before each iteration. Use this when you have a parameterized process that needs to run multiple times with different inputs — for example, "run the monthly close for every business unit in this table," or "load this report for every quarter listed."

Each loop iteration sees the variables as if they had been set manually, so the called workflow can reference them in expressions, filters, file paths, and table names using the standard `\{variable_name}` syntax. The loop is sequential by default; iterations don't run in parallel.



## Workflow to Stop


First, select the Project which contains the workflow that will be run on each loop from the **Project** dropdown menu.



Next, select the particular workflow for running from the **Workflow** dropdown menu.

## Examples

Examples coming soon
