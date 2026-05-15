---
title: Exasol
description: Configure an Exasol database connection in PlaidCloud to run high-performance analytical queries and integrate your data.
sidebar:
  order: 1
---

**Exasol** is an in-memory analytical database optimized for fast SQL over large datasets. Use this connector to read and write Exasol tables from PlaidCloud workflows. Connection uses standard username/password authentication with optional SSL.

## Upstream Documentation
Exasol documentation is [here](https://docs.exasol.com/home.htm).

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
| Db host | Text | Hostname or IP address of the database server. |
| Db port | Number | Port number for the database connection. |
| Db catalog | Text | Database, catalog, or schema to connect to. |

### Authentication

| Field | Type | Description |
|---|---|---|
| Db user | Text | Username for database authentication. |
| Use sso | Toggle | Authenticate via single sign-on instead of username/password. |
| Db password | Password | Password for database authentication. |

### SSL / TLS

| Field | Type | Description |
|---|---|---|
| Use ssl | Toggle | Encrypt the connection with SSL/TLS. |
| Ssl mode | Select | SSL verification mode (e.g., disable, require, verify-ca, verify-full). |
| Ssl auth client cert | Text (multi-line) | Client certificate (PEM) for mutual TLS authentication. |
| Ssl auth client key | Text (multi-line) | Client private key (PEM) for mutual TLS authentication. |
| Ssl auth root cert | Text (multi-line) | Root CA certificate (PEM) for verifying the server's cert. |
| Ssl auth cert revoke | Text (multi-line) | Certificate revocation list, if your environment uses one. |

### SSH Tunnel

| Field | Type | Description |
|---|---|---|
| Use ssh | Toggle | Tunnel the connection through an SSH bastion. |
| Ssh host | Text | SSH bastion hostname. |
| Ssh port | Number | SSH bastion port (default 22). |
| Ssh user | Text | SSH bastion username. |
| Ssh password | Password | SSH bastion password (if password auth is used). |
| Use ssh cert | Toggle | Authenticate to the SSH bastion with a private key instead of password. |
| Ssh private key | Text (multi-line) | SSH private key (PEM) for bastion authentication. |
| Ssh host key | Text (multi-line) | Expected SSH host key for bastion fingerprint verification. |
