---
title: Workday REST Connector
description: Configure a Workday REST API connection in PlaidCloud to integrate HR, finance, and planning data into your workflows.
sidebar:
  order: 1
---

## API Documentation
The [vendor API reference](https://community.workday.com/sites/default/files/file-hosting/restapi/) covers this connector\'s endpoints.

## Configuration

These fields appear when creating or editing this connection. Required vs optional depends on the authentication options you enable.

### Identification

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Alias | Text (multi-line) | Optional alias or notes about the connection. |
| Is active | Toggle | Whether the connection is enabled. Disable to pause without deleting. |
| Db read only | Toggle | Restrict the connection to read-only operations. |
| Access type | Select | Read-only, write-only, or read-write access level for this connection. |

### Other

| Field | Type | Description |
|---|---|---|
| Oauth2 client id | Text | — |
| Oauth2 client secret | Text | Secret credential — stored encrypted. |
| Workday url | Text | URL endpoint. |
| Oauth2 refresh token | Text | — |
