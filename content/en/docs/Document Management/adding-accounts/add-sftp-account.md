---
title: Add SFTP Account
slug: add-sftp-account
weight: 13.0
description: Add an SFTP (Secure File Transfer Protocol) account to PlaidCloud for importing and exporting data files using SSH-based file transfer.
date: 2026-04-08T00:00:00
---


## SFTP Server Setup

Ensure the following are available from your SFTP server administrator:

1. The **hostname or IP address** of the SFTP server
2. The **SSH port** (default is `22`)
3. A **username** with access to the target directory
4. Either a **password** or an **SSH private key** for authentication
5. Optionally, the **server's SSH host key fingerprint** for strict host verification

You should now have everything you need to add your SFTP account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Secure File Transfer (SFTP)` as the Service Type
6. Fill in a name and description
7. Enter the remote directory path into the **Start Path** field (e.g. `/data/uploads`)
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
9. Enter the **username** into the Public Key/User field under Auth Credentials
10. Enter the **password** into the Private Key/Password field under Auth Credentials
11. Navigate to the **SSH Config** tab
12. Enter the **Host or IP Address** of the SFTP server
13. Enter the **SSH Connection Port** (default `22`)
14. If using key-based authentication instead of a password, paste the **RSA Private Key** into the RSA Private Key field. When a private key is provided, it takes precedence over the password.
15. Optionally paste the **Remote Server RSA Fingerprint** for strict host key verification. Leave blank to auto-fill on first connection.
16. Select the Save button and your new Document account is live

{{< note >}}
You can test the SSH connection using the **Test SSH Connection** button on the SSH Config tab before saving.
{{< /note >}}
