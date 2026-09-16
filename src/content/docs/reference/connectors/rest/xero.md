---
title: Xero REST Connector
description: Set up a Xero connection in PlaidCloud with a one-click OAuth grant, import Accounting API entities, and post manual journals, invoices, bills, payments, and credit notes.
sidebar:
  order: 1
---

## API Documentation

Xero's [Accounting API reference](https://developer.xero.com/documentation/api/accounting/overview) documents the entities, `where=` filters, and create payloads this connector uses.

## How Authentication Works

The connection authenticates with Xero's **OAuth 2.0** grant. PlaidCloud registers the OAuth app itself, so there is no client id or client secret to obtain or enter — you click **Connect to Xero**, sign in to Xero, and approve the grant. PlaidCloud stores the resulting tokens on the connection and refreshes them for you, persisting each rotated refresh token so a long-idle connection keeps working.

One grant covers every Xero organisation you approve it for. The connection targets exactly one of them: the **Organisation** picker lists the organisations the grant returned, and every request carries that organisation's tenant id. To read or post against a second organisation, create a second Xero connection and pick that organisation on it.

Xero's Demo Company is an organisation property, not a connection setting — a demo organisation appears in the **Organisation** list like any other, so a sandbox connection is one that points at it.

## Configuration

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Connect to Xero | Button | Starts the Xero sign-in and consent flow. |
| Connection Status | Status | Reads `Not connected` until the grant completes, then reports how many organisations it covers. |
| Organisation | Select | Which Xero organisation this connection reads and posts against. Populated from the grant. |

## Rate Limits

Xero limits each organisation to 60 calls per minute and 5,000 calls per day, with a cap of 5 concurrent calls. PlaidCloud governs the per-minute and concurrency limits per connection, so one organisation's throttling never stalls another connection's calls, and honors Xero's `Retry-After` on a throttled response. The daily cap is yours to manage — schedule wide pulls rather than running many at once.

## Entities Available to Import

The **Xero: Import Entity** step covers eleven Accounting API entities: `accounts`, `contacts`, `invoices`, `credit_notes`, `payments`, `manual_journals`, `bank_transactions`, `items`, `tracking_categories`, `tax_rates`, and `currencies`. Each pull takes an optional status narrow, a date range, and a modified-since cutoff. See [Xero: Import Entity](/reference/workflow-steps/xero/import-xero-entity/) for the full field reference.

## Posting Documents

The **Xero: Post Document** step posts manual journals, invoices, bills, payments, and credit notes through PlaidCloud's shared ERP write pipeline, from a header table and a lines table. See [Xero: Post Document](/reference/workflow-steps/xero/xero-post/) for the field reference, and [Connect to Xero](/guides/connections/xero/) for the full posting walkthrough.

## Known Limitations

| Limitation | What it means |
|---|---|
| Manual journals and payments can't be looked up after an ambiguous outcome | Invoices, bills, and credit notes carry a document number PlaidCloud stamps and can query back. A manual journal's narration and a payment's reference are not queryable, so an in-doubt write of either is quarantined for you to resolve in Xero rather than guessed at. |
| Reversal covers manual journals and invoices only | A manual journal reverses as a debit/credit-swapped journal; an invoice reverses as a mirroring credit note. Bills, payments, and credit notes have no documented undo payload, so PlaidCloud refuses a reversal rather than inventing one. |
| Filters are fixed fields, not a query language | Xero's query API exposes a status narrow and a date range per entity, not an open filter language — so the import step offers those fields rather than a field/operator/value table. |
| One organisation per connection | Every request carries one tenant id. A second organisation needs a second connection. |

## Related

- [Connect to Xero (guide)](/guides/connections/xero/) — step-by-step: create the connection, test it, import an entity, and post a document.
- [Xero: Import Entity](/reference/workflow-steps/xero/import-xero-entity/)
- [Xero: Post Document](/reference/workflow-steps/xero/xero-post/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
