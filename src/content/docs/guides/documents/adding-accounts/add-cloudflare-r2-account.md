---
title: Add Cloudflare R2 Account
description: Add a Cloudflare R2 storage account to PlaidCloud for importing and exporting data files using Cloudflare's zero-egress-fee object storage.
sidebar:
  order: 9
---

## Cloudflare R2 Setup

These steps need to be completed within the Cloudflare dashboard.

1. Sign in to the [Cloudflare dashboard](https://dash.cloudflare.com)
2. Select your account, then navigate to **R2 Object Storage** in the left sidebar
3. Create a bucket if one does not already exist. Note the bucket name.
4. Navigate to **R2 Object Storage > Manage R2 API Tokens**
5. Select **Create API Token**
6. Give the token a name, select the bucket(s) it should have access to, and choose **Object Read & Write** permissions
7. Select **Create API Token**
8. Copy the **Access Key ID** and **Secret Access Key**. Save both for the PlaidCloud Document setup below. The secret is only shown once.
9. Note the **S3 API endpoint** for your account. It follows the pattern `https://{account_id}.r2.cloudflarestorage.com` and is shown on the R2 overview page.

You should now have everything you need to add your Cloudflare R2 account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Cloudflare R2` as the Service Type
6. Fill in a name and description
7. Enter the **Start Path** as your R2 endpoint followed by the bucket name: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. The **Region** field can be set to `auto` or left blank — R2 automatically selects the closest region
9. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
10. Paste the **Access Key ID** into the Access Key ID field under Auth Credentials
11. Paste the **Secret Access Key** into the Secret Access Key field under Auth Credentials
12. Select the Save button and your new Document account is live
