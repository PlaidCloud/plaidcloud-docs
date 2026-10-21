---
title: Adding New Document Accounts
description: Connect cloud and on-prem document storage to PlaidCloud — S3, GCS, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV, and more.
sidebar:
  label: Adding New Document Accounts
  order: 1
---

Connect cloud and on-prem document storage to PlaidCloud — S3, Google Cloud Storage, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV, and more. Each provider has its own credentials and connection flow.

The quickest option is a **PlaidCloud Managed Bucket**, where PlaidCloud sets up and runs the storage for you — you only pick a name, with nothing else to configure. To connect storage you already own, choose the matching provider below.

## Saved Secrets Are Write-Only

An account's secret, the field labelled **Private Key / Password** or, depending on the account type, **Secret Access Key**, **Account Key**, **Client Secret**, **Access Token**, **Password**, **System User JSON Key** or **OAuth2 Credentials JSON**, is write-only, and so is an SFTP account's **RSA Private Key**. Once saved, they are never shown again, in the form, the API or to an AI assistant. When you edit an account, the field is empty with the hint *Paste the value; leave blank on edit to keep the saved one.* Leave it blank to keep the saved secret, or paste a new one to replace it.

Changing where an account connects needs its secret entered again. If you change the first part of the **Start Path** (for cloud storage, the bucket or container), an SFTP account's **Host or IP Address** or **SSH Connection Port**, or a OneDrive account's **OneDrive Tenant ID**, also paste the secret, or saving is refused with *Changing where the account connects needs its secret entered again*. This stops anyone who can edit an account but never saw its secret from sending that secret to a server they choose.

An AI assistant connected through the PlaidCloud MCP connector can also create and update accounts, with a storage type, credentials and start path. Credentials are write-only and hidden when the account is read back. For a worked example, see [Add OneDrive / SharePoint Account](/guides/documents/adding-accounts/add-onedrive-account/#create-the-account-with-an-ai-assistant).
