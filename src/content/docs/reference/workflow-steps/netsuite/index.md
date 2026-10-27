---
title: NetSuite Steps
description: NetSuite workflow steps — import balances, GL detail, master data or your own SuiteQL query, and post journal entries over your NetSuite connection.
---

Workflow steps that read from and write to NetSuite over your [NetSuite connection](/guides/connections/netsuite/). The canned import steps are the simplest way to pull the common financial and reference data — pick a connection, a target table, and a date range or record type, with no SuiteQL to write.

## Import Steps

- [NetSuite: Import Balances](/reference/workflow-steps/netsuite/import-balances/) — account balances (a trial balance) for a date range and subsidiary.
- [NetSuite: Import GL Detail](/reference/workflow-steps/netsuite/import-gl-detail/) — general ledger transaction-line detail for a date range and subsidiary.
- [NetSuite: Import Master Data](/reference/workflow-steps/netsuite/import-master-data/) — master lists: accounts, subsidiaries, departments, classes, locations, vendors, or customers.
- [NetSuite: Import SuiteQL Query](/reference/workflow-steps/netsuite/import-suiteql-query/) — run your own SuiteQL query and load the result into a typed table, with date windows and paging handled for you.

## Post Steps

- [Post NetSuite Journal Entry](/reference/workflow-steps/netsuite/post-netsuite-journal-entry/) — post header/line journal entries back to NetSuite.

## Custom Pulls

For data the canned import steps don't cover — a bespoke query, or a NetSuite record with no canned step — use [NetSuite: Import SuiteQL Query](/reference/workflow-steps/netsuite/import-suiteql-query/) with your own SuiteQL. See [NetSuite SuiteQL Query Examples](/guides/connections/netsuite-financial-queries/) for starting points.

## Related

- [NetSuite REST Connector](/reference/connectors/rest/netsuite/)
- [Connect to NetSuite](/guides/connections/netsuite/)
- [Import NetSuite Financials](/guides/connections/import-netsuite-financials/)
