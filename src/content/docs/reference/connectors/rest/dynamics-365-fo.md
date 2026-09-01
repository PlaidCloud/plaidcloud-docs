---
title: Dynamics 365 Finance & Operations REST Connector
description: Set up a Dynamics 365 Finance & Operations connection in PlaidCloud to import OData/DMF entities and post journal entries asynchronously.
sidebar:
  order: 1
---

## API Documentation

D365 F&O's [OData v4 endpoints](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata) and [Data Management Framework](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export) document the endpoints and bulk-extract path this connector uses.

## How Authentication Works

The connection authenticates as an application using Entra ID (Azure AD) **client-credentials** — an app registration's client ID and secret exchanged for an access token, scoped to the environment's resource. There is no interactive sign-in.

## Configuration

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Environment URL | Text | Your D365 F&O environment URL, e.g. `https://yourorg.operations.dynamics.com`. |
| Client ID | Text | The Entra app registration's application (client) ID. |
| Client Secret | Text | The app registration's client secret. Stored encrypted. |
| Tenant ID | Text | Your Azure AD tenant ID. |
| Resource/Scope | Text | The OAuth2 scope requested, typically the environment URL plus `/.default`. |

## Entities Available to Import

The **Import D365 F&O Entity** step covers six entities: `main_accounts`, `currencies`, `customers`, `vendors`, `released_products`, `ledger_journal_headers`. Each pull runs in either `odata` sync mode (a direct call, for routine pulls) or `dmf` bulk mode (an asynchronous Data Management Framework export job, for large extracts), and supports per-entity server-side filters including date, account, and dimension ranges. See [Import D365 F&O Entity](/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) for the full field reference.

## Posting Journal Entries

The **D365 F&O: Post Journal Entry** step posts general ledger journal entries through PlaidCloud's shared ERP write pipeline: submit to D365 F&O's asynchronous custom-service journal post action, poll to a terminal state, and confirm before reporting an entry posted. A correction posts a new, debit/credit-swapped reversing entry rather than editing the original. See [D365 F&O: Post Journal Entry](/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) for the field reference, and [Connect to Dynamics 365 Finance & Operations](/guides/connections/dynamics-365-fo/) for the full posting walkthrough.

## Known Limitations

| Limitation | What it means |
|---|---|
| DMF sync mode has extract latency | A `dmf` pull waits on an asynchronous export job — materially slower than an `odata` pull of the same size. |
| Dimension filtering is structure-dependent | A financial dimension not part of your account structure isn't filterable server-side; scope it in your workflow after the pull. |
## Related

- [Connect to Dynamics 365 Finance & Operations (guide)](/guides/connections/dynamics-365-fo/) — step-by-step: create the connection, test it, import an entity, and post a journal.
- [Import D365 F&O Entity](/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
