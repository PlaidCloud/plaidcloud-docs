---
title: Microsoft Dynamics 365 REST Connector
description: Configure a Microsoft Dynamics REST API connection in PlaidCloud to integrate ERP and CRM data into your analysis workflows.
sidebar:
  order: 1
---

## API Documentation
The [vendor API reference](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) covers this connector\'s endpoints.

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
| Dynamics tenant | Text | — |
| Oauth2 client id | Text | — |
| Oauth2 client secret | Text | Secret credential — stored encrypted. |
| Dynamics crm | Text | — |
