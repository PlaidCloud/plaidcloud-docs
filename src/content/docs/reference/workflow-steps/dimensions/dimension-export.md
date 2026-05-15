---
title: Dimension Export
description: Export dimension data from PlaidCloud in a workflow step to save hierarchical structures as files or transfer to other systems.
sidebar:
  order: 4
---

## Description

Flattens a dimension into a tabular PlaidCloud table — one row per member with columns for parent, level, value, aliases, and properties. Use this when you need to query, join, or feed dimension structure into downstream systems that can't read PlaidCloud's hierarchical format directly.

Common use: export the dimension as a table, then write it to an external system (BI tool, reporting database, file delivery) using a regular export step.
