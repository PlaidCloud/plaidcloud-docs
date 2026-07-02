---
title: Add a Managed Bucket Account
description: Create a PlaidCloud-managed cloud storage bucket for Document with one form — no Google Cloud project, service account, or JSON key setup required.
sidebar:
  order: 2
---

A **Managed Bucket** is the fastest way to add cloud file storage to Document. Unlike the other providers, you don't create a bucket, a service account, or a key in a cloud console — PlaidCloud provisions a dedicated storage bucket and its credentials for you inside your own tenant's cloud project. You only choose a bucket name, a location, and a storage class.

Use a Managed Bucket when you want a new, isolated place to keep Document files and don't need to reuse an existing bucket you already own. To connect a bucket you manage yourself, use [Add Google Cloud Storage Account](/guides/documents/adding-accounts/add-google-cloud-storage-account/) instead.

## Setup

1. Sign into PlaidCloud
2. Select the workspace where the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Managed Bucket` as the Service Type
6. Fill in a name and an optional description
7. Enter a **Bucket Name**. Bucket names must be 3–63 characters, use only lowercase letters, digits, dots, hyphens, or underscores, and start and end with a letter or digit. The name is **globally unique across Google Cloud** — if it's already taken, you'll be asked to choose another
8. Choose a **Bucket Location** (defaults to `us-central1`). Multi-region options (`US`, `EU`, `Asia`) store data redundantly across a wide area; single regions keep it in one place
9. Choose a **Storage Class** (defaults to `Standard`). Use `Standard` for data you access often; `Nearline`, `Coldline`, and `Archive` cost less to store but more to read and suit progressively colder data
10. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure
11. Select the Save button

PlaidCloud provisions the bucket and a dedicated credential scoped to just that bucket, then creates the account with you as its owner. The account is ready to browse and upload to immediately.

:::note
Managed Buckets may be limited by your plan. If your plan doesn't include Managed Buckets, or you've reached your plan's limit, the form will tell you when you try to create one.
:::

## After Creation

- The bucket name is fixed once created — it can't be changed on an existing account.
- Deleting the account removes its dedicated credential but **leaves the bucket and its files in place**, so a deletion never destroys your data. Contact support if you need the underlying bucket removed.
- A Managed Bucket behaves like any other Document account for [access control](/guides/documents/account-management/control-document-account-access/), [ownership](/guides/documents/account-management/managing-document-account-owners/), and browsing.
