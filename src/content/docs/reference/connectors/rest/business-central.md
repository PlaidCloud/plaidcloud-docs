---
title: Business Central REST Connector
description: Set up a Microsoft Dynamics 365 Business Central connection in PlaidCloud with Azure AD client-credentials to import OData entities and post general journal lines.
sidebar:
  order: 1
---

## API Documentation

Business Central's [standard OData v2.0 API](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) documents the entities and `$filter`/`$orderby` options this connector uses.

## How Authentication Works

The connection authenticates as an application using Entra ID (Azure AD) **client-credentials (S2S)** — an app registration's client ID and secret exchanged for an access token at `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token`, scoped to `https://api.businesscentral.dynamics.com/.default`. There is no interactive sign-in. The app registration needs API permissions granted to Business Central (`API.ReadWrite.All` or a narrower scope your admin issues).

Every request is scoped to one **environment** (e.g. `Production` or a sandbox environment) and one **company** within it — both are set on the connection, not chosen per request.

## Configuration

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Client ID | Text | The Entra app registration's application (client) ID. |
| Client Secret | Text | The app registration's client secret. Stored encrypted. |
| Tenant ID | Text | Your Azure AD tenant ID. |
| Environment | Text | The Business Central environment name, e.g. `Production`. |
| Company | Text | The Business Central company ID this connection reads and posts against. |

## Entities Available to Import

The **Import Business Central Entity** step covers six entities: `accounts`, `generalLedgerEntries`, `customers`, `vendors`, `items`, `journals`. Each pull supports per-entity server-side filters. See [Import Business Central Entity](/reference/workflow-steps/business-central/import-business-central-entity/) for the full field reference.

`generalLedgerEntries` is read-only and posted-only — it's the entity to pull for a trial balance or GL detail, since it never includes a line still sitting in an unposted journal batch.

## Posting General Journal Lines

The **Business Central Post** step creates lines inside an **existing** journal batch and posts that batch through PlaidCloud's shared ERP write pipeline, verifying the batch holds only this request's lines before posting and confirming the post against `generalLedgerEntries` (not the journal batch itself). See [Business Central: Post General Journal Lines](/reference/workflow-steps/business-central/business-central-post/) for the field reference, and [Connect to Business Central](/guides/connections/business-central/) for the full posting walkthrough.

## Known Limitations

| Limitation | What it means |
|---|---|
| One write document type | Only General Journal Line posting is supported. The draft-document flow (sales/purchase invoices, Draft → Posted) is not — the post action for that flow isn't pinned down in Microsoft's published documentation. |
| Posts into an existing batch only | This connector never creates a journal batch in Business Central — create it there first. |
| Concurrent same-batch posts | The idempotency guard is scoped by document number, not by journal batch — two different document numbers posting concurrently to the same batch aren't guaranteed to serialize. |
| No live tenant validation | Built to Business Central's documented OData v2.0 API and a mock server; not yet exercised against a live tenant. |

## Related

- [Connect to Business Central (guide)](/guides/connections/business-central/) — step-by-step: create the connection, test it, import an entity, and post a journal.
- [Import Business Central Entity](/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/reference/workflow-steps/business-central/business-central-post/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
