---
title: Acumatica Steps
description: Workflow steps that read from and write to Acumatica over your Acumatica connection — import contract-based REST entities, and post journal transactions, invoices, bills, and payments.
---

Workflow steps that read from and write to Acumatica over your [Acumatica connection](/guides/connections/acumatica/). The import step pulls Acumatica's contract-based REST entities with no OData to write; the post step posts journal transactions, sales invoices, bills, and payments through PlaidCloud's shared ERP write pipeline.

## Steps

- [Import Acumatica Entity](/reference/workflow-steps/acumatica/import-acumatica-entity/) — master data and transactional entities, with server-side filters.
- [Acumatica: Post Documents](/reference/workflow-steps/acumatica/acumatica-post/) — post journal transactions, sales invoices, bills, and payments.

## Related

- [Acumatica REST Connector](/reference/connectors/rest/acumatica/)
- [Connect to Acumatica](/guides/connections/acumatica/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
