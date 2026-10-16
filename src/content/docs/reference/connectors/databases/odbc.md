---
title: ODBC
description: Set up an ODBC connection in PlaidCloud through a 64-bit System DSN or an ODBC driver installed on a PlaidLink agent's machine.
sidebar:
  order: 1
---

**ODBC (Open Database Connectivity)** reaches a database through the ODBC setup on the machine where a [PlaidLink agent](/reference/cli/plaidlink/) runs. Use it for a database that has no dedicated PlaidCloud connector, from agent steps such as [Agent Remote Export of SQL Result](/reference/workflow-steps/agent/agent-remote-export-of-sql-result/). To create one, choose **ODBC** as the connection type.

An ODBC connection works one of two ways:

- **Through a DSN.** Leave **ODBC Driver** blank and name a data source (DSN) set up on the agent's machine. The DSN holds the driver, server, database and any other driver settings, and **Connection Attributes** can override them. This works with any ODBC driver.
- **Through a driver.** Choose or type an **ODBC Driver** installed on the agent's machine, then give the server and database. PlaidCloud passes the driver a `Server` and a `Database` setting, followed by any **Connection Attributes**, so this suits drivers that take the server and database that way, such as Microsoft's SQL Server drivers, PostgreSQL, MySQL and MariaDB. For a driver that names them differently, use a DSN.

## Upstream Documentation
Each database's ODBC driver has its own settings. Refer to the driver vendor's documentation for the keywords it accepts, both when you create a DSN and when you write connection attributes.

## Create the DSN on the Agent's Machine

1. On the machine where the agent runs, open **ODBC Data Sources (64-bit)**.
2. On the **System DSN** tab, add a data source that uses the database's ODBC driver, and enter the server, database and any other settings the driver asks for.
3. Note the **Data Source Name**. You enter it in the connection.

:::caution
The DSN must be a 64-bit **System DSN**. The agent runs as a Windows service, which can't see a User DSN or a DSN created in the 32-bit ODBC administrator. The step then fails with `IM002 … Data source name not found and no default driver specified`.
:::

## Configuration

### Database Connection

| Field | Required | Description |
|---|---|---|
| ODBC Driver | No | Leave blank to connect through a DSN. Otherwise, the name of an ODBC driver installed on the agent's machine, exactly as **ODBC Data Sources (64-bit)** lists it on its **Drivers** tab. The list offers common drivers, and you can type any other. A driver name can't contain braces or semicolons. |
| Data Source Name (DSN) or Server | Yes | Without a driver, the name of the System DSN on the agent's machine. With a driver, the database server's host name, or `host,port` for SQL Server on a non-default port. |
| Database | With a driver | The database to open. It is unavailable without a driver, because the DSN names its own, and saving refuses a database without a driver. |
| Connection Attributes | No | Other settings for the driver, as `KEY=value` pairs separated by `;`. See [Connection Attributes](#connection-attributes). |

The connection has no port field. For SQL Server on a non-default port, add it to the server as `host,port`, because Microsoft's SQL Server drivers take no port keyword. For another driver that takes one, give it as an attribute, such as `PORT=5433`. With a DSN, set the port in the DSN.

### Connection Attributes

**Connection Attributes** passes ODBC settings to the driver in either mode, written the way ODBC writes them:

- With a driver, they follow the server and database. Use them for whatever else the driver needs, such as `PORT=5433` for a driver that takes a port.
- With a DSN, they override the DSN's own settings, such as `DBQ=MYLIB`.

Separate pairs with `;`, as in `PORT=5433;SSLMODE=require`. Wrap a value that contains `;` in braces, as in `KEY={first;second}`, and inside braces write `}` as `}}`. Keywords reach the driver in upper case; ODBC keywords don't depend on case.

Saving refuses:

- text that isn't `KEY=value` pairs, including a brace that is never closed and a keyword with no value;
- a keyword given more than once, in any case;
- a keyword the connection sets from its own fields: `DRIVER`, `DSN`, `SERVER`, `DATABASE`, `UID`, `PWD`, `USER`, `USERID`, `USERNAME` and `PASSWORD`.

Connection lists mask the attributes, because a driver can take its own credential keyword there; the connection's own form shows them. Clear the field to remove them. Enter the user and password under **Auth Credentials**.

:::note
**ODBC Driver 18 for SQL Server** encrypts the connection and checks the server's certificate by default. For a server with a self-signed certificate, add `TrustServerCertificate=yes` to the attributes.
:::

### Auth Credentials

| Field | Description |
|---|---|
| User | The user to connect as. |
| Use Single Sign-On Authentication (No Password, Optional User) | Connect without a stored password. |
| Password | The user's password (write-only). Leave it blank on edit to keep the saved password. |

### SSL Config and SSH Config

These tabs don't apply to an ODBC connection. Set encryption and other driver options in the DSN or the connection attributes.

## Connections Saved by an Earlier Version

Earlier versions of this form required a **Database** and a driver chosen from a fixed list, and filled in a **Port**, but never passed the driver on, so those connections couldn't connect. Open the connection and either:

- **Connect through a DSN:** clear **ODBC Driver**, enter the DSN, and save. Saving clears the old Database.
- **Connect through a driver:** check that **ODBC Driver** matches a driver installed on the agent's machine. Many names in the old list weren't the names drivers register under.

A connection that keeps a driver from the old list opens as a driver connection, and fails to connect until the driver is one installed on the agent's machine.

Saving also clears the old Port. A connection that only ever had a DSN, with no Database, opens with **ODBC Driver** blank.
