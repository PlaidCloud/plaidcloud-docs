---
title: Workday Financials Steps
description: Workflow steps that read from and write to Workday Financials over your Workday Financials connection — import data through a RaaS report, and post accounting journals.
---

Workflow steps that read from and write to Workday Financials over your [Workday Financials connection](/guides/connections/workday-financials/). The import step pulls a customer-supplied Report-as-a-Service (RaaS) report; the post step posts accounting journals through PlaidCloud's shared ERP write pipeline.

## Steps

- [Import Workday Entity](/reference/workflow-steps/workday-financials/import-workday-entity/) — pull a RaaS report, with report-parameter filters.
- [Workday Financials: Post Journal Entry](/reference/workflow-steps/workday-financials/workday-post/) — post accounting journals via `Submit_Accounting_Journal`, with a posted reversing entry for corrections.

## Related

- [Workday Financials Connector](/reference/connectors/rest/workday-financials/)
- [Connect to Workday Financials](/guides/connections/workday-financials/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
