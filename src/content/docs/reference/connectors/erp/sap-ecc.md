---
title: SAP ECC Connector
description: Configure an SAP ECC ERP connection in PlaidCloud to integrate financial, logistics, and operational data into your workflows.
sidebar:
  order: 1
---

## Upstream Documentation
SAP has removed all ECC documentation and currently only provides documentation for [S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE).

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
| Client | Text | — |
| Lang | Select | — |
| Trace | Select | — |
| Ashost | Text | — |
| Sysnr | Text | — |
| Mshost | Text | — |
| Msserv | Text | — |
| Sysid | Text | — |
| Group | Text | — |
| User | Text | — |
| Passwd | Password | — |
