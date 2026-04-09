---
title: Add Backblaze B2 Account
slug: add-backblaze-b2-account
weight: 8.0
description: Add a Backblaze B2 storage account to PlaidCloud for importing and exporting data files using affordable cloud object storage.
date: 2026-04-08T00:00:00
---


## Backblaze B2 Setup

These steps need to be completed within the Backblaze B2 console.

1. Sign in to the [Backblaze B2 console](https://secure.backblaze.com/b2_buckets.htm)
2. Navigate to **Buckets** and create a bucket if one does not already exist. Note the bucket name.
3. Navigate to **App Keys**
4. Select **Add a New Application Key**
5. Give the key a name, select the bucket it should have access to, and choose the appropriate permissions (read and write)
6. Select **Create New Key**
7. Copy the **keyID** (this is your Access Key) and **applicationKey** (this is your Secret Key). Save both for the PlaidCloud Document setup below. The application key is only shown once.
8. Note the **S3 Endpoint** for your bucket's region. It follows the pattern `https://s3.{region}.backblazeb2.com` (e.g. `https://s3.us-west-004.backblazeb2.com`). This can be found on the bucket details page.

You should now have everything you need to add your Backblaze B2 account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Backblaze B2` as the Service Type
6. Fill in a name and description
7. Enter the **Start Path** as your S3-compatible endpoint followed by the bucket name: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Enter the **Region** for your bucket (e.g. `us-west-004`)
9. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
10. Paste the **keyID** into the Access Key ID field under Auth Credentials
11. Paste the **applicationKey** into the Secret Access Key field under Auth Credentials
12. Select the Save button and your new Document account is live
