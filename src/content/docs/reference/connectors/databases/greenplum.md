---
title: Greenplum
description: Set up a Greenplum database connection in PlaidCloud to query, import, and export data with your Greenplum data warehouse.
sidebar:
  order: 1
---

**Greenplum** is a massively parallel PostgreSQL-derived analytical database (originally Pivotal, now VMware Tanzu). Use this connector to read and write Greenplum tables from PlaidCloud workflows. The wire protocol is PostgreSQL-compatible, so most PostgreSQL tooling considerations apply.

## Upstream Documentation
[The Greenplum documentation](https://techdocs.broadcom.com/us/en/vmware-tanzu/data-solutions/tanzu-greenplum/7/greenplum-database/landing-index.html).

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
