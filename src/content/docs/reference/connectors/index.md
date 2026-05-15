---
title: Data and Service Connectors
description: Connect PlaidCloud to external data sources and services including databases, ERPs, REST APIs, cloud storage, and Git repositories.
sidebar:
  label: Data and Service Connectors
---

PlaidCloud connects to external data sources and services through purpose-built connectors. Each connector handles the authentication, protocol, and data-shape specifics of one provider family.

## Categories

### Databases and Data Lakes

Relational databases, cloud warehouses, query engines, and lakehouse formats.

- [Databases](/reference/connectors/databases/) — PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, Redshift, BigQuery, Databricks, and 15+ more
- [Open Tables](/reference/connectors/open-tables/) — Apache Iceberg, Delta Lake, Hudi, Hive open table formats

### Cloud and SaaS Services

- [REST](/reference/connectors/rest/) — Salesforce, NetSuite, Workday, QuickBooks, Stripe, Dynamics, and more
- [ERP systems](/reference/connectors/erp/) — SAP ECC, S/4HANA, Oracle EBS/Fusion, Infor, JD Edwards
- [Cloud services](/reference/connectors/cloud-services/) — third-party data services
- [Google](/reference/connectors/google/) — BigQuery, Google Sheets
- [Collaboration](/reference/connectors/collaboration/) — Slack, Microsoft Teams

### Development and Source Control

- [Git providers](/reference/connectors/git/) — GitHub, GitLab, Bitbucket, Azure Repos, CodeCommit

## Related

- [Connections guide](/guides/connections/) — task-oriented walkthrough for creating and managing connections
- [Workflow steps reference](/reference/workflow-steps/) — what to do with a connection once it's configured
