---
title: Add Azure Blob Storage Account
description: Add an Azure Blob Storage account to PlaidCloud for importing and exporting data files using Microsoft Azure cloud object storage.
sidebar:
  order: 5
---

## Azure Blob Storage Setup

These steps need to be completed within the Azure portal.

1. Sign in to the [Azure portal](https://portal.azure.com)
2. Navigate to **Storage accounts** and select or create a storage account
3. In the left sidebar under **Security + networking**, select **Access keys**
4. Copy the **Storage account name** and one of the **Key** values. Save both for the PlaidCloud Document setup below.
5. Navigate to **Containers** under **Data storage** and create a container if one does not already exist. Note the container name.

You should now have everything you need to add your Azure Blob Storage account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Azure Blob Storage` as the Service Type
6. Fill in a name and description
7. Enter the container name and optional path prefix into the **Start Path** field (e.g. `my-container/data`). The first path segment is the container name.
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
9. Paste the **Storage account name** into the Account Name field under Auth Credentials
10. Paste the **Key** into the Account Key field under Auth Credentials
11. Select the Save button and your new Document account is live
