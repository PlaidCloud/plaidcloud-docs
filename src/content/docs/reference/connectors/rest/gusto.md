---
title: Gusto REST Connector
description: Set up a Gusto REST API connection in PlaidCloud to integrate payroll, benefits, and HR data into your analysis workflows.
sidebar:
  order: 1
---

## API Documentation
The API documentation is for this connector is located [here](https://docs.gusto.com/app-integrations/reference/get-v1-token-info).

## Configuration

These fields appear when creating or editing this connection. Required vs optional depends on the authentication options you enable.

### Identification

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Alias | Text (multi-line) | Optional alias or notes about the connection. |
| Is active | Toggle | Whether the connection is enabled. Disable to pause without deleting. |

### Other

| Field | Type | Description |
|---|---|---|
| Host | Text | — |
| Auth type | Select | — |
| Enable ssl verification | Toggle | — |
| Follow redirects | Toggle | — |
| Redirect follow http | Toggle | — |
| Redirect follow auth | Toggle | — |
| Redirect remove referer | Toggle | — |
| Strict http | Toggle | — |
| Encode url | Toggle | URL endpoint. |
| Disable cookie jar | Toggle | — |
| Server cipher | Toggle | — |
| Max redirects | Number | — |
| Test endpoint | Text | — |
| Test method | Select | — |
