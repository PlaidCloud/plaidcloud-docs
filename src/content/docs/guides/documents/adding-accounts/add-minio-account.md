---
title: Add MinIO Account
description: Add a MinIO storage account to PlaidCloud for importing and exporting data files using self-hosted S3-compatible object storage.
sidebar:
  order: 7
---

## MinIO Setup

These steps need to be completed within the MinIO Console or via the `mc` CLI.

1. Sign in to the MinIO Console (e.g. `https://your-minio-host:9001`)
2. Navigate to **Buckets** and create a bucket if one does not already exist. Note the bucket name.
3. Navigate to **Identity > Users** (or **Access Keys**)
4. Create a new user or service account with read/write access to the target bucket
5. Copy the **Access Key** and **Secret Key** generated for the user. Save both for the PlaidCloud Document setup below.
6. Note the MinIO endpoint URL (e.g. `https://play.min.io` or `https://minio.yourcompany.com`)

You should now have everything you need to add your MinIO account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `MinIO` as the Service Type
6. Fill in a name and description
7. Enter the **Start Path** as your MinIO endpoint URL followed by the bucket name and optional prefix: `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. Enter the **Region** if your MinIO deployment uses regions; otherwise leave blank
9. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
10. Paste the **Access Key** into the Access Key ID field under Auth Credentials
11. Paste the **Secret Key** into the Secret Access Key field under Auth Credentials
12. Select the Save button and your new Document account is live
