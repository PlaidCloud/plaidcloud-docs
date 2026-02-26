---
title: Add OneDrive Account
slug: add-onedrive-account
weight: 4.0
description: How to add a Microsoft OneDrive account to Document
date: 2024-01-01T00:00:00
---


## OneDrive Setup

These steps need to be completed within the Azure portal to register an application and obtain the credentials PlaidCloud needs to access OneDrive.

### Register an Application in Azure

1. Sign in to the [Azure portal](https://portal.azure.com) and navigate to **Microsoft Entra ID**.
2. In the left sidebar, select **App registrations**.
3. Click **+ New registration**.
4. Enter a name for the application (e.g., `PlaidCloud`).
5. Under **Supported account types**, select the option that matches your organization:
   - **Accounts in this organizational directory only** — for a single-tenant setup (most common)
   - **Accounts in any organizational directory** — for multi-tenant access
6. Leave the **Redirect URI** blank.
7. Click **Register**.

### Copy the Client ID

After registration, you will land on the application overview page.

1. Copy the **Application (client) ID** — this is your **Client ID**. Save it for the PlaidCloud Document setup below.

### Create a Client Secret

1. In the left sidebar, select **Certificates & secrets** under **Manage**.
2. Click **+ New client secret**.
3. Enter a description (e.g., `PlaidCloud`) and choose an expiration period.
4. Click **Add**.
5. Copy the **Value** of the newly created secret immediately — this is your **Client Secret**. It will not be shown again after you leave this page.

### Grant API Permissions

1. In the left sidebar, select **API permissions** under **Manage**.
2. Click **+ Add a permission**.
3. Select **Microsoft Graph**.
4. Select **Delegated permissions** or **Application permissions** depending on your access model:
   - Use **Application permissions** for unattended/service access (most common for PlaidCloud Document)
5. Search for and select the following permissions:
   - `Files.Read.All` — to read files and folders
   - `Files.ReadWrite.All` — if PlaidCloud Document needs to write files
   - `Sites.Read.All` — if accessing SharePoint-backed OneDrive for Business libraries
6. Click **Add permissions**.
7. Click **Grant admin consent for [your organization]** and confirm.

---

### Find the OneDrive Drive Path (Start Path)

The **Start Path** in PlaidCloud Document controls which folder in OneDrive is used as the root for the account. To find the correct path:

1. Open [OneDrive](https://onedrive.live.com) or your organization's SharePoint-based OneDrive for Business in a browser.
2. Navigate to the folder you want to use as the root for this PlaidCloud Document account.
3. The path shown in the browser's address bar or the folder breadcrumb reflects the folder hierarchy within OneDrive.
4. Use the relative path from the root of the drive as the **Start Path** — for example, `/Documents/Finance` or `/Shared/Data`.

{{< note >}}
To use the entire OneDrive as the root, leave the Start Path blank. To restrict PlaidCloud Document to a specific folder and its contents, enter the path to that folder.
{{< /note >}}

---

You should now have everything you need to add your OneDrive account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `OneDrive` as the Service Type
6. Fill in a name and description
7. Enter the folder path identified above into the **Start Path** field, or leave it blank to use the root of the drive
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
9. Paste the **Client ID** copied from the Azure app registration into the Public Key/User text field under Auth Credentials
10. Paste the **Client Secret** copied from the Azure app registration into the Private Key/Password text field under Auth Credentials
11. Select the Save button and your new Document account is live
