---
title: SAP ECC and S/4HANA Connector
description: Configure the SAP ECC / S/4HANA connection in PlaidCloud to integrate financial, logistics, and operational SAP data into your workflows over RFC.
sidebar:
  order: 1
  label: SAP ECC / S/4HANA
---

One connection type covers both SAP ECC and SAP S/4HANA. Both are reached the same way — Remote Function Calls against the application server — so PlaidCloud does not ask you which generation you are on. In the **Connections** screen, choose **New → SAP ECC / S/4HANA Instance**.

The [SAP workflow steps](/reference/workflow-steps/sap/) all run against a connection of this type.

## Upstream Documentation

SAP has removed all ECC documentation and currently only provides documentation for [S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE). The RFC interfaces PlaidCloud uses are common to both.

## Configuration

These fields appear when creating or editing the connection.

### Account Description

| Field | Type | Description |
|---|---|---|
| Account Name | Text | Display name for this connection, shown wherever a step picks a connection. Required. |
| Memo | Text (multi-line) | Optional notes about the connection — which system it points at, who owns it. |

### SAP Environment

| Field | Type | Description |
|---|---|---|
| Client | Text | SAP client number, e.g. `100`. Required. |
| Language | Select | Logon language as a two-letter SAP code. Defaults to `EN`. Required. |
| Trace Level | Select | RFC trace verbosity — Off, Brief, Verbose, or Full. Leave at Off unless you are diagnosing a connection problem. Required. |
| Connection type | Radio | **Use Single Direct Connection** to reach one application server, or **Use Load Balanced Multi-System Connection** to go through a message server. The fields below activate according to this choice. |

Choosing **Use Single Direct Connection** enables:

| Field | Type | Description |
|---|---|---|
| Host | Text | Hostname or IP address of the application server. |
| System Number | Text | Two-digit SAP system number, e.g. `00`. |

Choosing **Use Load Balanced Multi-System Connection** enables:

| Field | Type | Description |
|---|---|---|
| MS Host | Text | Hostname or IP address of the message server. |
| MS Server | Text | Message server port or service name. |
| System ID | Text | Three-character SAP system ID, e.g. `PRD`. |
| Group | Text | Logon group to balance across, e.g. `PUBLIC`. |

### Auth Credentials

| Field | Type | Description |
|---|---|---|
| User | Text | SAP logon user for the RFC calls. Required. |
| Password | Password | Password for that user. Write-only — leave it blank when editing to keep the stored password. |

### Usage

| Field | Type | Description |
|---|---|---|
| Active (Allow Access) | Toggle | Whether the connection can be used. Clear it to pause the connection without deleting it. |
| Read Only | Toggle | Restrict the connection to read operations. |

### Security Model

| Field | Type | Description |
|---|---|---|
| Security Model | Select | Who may use this connection — Private (Only Owners), Specific Members Only, Specific Security Groups Only, or All Workspace Members. |

## Testing the Connection

**Test Connection** on the connection window logs on with the details above and reports back. When you edit an existing connection and change any setting, retype the password before testing — the stored one is not sent alongside edited values.
