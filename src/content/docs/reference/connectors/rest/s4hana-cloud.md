---
title: SAP S/4HANA Cloud REST Connector
description: Set up a SAP S/4HANA Cloud Public Edition connection in PlaidCloud to import trial balance and journal entry item data over OData, and post journal entries over SOAP.
sidebar:
  order: 1
---

## API Documentation

SAP S/4HANA Cloud's [Trial Balance API (`API_OPLACCTGDOCITEMCUBE_SRV`)](https://api.sap.com/) and [Journal Entry Item - Basic API (`API_JOURNALENTRYITEMBASIC_SRV`)](https://api.sap.com/) on SAP API Business Hub document the OData endpoints this connector uses, alongside the SOAP journal-entry bulk-create service exposed through a Communication Arrangement.

## How Authentication Works

The connection authenticates as an application using **OAuth2 client-credentials** — a Communication Arrangement's client ID and secret exchanged for an access token against the tenant's OAuth2 token endpoint. There is no interactive sign-in.

## Configuration

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Host | Text | Your S/4HANA Cloud tenant host, e.g. `https://yourorg.s4hana.ondemand.com`. |
| Token URL | Text | The Communication Arrangement's OAuth2 token endpoint. |
| Client ID | Text | The Communication Arrangement's OAuth2 client ID. |
| Client Secret | Text | The Communication Arrangement's OAuth2 client secret. Stored encrypted. |

## Entities Available to Import

The **Import S/4HANA Entity** step covers two entities: `trial_balance` (aggregated period-end GL account balances, over `API_OPLACCTGDOCITEMCUBE_SRV`) and `journal_entry_items` (posted journal entry line items, over `API_JOURNALENTRYITEMBASIC_SRV`). Both support server-side filters on `CompanyCode`, `GLAccount`, `CostCenter`, `ProfitCenter`, `FiscalYear`, `FiscalPeriod`, and `Ledger`, with `PostingDate`, `FiscalYear`, and `FiscalPeriod` accepting `ge`/`le` range bounds. See [Import S/4HANA Entity](/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) for the full field reference.

## Posting Journal Entries

The **S/4HANA: Post Journal Entry** step posts general ledger journal entries through PlaidCloud's shared ERP write pipeline: submit via S/4HANA Cloud's `JournalEntryBulkCreateRequest_In` SOAP service, poll for the `JournalEntryBulkCreateConfirmation_Out` confirmation, and confirm before reporting an entry posted. A correction posts a new, debit/credit-swapped reversing entry rather than editing the original. See [S/4HANA: Post Journal Entry](/reference/workflow-steps/s4hana-cloud/s4hana-post/) for the field reference, and [Connect to SAP S/4HANA Cloud](/guides/connections/s4hana-cloud/) for the full posting walkthrough.

## Known Limitations

| Limitation | What it means |
|---|---|
| Confirmation latency | The SOAP bulk-create service processes requests asynchronously — materially slower than a synchronous OData write of the same size. |
| Filterable fields depend on your Communication Scenario | A cost object or dimension not exposed by your Communication Scenario isn't filterable server-side; scope it in your workflow after the pull. |
| No live tenant validation | This connector is newly released and built to S/4HANA Cloud's documented OData and SOAP APIs. It is pending validation against a live S/4HANA Cloud tenant — verify field mappings and posting behavior in a sandbox tenant before relying on it in production. |

## Related

- [Connect to SAP S/4HANA Cloud (guide)](/guides/connections/s4hana-cloud/) — step-by-step: create the connection, test it, import an entity, and post a journal.
- [Import S/4HANA Entity](/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
- [SAP ECC / S/4HANA Connector](/reference/connectors/erp/sap-s4/) — the separate, RFC/agent-based connector for on-premises or private-cloud S/4HANA.
