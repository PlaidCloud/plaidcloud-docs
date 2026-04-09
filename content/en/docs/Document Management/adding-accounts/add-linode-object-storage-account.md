---
title: Add Linode Object Storage Account
slug: add-linode-object-storage-account
weight: 11.0
description: Add a Linode (Akamai) Object Storage account to PlaidCloud for importing and exporting data files using Linode's S3-compatible cloud storage.
date: 2026-04-08T00:00:00
---


## Linode Object Storage Setup

These steps need to be completed within the Linode Cloud Manager.

1. Sign in to the [Linode Cloud Manager](https://cloud.linode.com)
2. Navigate to **Object Storage** in the left sidebar
3. Create a bucket if one does not already exist. Note the bucket name (called **label**) and region (e.g. `us-east-1`).
4. Navigate to **Object Storage > Access Keys**
5. Select **Create Access Key**
6. Give the key a label and select the bucket(s) it should have access to with read/write permissions
7. Select **Create Access Key**
8. Copy the **Access Key** and **Secret Key**. Save both for the PlaidCloud Document setup below. The secret is only shown once.
9. Note the endpoint URL for your bucket's region. It follows the pattern `https://{region}.linodeobjects.com` (e.g. `https://us-east-1.linodeobjects.com`)

You should now have everything you need to add your Linode Object Storage account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Linode Object Storage` as the Service Type
6. Fill in a name and description
7. Enter the **Start Path** as the endpoint URL followed by the bucket name: `https://us-east-1.linodeobjects.com/my-bucket`
8. Enter the **Region** (e.g. `us-east-1`)
9. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
10. Paste the **Access Key** into the Access Key ID field under Auth Credentials
11. Paste the **Secret Key** into the Secret Access Key field under Auth Credentials
12. Select the Save button and your new Document account is live
