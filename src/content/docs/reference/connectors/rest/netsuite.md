---
title: Netsuite REST Connector
description: Set up a NetSuite REST API connection in PlaidCloud to integrate ERP, financial, and e-commerce data into your workflows.
sidebar:
  order: 1
---

## API Documentation
The API documentation is for this connector is located [here](https://system.netsuite.com/help/helpcenter/en_US/APIs/REST_API_Browser/record/v1/2023.1/index.html).

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
| Netsuite certificate id | Text | — |
| Netsuite account id | Text | — |
| Netsuite private certificate | Text | — |
