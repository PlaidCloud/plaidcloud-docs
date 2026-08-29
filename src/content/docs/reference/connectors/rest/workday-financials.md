---
title: Workday Financials Connector
description: Set up a Workday Financials connection in PlaidCloud with an Integration System User to import data through a RaaS report and post journal entries over SOAP.
sidebar:
  order: 1
---

## API Documentation

Workday's [SOAP web services](https://community.workday.com/sites/default/files/file-hosting/productionapi/) and [Report-as-a-Service (RaaS)](https://doc.workday.com/) document the interfaces this connector uses.

## How Authentication Works

The connection authenticates with an **Integration System User (ISU)** — a Workday user type built for system-to-system integration, secured by an Integration System Security Group that grants it just the access this connector needs (report access for reads, the Submit Accounting Journal business process for posts). Requests carry the ISU's username and password; there is no interactive sign-in.

## Configuration

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Tenant Host | Text | Your Workday host, e.g. `wd5-impl.workday.com`. |
| Tenant Name | Text | Your Workday tenant name. |
| ISU Username | Text | The Integration System User's username. |
| ISU Password | Text | The Integration System User's password. Stored encrypted. |

## Importing Data

Workday Financials has no fixed set of canned entities. Instead, the **Import Workday Entity** step calls a **Report-as-a-Service (RaaS) report** you build in Workday and publish with Web Service access — you supply its URL. The step supports filters on `company`, `ledger`, `period`, `accounting_date` (range), `ledger_account` (range), and `cost_center`, each passed through as a report parameter, so a filter only works if your report defines a matching prompt. See [Import Workday Entity](/reference/workflow-steps/workday-financials/import-workday-entity/) for the full field reference.

## Posting Journal Entries

The **Workday Financials: Post Journal Entry** step posts accounting journals through PlaidCloud's shared ERP write pipeline, using Workday's `Submit_Accounting_Journal` SOAP operation and polling the entry's business-process status to a terminal state before reporting it posted. A correction posts a new, debit/credit-swapped reversing entry rather than editing the original. See [Workday Financials: Post Journal Entry](/reference/workflow-steps/workday-financials/workday-post/) for the field reference, and [Connect to Workday Financials](/guides/connections/workday-financials/) for the full posting walkthrough.

## Known Limitations

| Limitation | What it means |
|---|---|
| Import shape depends on your RaaS report | PlaidCloud has no canned entities for Workday Financials — the report's fields, prompts, and access control all live in Workday. A report change there can change your import's shape without any change on the PlaidCloud side. |
| Business-process approval adds latency | A journal routed through an approval step in your Submit Accounting Journal business process stays `pending` until approved in Workday; the terminal-state poll waits for that. |
| No live tenant validation | This connector is newly released and built to Workday's documented SOAP and RaaS interfaces. It is pending validation against a live Workday tenant — verify report output and posting behavior in a sandbox tenant before relying on it in production. |

## Related

- [Connect to Workday Financials (guide)](/guides/connections/workday-financials/) — step-by-step: create the connection, test it, import a report, and post a journal.
- [Import Workday Entity](/reference/workflow-steps/workday-financials/import-workday-entity/)
- [Workday Financials: Post Journal Entry](/reference/workflow-steps/workday-financials/workday-post/)
- [Review ERP Post History](/guides/connections/erp-post-history/)
- [Workday REST Connector](/reference/connectors/rest/workday/) — the separate, generic Workday connector for HR/payroll REST data.
