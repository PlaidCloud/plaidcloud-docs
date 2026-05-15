---
title: Google BigQuery Connector
description: Configure a Google BigQuery connection in PlaidCloud to run analytical queries and integrate large-scale data into workflows.
sidebar:
  order: 1
---

## Connection Documentation
[The Google BigQuery documentation](https://docs.cloud.google.com/bigquery/docs).

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

### Connection

| Field | Type | Description |
|---|---|---|
| Db project | Text | — |
| Db dataset | Text | — |
| Db catalog | Text | Database, catalog, or schema to connect to. |

### Authentication

| Field | Type | Description |
|---|---|---|
| Db user | Text | Username for database authentication. |
| Db password | Password | Password for database authentication. |
