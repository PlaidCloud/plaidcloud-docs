---
title: Add Azure Data Lake Gen2 Account
description: Add an Azure Data Lake Storage Gen2 account to PlaidCloud for importing and exporting data files using hierarchical namespace storage on Azure.
sidebar:
  order: 6
---

## Azure Data Lake Gen2 Setup

Azure Data Lake Storage Gen2 is built on top of Azure Blob Storage with a hierarchical namespace enabled. These steps need to be completed within the Azure portal.

1. Sign in to the [Azure portal](https://portal.azure.com)
2. Navigate to **Storage accounts** and select or create a storage account that has **Hierarchical namespace** enabled
3. In the left sidebar under **Security + networking**, select **Access keys**
4. Copy the **Storage account name** and one of the **Key** values. Save both for the PlaidCloud Document setup below.
5. Navigate to **Containers** under **Data storage** and create a filesystem (container) if one does not already exist. Note the filesystem name.

You should now have everything you need to add your Azure Data Lake Gen2 account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Azure Data Lake Gen2` as the Service Type
6. Fill in a name and description
7. Enter the filesystem name and optional path prefix into the **Start Path** field (e.g. `my-filesystem/data`). The first path segment is the filesystem name.
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
9. Paste the **Storage account name** into the Account Name field under Auth Credentials
10. Paste the **Key** into the Account Key field under Auth Credentials
11. Select the Save button and your new Document account is live
