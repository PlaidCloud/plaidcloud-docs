---
title: SAP S/4HANA Cloud Steps
description: Workflow steps that read from and write to SAP S/4HANA Cloud Public Edition over your S/4HANA Cloud connection — import trial balance and journal entry items, and post journal entries.
---

Workflow steps that read from and write to SAP S/4HANA Cloud Public Edition over your [S/4HANA Cloud connection](/guides/connections/s4hana-cloud/). The import step pulls trial balance or journal entry item data with no OData to write; the post step posts journal entries through PlaidCloud's shared ERP write pipeline.

## Steps

- [Import S/4HANA Entity](/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) — trial balance and journal entry item data, with server-side filters.
- [S/4HANA: Post Journal Entry](/reference/workflow-steps/s4hana-cloud/s4hana-post/) — post journal entries over SOAP, with a posted reversing entry for corrections.

## Related

- [SAP S/4HANA Cloud REST Connector](/reference/connectors/rest/s4hana-cloud/)
- [Connect to SAP S/4HANA Cloud](/guides/connections/s4hana-cloud/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
