---
title: Business Central Steps
description: Workflow steps that read from and write to Microsoft Dynamics 365 Business Central over your Business Central connection — import OData entities, and post general journal lines.
---

Workflow steps that read from and write to Business Central over your [Business Central connection](/guides/connections/business-central/). The import step pulls Business Central's standard OData v2.0 entities with no query to write; the post step posts general journal lines through PlaidCloud's shared ERP write pipeline.

## Steps

- [Import Business Central Entity](/reference/workflow-steps/business-central/import-business-central-entity/) — accounts, ledger entries, customers, vendors, items, and journals, with server-side filters.
- [Business Central: Post General Journal Lines](/reference/workflow-steps/business-central/business-central-post/) — post lines into an existing journal batch and post the batch.

## Related

- [Business Central REST Connector](/reference/connectors/rest/business-central/)
- [Connect to Business Central](/guides/connections/business-central/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
