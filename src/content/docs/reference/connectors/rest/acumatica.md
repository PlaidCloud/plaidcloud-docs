---
title: Acumatica REST Connector
description: Set up an Acumatica contract-based REST API connection in PlaidCloud to import master and transactional data and post journal transactions, invoices, bills, and payments.
sidebar:
  order: 1
---

## API Documentation

Acumatica's [contract-based REST API](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2) documents the endpoints and query options this connector uses.

## How Authentication Works

The connection is **session-based**: PlaidCloud logs in once per bounded unit of work (`POST <instance>/entity/auth/login` with your username, password, company, and optional branch) and reuses the resulting session cookie for every call in that unit, logging out when it's done. This isn't a bearer-token or OAuth flow — sessions count against your Acumatica license's concurrent-session limit, which trial and lower-tier instances can cap as low as 2, so avoid running many Acumatica steps in parallel on one connection.

## Configuration

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Base URL | Text | Your Acumatica instance URL, e.g. `https://yourcompany.acumatica.com`. |
| Username | Text | The PlaidCloud API user's login. |
| Password | Text | The PlaidCloud API user's password. Stored encrypted. |
| Company | Text | The exact Acumatica company ID this connection logs into. |
| Branch | Text | Optional. Leave blank to use the user's default branch. |

## Entities Available to Import

The **Import Acumatica Entity** step covers 18 contract-based entities:

**Master and reference data** — `account`, `subaccount`, `ledger`, `financial_period`, `branch`, `currency`, `currency_rate`, `customer`, `vendor`, `stock_item`, `warehouse`, `employee`, `tax_category`, `project`

**Transactional data** — `sales_invoice`, `bill`, `sales_order`, `shipment`

Each pull supports an `Active Only` toggle, an `Updated After` cutoff, and per-entity server-side filters. See [Import Acumatica Entity](/reference/workflow-steps/acumatica/import-acumatica-entity/) for the full field reference.

## Posting Documents

The **Acumatica Post** step posts **JournalTransaction**, **SalesInvoice**, **Bill**, and **Payment** documents through PlaidCloud's shared ERP write pipeline: create on Hold, release (an async action), and confirm the release before reporting a document posted. See [Acumatica: Post Documents](/reference/workflow-steps/acumatica/acumatica-post/) for the field reference, and [Connect to Acumatica](/guides/connections/acumatica/) for the full posting walkthrough.

## Known Limitations

| Limitation | What it means |
|---|---|
| GI-dependent reads not covered | Trial balance, GL transaction detail, inventory-on-hand, budgets, and intercompany data live behind Acumatica Generic Inquiries, not the 18 contract-based entities above. Build the GI in Acumatica and pull it with a [Generic REST connection](/reference/connectors/rest/generic-rest/). |
| No native idempotency key on write | Acumatica's PUT-based write API has no idempotency field; PlaidCloud's own ledger claim is the sole guard against a double post. |
| Reversal is manual | No document type has a documented void/reversal action. A posted document can't be reversed from PlaidCloud — correct it directly in Acumatica. |
| No Payment correlation field | Acumatica exposes no documented field to correlate a Payment to PlaidCloud's request after an ambiguous outcome; an in-doubt Payment is quarantined for manual resolution. |
| Line-item filtering isn't server-side | `$filter`-style filters reach entity and header fields, not a document's line-item dimensions (for example a line-level cost center). Scope lines in your workflow after the pull. |
| No live tenant validation | This connector is newly released and built to Acumatica's documented contract-based REST API. It is pending validation against a live Acumatica instance — verify field mappings and posting behavior in a sandbox company before relying on it in production. |

## Related

- [Connect to Acumatica (guide)](/guides/connections/acumatica/) — step-by-step: create the connection, test it, import an entity, and post a batch.
- [Import Acumatica Entity](/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/reference/workflow-steps/acumatica/acumatica-post/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
