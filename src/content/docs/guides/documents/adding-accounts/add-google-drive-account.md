---
title: Add Google Drive Account
description: Add a Google Drive storage account to PlaidCloud for importing and exporting data files using Google Drive cloud storage.
sidebar:
  order: 12
---

## Google Drive Setup

These steps need to be completed within the Google Cloud Console to create a service account that PlaidCloud can use to access Google Drive.

### Create a Google Cloud Project

1. Sign in to the [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select an existing one

### Enable the Google Drive API

1. Navigate to **APIs & Services > Library**
2. Search for **Google Drive API**
3. Select it and click **Enable**

### Create a Service Account

1. Navigate to **APIs & Services > Credentials**
2. Select **+ Create Credentials > Service account**
3. Enter a name for the service account (e.g. `plaidcloud-drive`)
4. Select **Create and Continue**
5. Optionally grant roles (e.g. **Viewer** for read-only, or **Editor** for read/write). Select **Continue**.
6. Select **Done**

### Generate a Service Account Key

1. In the **Service Accounts** list, select the service account you just created
2. Navigate to the **Keys** tab
3. Select **Add Key > Create new key**
4. Choose **JSON** format and select **Create**
5. A JSON key file will download. Save this file securely — it contains the credentials PlaidCloud will use.

### Share Drive Content With the Service Account

1. Copy the service account's email address (e.g. `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. In Google Drive, share the folder(s) you want PlaidCloud to access with this email address, granting **Editor** access. To use a Shared Drive, add the service account as a member of it instead.

You should now have everything you need to add your Google Drive account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage`
4. Select the **New Account** button
5. Select `Google Drive` as the Service Type
6. Fill in a name and description
7. Enter the shared folder path into the **Start Path** field, or leave it blank to access all shared content
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
9. Paste the entire contents of the JSON key file into the OAuth2 Credentials JSON field under Auth Credentials
10. Select the Save button and your new Document account is live

## Using the Account in Workflows

A Google Drive account works in workflows as well as in the Document browser. Steps can list, import, export, copy, move, rename and delete files and create folders.

- **Locations.** The account's top-level locations are the folders shared with the service account and the Shared Drives it is a member of. Paths are folder names, such as `Finance/Reports/2026`. If two shared folders or Shared Drives have the same name, the account refuses to open that name. Rename or unshare all but one.
- **Google Sheets.** A Google Sheet reads as an `.xlsx` export and appears as `Name.xlsx`. Other Google Workspace files, such as Docs and Slides, can't be read.
- **New files in My Drive.** A service account has no storage of its own, so in a folder that lives in someone's personal My Drive it can overwrite an existing file but can't create a new one. Create the file there first, or use a folder in a Shared Drive, which accepts new files and folders.
- **Missing folders.** A folder that doesn't exist lists as empty instead of causing an error.
- **Throttling.** PlaidCloud retries automatically when Google throttles a request or returns a temporary error.
