---
title: PlaidCloud Lakehouse
description: Configure the PlaidCloud Lakehouse database connection for high-performance querying and analytics on your lakehouse data.
sidebar:
  order: 1
---

## Upstream Documentation
There is very little configuration necessary for using the built-in PlaidCloud Lakehouse.  The documentation for the service is [here](https://docs.plaidcloud.com/docs/plaidcloud/analyze/dw/getting-started/).

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

### SSH tunnel

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

### Other

| Field | Type | Description |
|---|---|---|
| Server | Text | — |
| Lakehouse | Number | — |
