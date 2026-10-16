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

Set up the DSN on the machine where the agent runs, as a system DSN, so that the agent finds it whichever account it runs as.

### On Windows

1. Open **ODBC Data Sources (64-bit)**.
2. On the **System DSN** tab, add a data source that uses the database's ODBC driver, and enter the server, database and any other settings the driver asks for.
3. Note the **Data Source Name**. You enter it in the connection.

:::caution
The DSN must be a 64-bit **System DSN**. On Windows the agent runs as a service, which can't see a User DSN or a DSN created in the 32-bit ODBC administrator. The step then fails with `ODBC data source '<name>' is not defined on the agent machine`.
:::

### On Linux

On Linux the agent reaches ODBC through unixODBC.

1. Install unixODBC and the database's ODBC driver.
2. Check that the driver is registered in `odbcinst.ini`, under its name in square brackets. Most driver packages register themselves when installed, and `odbcinst -q -d` lists the registered drivers.
3. Add the data source to the system `odbc.ini`, as a section named for the DSN. Set `Driver` to the registered driver name, and add the server, database and any other settings the driver asks for:

   ```ini
   [Sales]
   Driver=ODBC Driver 18 for SQL Server
   Server=sales-db.example.com
   Database=Sales
   ```

4. Note the section name, `Sales` here. You enter it in the connection.

`odbcinst -j` shows where the system `odbcinst.ini` and `odbc.ini` are, usually `/etc`. A DSN in a user's own `~/.odbc.ini` is found only when the agent runs as that user.

### In a Container

The PlaidLink container image includes unixODBC but no ODBC driver. To use ODBC from an agent running in Docker or Kubernetes, build an image from it that installs the driver, and add the system `odbc.ini` with the DSN to the image or mount it into the container. The image runs as the `plaid` user, so switch to `root` to install the driver and back to `plaid` afterwards.

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
