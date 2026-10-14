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

### BigQuery Connection

| Field | Required | Description |
|---|---|---|
| Project | Yes | The Google Cloud project that holds the dataset. |
| Dataset | Yes | The BigQuery dataset to read and write. |
| Table | Yes | A table in the dataset. |

### Auth Credentials

| Field | Required | Description |
|---|---|---|
| Service Account Key (JSON) | Yes | Paste the whole JSON key file of a Google service account that can read the dataset. Grant it write access only if you want to write to the dataset. The key is write-only: leave it blank on edit to keep the saved one. |

The connection authenticates only with the service account key you give it. [Import SQL](/reference/workflow-steps/import/import-sql/) reads BigQuery through this connection, and [Export External Database Tables](/reference/workflow-steps/export/export-external-tables/) writes to it with a BigQuery load job.
