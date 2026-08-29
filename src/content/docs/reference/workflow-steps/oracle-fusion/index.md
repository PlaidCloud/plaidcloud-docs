---
title: Oracle Fusion Steps
description: Workflow steps that read from and write to Oracle Fusion Cloud over your Oracle Fusion connection — import GL balances and journal batches over OData/BIP or bulk FBDI extract, and post journal entries.
---

Workflow steps that read from and write to Oracle Fusion Cloud over your [Oracle Fusion connection](/guides/connections/oracle-fusion/). Two import steps cover different pull sizes — a direct OData/BIP call for routine pulls, and an asynchronous FBDI/BIP bulk extract for large ones; the post step posts journal batches through PlaidCloud's shared ERP write pipeline.

## Steps

- [Import Fusion Entity](/reference/workflow-steps/oracle-fusion/import-fusion-entity/) — GL balances and journal batches, with server-side date, period, and numeric range filters.
- [Import Fusion Bulk Extract](/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) — the same entities, via an asynchronous FBDI/BIP export job for large pulls.
- [Oracle Fusion: Post Journal Entry](/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) — post general ledger journal batches through the FBDI GL Interface, with a posted reversing entry for corrections.

## Related

- [Oracle Fusion Connector](/reference/connectors/erp/oracle-fusion/)
- [Connect to Oracle Fusion](/guides/connections/oracle-fusion/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
