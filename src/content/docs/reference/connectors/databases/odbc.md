---
title: ODBC
description: Set up an ODBC connection in PlaidCloud that reaches a database through a 64-bit System DSN on a PlaidLink agent's machine.
sidebar:
  order: 1
---

**ODBC (Open Database Connectivity)** reaches a database through a data source name (DSN) defined on the machine where a [PlaidLink agent](/reference/cli/plaidlink/) runs. Use it for a database that has no dedicated PlaidCloud connector, from agent steps such as [Agent Remote Export of SQL Result](/reference/workflow-steps/agent/agent-remote-export-of-sql-result/). To create one, choose **ODBC** as the connection type.

## Upstream Documentation
Each database's ODBC driver has its own settings. Refer to the driver vendor's documentation when you create the DSN.

## Create the DSN on the Agent's Machine

1. On the machine where the agent runs, open **ODBC Data Sources (64-bit)**.
2. On the **System DSN** tab, add a data source that uses the database's ODBC driver, and enter the server, database and any other settings the driver asks for.
3. Note the **Data Source Name**. You enter it in the connection.

:::caution
The DSN must be a 64-bit **System DSN**. The agent runs as a Windows service, which can't see a User DSN or a DSN created in the 32-bit ODBC administrator. The step then fails with `IM002 … Data source name not found and no default driver specified`.
:::

## Configuration

The DSN supplies the driver, server and database, so the connection has no fields for them.

### Database Connection

| Field | Required | Description |
|---|---|---|
| Data Source Name (DSN) | Yes | The name of the System DSN on the agent's machine. |

### Auth Credentials

| Field | Description |
|---|---|
| User | The user to connect as. |
| Use Single Sign-On Authentication (No Password, Optional User) | Connect without a stored password. |
| Password | The user's password (write-only). Leave it blank on edit to keep the saved password. |

### SSL Config and SSH Config

These tabs don't apply to an ODBC connection. Set encryption and other driver options in the DSN.

## Connections Saved by an Earlier Version

Earlier versions of this form required a **Database** and filled in a **Port**. A saved Database makes the connection bypass the DSN, and it fails with the same `IM002` error. Open the connection and save it: saving clears the Database and the Port.
