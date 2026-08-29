---
title: Dynamics 365 F&O Steps
description: Workflow steps that read from and write to Dynamics 365 Finance & Operations over your D365 F&O connection — import OData/DMF entities, and post journal entries.
---

Workflow steps that read from and write to Dynamics 365 Finance & Operations (D365 F&O) over your [D365 F&O connection](/guides/connections/dynamics-365-fo/). The import step pulls OData entities or bulk DMF extracts with no OData to write; the post step posts general ledger journal entries through PlaidCloud's shared ERP write pipeline.

## Steps

- [Import D365 F&O Entity](/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) — master data and journal headers, in OData or DMF bulk mode, with server-side filters.
- [D365 F&O: Post Journal Entry](/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) — post general ledger journal entries, with a posted reversing entry for corrections.

## Related

- [Dynamics 365 F&O REST Connector](/reference/connectors/rest/dynamics-365-fo/)
- [Connect to Dynamics 365 Finance & Operations](/guides/connections/dynamics-365-fo/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
