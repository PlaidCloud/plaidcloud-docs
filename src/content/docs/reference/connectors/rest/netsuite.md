---
title: NetSuite REST Connector
description: Set up a NetSuite REST API connection in PlaidCloud and pull financial and operational data with SuiteQL — OAuth 2.0 setup, connection fields, and query recipe.
sidebar:
  order: 1
---

The NetSuite connector authenticates with **OAuth 2.0 client credentials** (a signed JWT client assertion) and pulls tabular data with **SuiteQL** through the [REST Request step](/guides/workflows/rest-request-step/). For a start-to-finish walkthrough — connection, smoke test, and a scheduled financial and operational pull — see [Connect to NetSuite](/guides/connections/netsuite/).

## API Documentation

The [vendor API reference](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1540391670.html) covers NetSuite's REST record and SuiteQL query services.

## Security Requirements

The connector signs in as an integration, with no interactive login:

- A **2048-bit RSA key pair**. The **public certificate** is uploaded to NetSuite; the **private key** is held by PlaidCloud and used to sign a short-lived JWT that is exchanged for an access token. The private key is stored encrypted and never returned in cleartext.
- An **integration record** in NetSuite, which yields the **client id**.
- A **role** granting REST Web Services, **Log in using OAuth 2.0 Access Tokens**, and view access to every record your queries read. Add **SuiteAnalytics Workbook** if your queries touch analytics.

> The exact role permissions and OAuth scopes are built to NetSuite's documented shape and confirmed at live cutover — if a first call is rejected for scope or role, the surfaced error names the cause.

## NetSuite-Side Setup

Complete these in NetSuite before creating the connection. You end with four values: **account id**, **client id**, **certificate id**, and the **private key PEM**.

1. **Enable the features.** **Setup > Company > Enable Features > SuiteCloud** — turn on **REST Web Services** and **OAuth 2.0**.
2. **Generate the key pair.** Create a 2048-bit RSA key pair (for example with `openssl`). Keep the private key PEM for PlaidCloud.
3. **Upload the public certificate.** **Setup > Integration > OAuth 2.0 Client Credentials (M2M) Setup**, map the certificate to your integration and role, and record the **certificate id** it returns — this is the JWT `kid`.
4. **Create the integration record.** **Setup > Integration > Manage Integrations > New**, enable **Client Credentials**, and record the **client id**.
5. **Note the account id.** **Setup > Company > Company Information** — production is a number like `1234567`; a sandbox carries a suffix like `1234567_SB1`. Enter it exactly as shown; PlaidCloud derives the API host from it (underscores become hyphens, lower-cased — `1234567_SB1` resolves to `1234567-sb1.suitetalk.api.netsuite.com`).

## Configuration

These fields appear when creating or editing this connection.

### Identification

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Alias | Text (multi-line) | Optional alias or notes about the connection. |
| Is active | Toggle | Whether the connection is enabled. Disable to pause without deleting. |
| Db read only | Toggle | Restrict the connection to read-only operations. |
| Access type | Select | Read-only, write-only, or read-write access level for this connection. |

### NetSuite

| Field | Type | Description |
|---|---|---|
| Netsuite account id | Text | Account id exactly as NetSuite shows it, including any `_SB1` sandbox suffix. The REST host is derived from it. |
| Oauth2 client id | Text | Client id from the integration record. |
| Netsuite certificate id | Text | Certificate id (`kid`) from the public-certificate upload. Not a secret. |
| Netsuite private certificate | Text (secret, multi-line) | The private-key PEM block. Stored encrypted; never returned. If the form can't hold a multi-line PEM in your build, set it via the MCP `connection_upsert` tool instead. |

## Create the Connection

Choose **NetSuite** (not the generic **REST** type) under **Tools > Connections > New Connection**, enter the four values above, and click `Create`. Only the NetSuite kind derives the host and auto-injects the SuiteQL headers and paging; a generic-REST connection would run unauthenticated. The step-by-step version is in the [connection guide](/guides/connections/netsuite/#create-the-connection).

## Pulling Data with SuiteQL

SuiteQL is the pull path — the record API returns only ids and links, not field values. Query it through a REST Request step:

- **Method** `POST`, **Endpoint** `/services/rest/query/v1/suiteql`.
- **Body** a single JSON object, `{"q": "SELECT ... FROM ... ORDER BY ..."}`.
- **`Prefer: transient`, `Content-Type: application/json`, and offset paging are injected by the connection** — do not hand-configure them. Paging is service-fixed, not form-adjustable.
- **A deterministic `ORDER BY` is required** on any paged query (e.g. `ORDER BY internalid`). Without it, offset paging silently duplicates and skips rows across pages — a financial mis-tie you won't see until you reconcile.
- **Define your columns with real types.** SuiteQL returns every value as a string; typed columns (Currency/Decimal, Date/Datetime, Boolean) tell PlaidCloud how to coerce them, and a blank value is read as empty.

> The SuiteQL response envelope (the `items` / `hasMore` paths) is built to the documented shape and confirmed at live cutover.

## Known Limitations

- **Schema auto-guess does not apply the connection's service config** — define the target columns and their types manually rather than relying on a guessed schema.
- **Paging is service-fixed** — the offset/limit and page size are set by the connector and are not form-adjustable.
- **Every pull is a full-table replace.** There is no incremental or delta path, so a scheduled pull re-extracts the whole result each run. Keep the `WHERE` clause to the slice you need — a rolling date window, for instance.
- **Multi-currency / subsidiary.** On `transaction`/`transactionline`, `amount` is in each transaction's own currency. A cross-subsidiary total over `amount` is consolidation-wrong — select consolidated or exchange-rate-converted fields when you total across subsidiaries.

## Related

- [Connect to NetSuite](/guides/connections/netsuite/) — the full walkthrough.
- [REST Request Step](/guides/workflows/rest-request-step/) — the step this pull is built on.
