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
2. In Google Drive, share the folder(s) you want PlaidCloud to access with this email address, granting **Editor** access

You should now have everything you need to add your Google Drive account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Google Drive` as the Service Type
6. Fill in a name and description
7. Enter the shared folder path into the **Start Path** field, or leave it blank to access all shared content
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
9. Paste the entire contents of the JSON key file into the OAuth2 Credentials JSON field under Auth Credentials
10. Select the Save button and your new Document account is live
