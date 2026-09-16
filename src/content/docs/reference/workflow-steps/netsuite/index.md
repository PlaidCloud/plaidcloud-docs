---
title: NetSuite Steps
description: Workflow steps that read from and write to NetSuite over your NetSuite connection — import balances, GL detail, and master data, and post journal entries.
---

Workflow steps that read from and write to NetSuite over your [NetSuite connection](/guides/connections/netsuite/). The canned import steps are the simplest way to pull the common financial and reference data — pick a connection, a target table, and a date range or record type, with no SuiteQL to write.

## Import Steps

- [NetSuite: Import Balances](/reference/workflow-steps/netsuite/import-balances/) — account balances (a trial balance) for a date range and subsidiary.
- [NetSuite: Import GL Detail](/reference/workflow-steps/netsuite/import-gl-detail/) — general ledger transaction-line detail for a date range and subsidiary.
- [NetSuite: Import Master Data](/reference/workflow-steps/netsuite/import-master-data/) — master lists: accounts, subsidiaries, departments, classes, locations, vendors, or customers.

## Post Steps

- [Post NetSuite Journal Entry](/reference/workflow-steps/netsuite/post-netsuite-journal-entry/) — post header/line journal entries back to NetSuite.

## Custom Pulls

For data the import steps don't cover — a bespoke query, or a NetSuite record with no canned step — use the [REST Request step](/guides/workflows/rest-request-step/) against your NetSuite connection with your own SuiteQL. See [NetSuite SuiteQL Query Examples](/guides/connections/netsuite-financial-queries/).

## Related

- [NetSuite REST Connector](/reference/connectors/rest/netsuite/)
- [Connect to NetSuite](/guides/connections/netsuite/)
- [Import NetSuite Financials](/guides/connections/import-netsuite-financials/)
