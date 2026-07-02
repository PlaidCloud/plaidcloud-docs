---
title: Add a Managed Bucket Account
description: Add fully managed file storage to PlaidCloud Document in one step — pick a name and PlaidCloud sets everything up for you, with nothing to configure.
sidebar:
  order: 2
---

A **Managed Bucket** is the fastest way to add file storage to Document. PlaidCloud creates and runs the storage for you — there's nothing to set up beforehand and no credentials to manage. You just give it a name.

Use a Managed Bucket when you want a new, self-contained place to keep Document files. To connect storage you already own and manage yourself, pick one of the other providers on the [Adding New Document Accounts](/guides/documents/adding-accounts/) page instead.

## Setup

1. Sign into PlaidCloud
2. Select the workspace where the new Document account will reside
3. Go to `Document > Manage Accounts`
4. Select the `+ New Account` button
5. Select `Managed Bucket` as the Service Type
6. Fill in a name and an optional description
7. Enter a **Bucket Name**. Names must be 3–63 characters, use only lowercase letters, digits, dots, or hyphens, and start and end with a letter or digit. The name must be **globally unique** — if it's already in use, you'll be asked to choose another
8. Select an appropriate **Security Model** for your use case. Leave it `Private` if unsure
9. Select the Save button

PlaidCloud sets up the storage and makes you its owner. The account is ready to browse and upload to immediately — there's nothing else to configure. Storage costs are optimized for you automatically based on how often your files are accessed, so there's nothing to tune.

:::note
Managed Buckets are available on the **Business** and **Enterprise** plans. If your plan doesn't include them, or you've reached your plan's limit, the form will tell you when you try to create one.
:::

## After Creation

- The bucket name is fixed once created — it can't be changed on an existing account.
- Deleting the account **leaves the stored files in place**, so a deletion never destroys your data. Contact support if you need the storage itself removed.
- A Managed Bucket behaves like any other Document account for [access control](/guides/documents/account-management/control-document-account-access/), [ownership](/guides/documents/account-management/managing-document-account-owners/), and browsing.
