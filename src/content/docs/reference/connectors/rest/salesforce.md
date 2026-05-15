---
title: Salesforce REST Connector
description: Set up a Salesforce REST API connection in PlaidCloud to integrate CRM, sales, and customer data into your analysis workflows.
sidebar:
  order: 1
---

## API Documentation
The API documentation is for this connector is located [here](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_what_is_rest_api.html).

## Configuration

These fields appear when creating or editing this connection. Required vs optional depends on the authentication options you enable.

### Identification

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Alias | Text (multi-line) | Optional alias or notes about the connection. |
| Is active | Toggle | Whether the connection is enabled. Disable to pause without deleting. |
| Access type | Select | Read-only, write-only, or read-write access level for this connection. |

### Authentication

| Field | Type | Description |
|---|---|---|
| Client id | Text | OAuth client ID issued by the provider. |
| Client secret | Password | OAuth client secret issued by the provider. |

### Other

| Field | Type | Description |
|---|---|---|
| Host | Text | — |
