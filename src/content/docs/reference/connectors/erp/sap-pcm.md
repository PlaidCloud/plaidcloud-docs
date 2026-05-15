---
title: SAP Profitability and Cost Management (PCM) Connector
description: Configure an SAP Profitability and Cost Management connection in PlaidCloud to integrate cost allocation data into workflows.
sidebar:
  order: 1
---

## Upstream Documentation
The SAP PCM legacy documentation is [here](https://help.sap.com/docs/SAP_PROFITABILITY_AND_COST_MANAGEMENT).

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

### Authentication

| Field | Type | Description |
|---|---|---|
| Db user | Text | Username for database authentication. |
| Use sso | Toggle | Authenticate via single sign-on instead of username/password. |
| Db password | Password | Password for database authentication. |
