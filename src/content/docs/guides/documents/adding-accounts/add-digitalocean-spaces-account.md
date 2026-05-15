---
title: Add DigitalOcean Spaces Account
description: Add a DigitalOcean Spaces storage account to PlaidCloud for importing and exporting data files using DigitalOcean's S3-compatible object storage.
sidebar:
  order: 10
---

## Digitalocean Spaces Setup

These steps need to be completed within the DigitalOcean control panel.

1. Sign in to the [DigitalOcean Control Panel](https://cloud.digitalocean.com)
2. Navigate to **Spaces Object Storage** in the left sidebar
3. Create a Space if one does not already exist. Note the Space name and region (e.g. `nyc3`).
4. Navigate to **API > Spaces Keys** (under the Tokens section)
5. Select **Generate New Key**
6. Give the key a name
7. Copy the **Key** (Access Key) and **Secret**. Save both for the PlaidCloud Document setup below. The secret is only shown once.
8. Note the endpoint URL for your Space's region. It follows the pattern `https://{region}.digitaloceanspaces.com` (e.g. `https://nyc3.digitaloceanspaces.com`)

You should now have everything you need to add your DigitalOcean Spaces account to PlaidCloud Document.


## PlaidCloud Document Setup

1. Sign into PlaidCloud
2. Select the workspace that the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `DigitalOcean Spaces` as the Service Type
6. Fill in a name and description
7. Enter the **Start Path** as the endpoint URL followed by the Space name: `https://nyc3.digitaloceanspaces.com/my-space`
8. Enter the **Region** (e.g. `nyc3`, `sfo3`, `ams3`)
9. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure.
10. Paste the **Key** into the Access Key ID field under Auth Credentials
11. Paste the **Secret** into the Secret Access Key field under Auth Credentials
12. Select the Save button and your new Document account is live
