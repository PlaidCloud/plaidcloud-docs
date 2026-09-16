---
title: Salesforce REST Connector
description: Set up a Salesforce REST API connection in PlaidCloud with the OAuth 2.0 client credentials flow, test it, and pull CRM objects into project tables with the Salesforce Query Object step.
sidebar:
  order: 1
---

## API Documentation

The [Salesforce REST API reference](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html) documents the record and metadata endpoints, and the [Bulk API 2.0 Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.api_asynch.meta/api_asynch/bulk_api_2_0.htm) documents the query jobs the [Salesforce: Query Object](/reference/workflow-steps/salesforce/query-salesforce-object/) step runs on.

For a start-to-finish walkthrough — the Salesforce-side app, the Run As user, creating the connection, and testing it — follow the [Connect to Salesforce](/guides/connections/salesforce/) guide. This page is the field reference behind it.

## How Authentication Works

The connector signs in with **OAuth 2.0 client credentials**: PlaidCloud exchanges the app's consumer key and secret for an access token at the org's own token endpoint, and calls the API as the user the app names in its **Run As** setting. There is no interactive login, no refresh token, and no certificate to manage.

Two properties of that exchange matter in practice:

- **One token covers a whole extract.** PlaidCloud caches the access token per connection and environment until shortly before it expires, so a large paged read does not re-authenticate on every page. A token that Salesforce stops honoring early — revoked, an IP restriction, a changed session policy — is discarded and replaced once, automatically.
- **Requests go where Salesforce says.** The token response names the org's instance, and every subsequent call is made against that instance rather than against the host you typed, so a connection keeps working after a My Domain or instance change.

The REST API version is pinned per connection rather than floating, so an org upgrade cannot silently change response shapes underneath a saved step. New connections use a currently supported version; a connection can be pinned to a different one through the connection configuration API, and if a pinned version reaches end of life Salesforce answers HTTP 410 and PlaidCloud reports which version was retired.

## Configuration

These fields appear when creating or editing a Salesforce connection in **Tools > Connections**.

### Account Description

| Field | Type | Description |
|---|---|---|
| Account Name | Text | Display name for this connection. |
| Memo | Text (multi-line) | Optional notes about the connection. |

### Connection

| Field | Type | Description |
|---|---|---|
| Host or IP Address | Text | The org's My Domain host — `mycompany.my.salesforce.com` for production and Developer Edition, `mycompany--uat.sandbox.my.salesforce.com` for a sandbox. PlaidCloud adds `https://` if you leave it off. |

### Auth Credentials

| Field | Type | Description |
|---|---|---|
| Client ID | Text | The app's consumer key. |
| Client Secret | Password | The app's consumer secret. Saved encrypted; type a new value to change it, leave it blank to keep the stored one. |

### Usage and Security

| Field | Type | Description |
|---|---|---|
| Active (Allow Access) | Toggle | Whether the connection can be used. Clear it to suspend access without deleting the connection. |
| Security Model | Select | Who can use the connection — private to its owners, specific members, specific security groups, or all workspace members. |

Each connection holds one set of these values per environment, so one connection can point at a sandbox in your development environment and at production in your production environment. Test and set credentials per environment.

## Test Connection

**Test Connection** performs the real token exchange and reports what the credentials authenticate as:

| Reported | Why it matters |
|---|---|
| Organization id | Confirms which org the credentials reach — the fastest way to catch a sandbox credential saved into a production environment. |
| API version | The highest version this org supports. Reads run on the version pinned to the connection — `v61.0` unless `salesforce_api_version` is set — not on this one. |
| Run As user | The user every row and field this connection ever returns is scoped to. Check this before trusting an extract's row counts. |

A failed test names the cause. Authentication failures report the HTTP status and prompt you to re-enter the client id and secret, because a client secret cannot be read back once saved.

## Known Limitations

- **The Run As user scopes every read, in two different ways.** Rows that user cannot see are simply absent, with no error and no count. A field that user cannot read fails the whole query. Both are covered in [The Run As User Scopes Everything](/guides/connections/salesforce/#the-run-as-user-scopes-everything).
- **Reads only.** This connector extracts data; it does not write records back to Salesforce.
- **Some field types cannot be extracted** — compound address and geolocation fields, `base64` blobs, `encryptedstring`, and `anyType`. The step's field picker marks each one and names the reason. See [Fields the Step Refuses](/reference/workflow-steps/salesforce/query-salesforce-object/#fields-the-step-refuses).
- **An extract is not a sync.** A record deleted in Salesforce stays in the target table.

## Related

- [Connect to Salesforce](/guides/connections/salesforce/) — step-by-step walkthrough
- [Salesforce: Query Object](/reference/workflow-steps/salesforce/query-salesforce-object/)
- [Create and Manage a Connection](/guides/connections/create-connection/)
