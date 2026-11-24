---
title: Analytics Learning Path
description: What to read before the PlaidCloud Analytics Practitioner and Expert labs, and what each lab asks you to do.
sidebar:
  label: Analytics
---

The Analytics track is about metrics that give one right answer however they're broken down, and shared meanings across tables. Start with the [Foundations](/guides/certification/foundations/) path. For how labs work, see [PlaidCloud Certification](/guides/certification/).

## Practitioner

### Read in This Order

1. [Run a Workflow](/guides/workflows/run-a-workflow/)
2. [Viewing Workflow Log](/guides/workflows/viewing-workflow-log/)
3. [Metric Definitions](/integrations/ai-coding-agents/metric-definitions/), including how to derive a metric from others
4. [Build a Dashboard From a Published Table](/get-started/tutorials/build-a-dashboard/), for the optional dashboard

### What the Lab Asks

The lab is called *Analytics: define metrics for three questions*.

You run a workflow that prepares a sales table, then define metrics on that table, each with region and channel in its grain: revenue by region, average order value by channel, derived from an order count, and cost as a share of revenue by region, derived from a cost metric. Every metric is built on the prepared table, not the raw one. A dashboard for the three answers is a good next step, but it isn't graded.

The lab checks that the workflow runs and that each of the three metrics gives the right answer.

## Expert

The Expert lab is timed: you have 4 hours from the moment you start it.

### Read in This Order

1. [Metric Definitions](/integrations/ai-coding-agents/metric-definitions/)
2. [Data Model and Project Elements](/guides/projects/data-model/)
3. [Analysis Paths](/integrations/ai-coding-agents/analysis-paths/)

### What the Lab Asks

The lab is called *Analytics Expert: metrics that agree*.

Two metrics give different answers depending on how they're broken down, and the revenue total is more than the orders add up to. You repair them so each returns one correct answer by region and by product, keeping their names. Then you make the columns that mean the same thing one shared element: one for region, across the tables that hold it under different column names, and one for product.

The lab checks that the workflow runs, that revenue by region and by product and units by product are right, and that the elements cover the right columns.
