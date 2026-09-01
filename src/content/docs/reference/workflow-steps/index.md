---
title: Workflow Steps
description: Every workflow step type in PlaidCloud — import, export, transforms, allocations, dimensions, documents, notifications, and more.
---

Workflow steps are the building blocks of PlaidCloud automation. Each step performs one operation (import a CSV, join two tables, send a notification) and steps are composed into workflows that run sequentially, in parallel, conditionally, or in loops.

## Categories

### Data Movement

- [Import](/reference/workflow-steps/import/) — pull data in (24 source types: CSV, Excel, Parquet, JSON, SQL, BigQuery, SPSS, Singer sources, and more)
- [Export](/reference/workflow-steps/export/) — push data out (11 destination types: CSV, XML, SQL, Excel, Google Sheets, table archive, and more)

### Table Transformations

- [Tables](/reference/workflow-steps/tables/) — joins, unions, filters, lookups, pivots, melts, targeted updates (19 steps)
- [Common operations](/reference/workflow-steps/common/) — shared data mapping and filtering patterns

### Geospatial

- [Geospatial](/reference/workflow-steps/spatial/) — import spatial files, buffer, match, measure, and build geometry; full Alteryx spatial-tool coverage (14 steps)

### Modeling

- [Allocation](/reference/workflow-steps/allocation/) — driver-based spreading, split allocations, rule-based tagging
- [Dimensions](/reference/workflow-steps/dimensions/) — load, sort, clear, export, and manage hierarchies
- [Optimization](/reference/workflow-steps/optimization/) — linear and mixed-integer solver steps
- [Machine learning](/reference/workflow-steps/machine-learning/) — train scikit-learn models and score tables with them (2 steps)

### Documents and Files

- [Document](/reference/workflow-steps/document/) — file operations, directory listing, PDF manipulation, image processing, encoding conversion (21 steps)
- [Text and documents](/reference/workflow-steps/text-documents/) — PDF text extraction, image OCR, sentiment, topic modeling, word clouds (6 steps)

### Communication

- [Notifications](/reference/workflow-steps/notifications/) — email, Slack, Teams, SMS, webhook, Twitter, log (9 steps)
- [Reports](/reference/workflow-steps/reports/) — render single or batch PDF reports from RML templates

### Workflow Control

- [Workflow control](/reference/workflow-steps/workflow-control/) — variables, loops, sub-workflows, Macros, error handling, row-count assert (14 steps)
- [General](/reference/workflow-steps/general/) — LLM step, pass, wait, user-defined transform, run remote Python, Alteryx executor
- [Packaged macros](/reference/workflow-steps/macros/) — Alteryx packaged-macro equivalents: Create Samples, DateTime Now, Heat Map, Pie Wedge Trade Area (4 steps)

### Enterprise Integrations

- [Agent](/reference/workflow-steps/agent/) — PlaidLink Agent operations for on-premises resources
- [NetSuite](/reference/workflow-steps/netsuite/) — import balances, GL detail, and master data; post journal entries to NetSuite
- [Acumatica](/reference/workflow-steps/acumatica/) — import master and transactional entities; post journal transactions, invoices, bills, and payments
- [Business Central](/reference/workflow-steps/business-central/) — import OData entities; post general journal lines
- [Dynamics 365 F&O](/reference/workflow-steps/dynamics-365-fo/) — import OData/DMF entities; post journal entries
- [Oracle Fusion](/reference/workflow-steps/oracle-fusion/) — import GL balances and journal batches; post journal entries through FBDI
- [Oracle EPM (HFM / FCCS)](/reference/workflow-steps/oracle-epm/) — self-serve an ad-hoc data slice from Oracle FCCS with a point-of-view picker; optional scheduled recurring load
- [Workday Financials](/reference/workflow-steps/workday-financials/) — import a RaaS report; post accounting journals
- [Sage Intacct](/reference/workflow-steps/sage-intacct/) — import balances, AP bills, ad-hoc queries, and GL/dimension objects; post journal entries
- [SAP S/4HANA Cloud](/reference/workflow-steps/s4hana-cloud/) — import trial balance and journal entry items over OData; post journal entries over SOAP
- [SAP](/reference/workflow-steps/sap/) — SAP ECC / S/4HANA RFC calls
- [SAP-PCM](/reference/workflow-steps/sap-pcm/) — SAP Profitability and Cost Management model control
