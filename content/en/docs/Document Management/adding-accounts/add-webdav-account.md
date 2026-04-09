---
title: Add WebDAV Account
slug: add-webdav-account
weight: 14.0
description: Add a WebDAV storage account to PlaidCloud for importing and exporting data files using WebDAV-compatible servers such as Nextcloud, ownCloud, or Apache.
date: 2026-04-08T00:00:00
---


## WebDAV Server Setup

Ensure the following are available from your WebDAV server administrator:

1. The **WebDAV endpoint URL** (e.g. `https://nextcloud.yourcompany.com/remote.php/dav/files/username/`)
2. A **username** with access to the target directory
3. A **password** or app-specific password for authentication

{{< note >}}
Many cloud services expose a WebDAV interface. For example, Nextcloud uses `https://your-server/remote.php/dav/files/{username}/` and ownCloud uses `https://your-server/remote.php/webdav/`. Check your provider's documentation for the correct URL.
{{< /note >}}

You should now have everything you need to add your WebDAV account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `WebDAV` as the Service Type
6. Fill in a name and description
7. Enter the full **WebDAV endpoint URL** into the **Start Path** field (e.g. `https://nextcloud.yourcompany.com/remote.php/dav/files/username/`)
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
9. Enter the **username** into the Username field under Auth Credentials
10. Enter the **password** into the Password field under Auth Credentials
11. Select the Save button and your new Document account is live
