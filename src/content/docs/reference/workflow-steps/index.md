---
title: Workflow Steps
description: Every workflow step type in PlaidCloud — import, export, transforms, allocations, dimensions, documents, notifications, and more.
---

Workflow steps are the building blocks of PlaidCloud automation. Each step performs one operation (import a CSV, join two tables, send a notification) and steps are composed into workflows that run sequentially, in parallel, conditionally, or in loops.

## Categories

### Data Movement

- [Import](/reference/workflow-steps/import/) — pull data in (26 source types: CSV, Excel, Parquet, JSON, SQL, BigQuery, SAS, SPSS, Singer sources, and more)
- [Export](/reference/workflow-steps/export/) — push data out (12 destination types: CSV, HTML, XML, SQL, Excel, Google Sheets, table archive, and more)

### Table Transformations

- [Tables](/reference/workflow-steps/tables/) — joins, unions, filters, lookups, pivots, melts, in-place updates (19 steps)
- [Common operations](/reference/workflow-steps/common/) — shared data mapping and filtering patterns

### Modeling

- [Allocation](/reference/workflow-steps/allocation/) — driver-based spreading, split allocations, rule-based tagging
- [Dimensions](/reference/workflow-steps/dimensions/) — load, sort, clear, export, and manage hierarchies
- [Optimization](/reference/workflow-steps/optimization/) — linear and mixed-integer solver steps

### Documents and Files

- [Document](/reference/workflow-steps/document/) — file operations, PDF manipulation, image processing, encoding conversion (20 steps)

### Communication

- [Notifications](/reference/workflow-steps/notifications/) — email, Slack, Teams, SMS, webhook, Twitter, log (9 steps)
- [Reports](/reference/workflow-steps/reports/) — render single or batch PDF reports from RML templates

### Workflow Control

- [Workflow control](/reference/workflow-steps/workflow-control/) — variables, loops, sub-workflows, Macros, error handling (13 steps)
- [General](/reference/workflow-steps/general/) — LLM step, pass, wait, user-defined transform, run remote Python

### Enterprise Integrations

- [Agent](/reference/workflow-steps/agent/) — PlaidLink Agent operations for on-premises resources
- [SAP](/reference/workflow-steps/sap/) — SAP ECC RFC calls
- [SAP-PCM](/reference/workflow-steps/sap-pcm/) — SAP Profitability and Cost Management model control
