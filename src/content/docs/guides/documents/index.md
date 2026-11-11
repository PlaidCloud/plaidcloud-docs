---
title: File Management
description: Manage file storage accounts in PlaidCloud for importing and exporting data via CSV, Excel, Parquet, and other file formats.
sidebar:
  label: Overview
---

PlaidCloud Documents — store, organize, search, and share files alongside your data and workflows. Documents can be sourced from any connected storage account and referenced in workflows.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 200" role="img" aria-label="Connected storage accounts such as S3, Google Cloud Storage, and OneDrive feed PlaidCloud Documents, where files are stored, organized, searched, and shared. Workflow steps then reference those files to import and export data." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="dc-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <text x="76" y="30" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-gray-3)">storage accounts</text>
  <rect x="16" y="40" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="60" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">S3</text>
  <rect x="16" y="82" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Cloud Storage</text>
  <rect x="16" y="124" width="120" height="30" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="76" y="144" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">OneDrive</text>
  <path d="M136 55 C186 55 206 92 246 96" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 97 L246 100" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <path d="M136 139 C186 139 206 108 246 104" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="248" y="70" width="180" height="64" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="338" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Documents</text>
  <text x="338" y="115" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">store · organize · search · share</text>
  <path d="M428 102 L510 102" stroke="var(--sl-color-gray-3)" stroke-width="1.8" fill="none" marker-end="url(#dc-arrow)" />
  <rect x="512" y="76" width="152" height="52" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="588" y="100" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">workflow steps</text>
  <text x="588" y="118" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">import · export files</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Files land in Documents from any connected storage account, where you store, organize, search, and share them — then reference them from workflow steps to import and export data.</figcaption>
</figure>

## The Documents Workspace

**Document** opens with a rail on the left and the page you pick beside it. The rail groups its pages under **Documents** (**Overview** and **Browse**) and **Accounts** (**Your accounts** and **Manage**). Members who can't open a page don't see its item. Each page has a title and a short subtitle at the top, with its actions in the header beside them.

| Rail item | What it shows |
|---|---|
| **Overview** | Tiles for your accounts (**Accounts**, **Shared**, **Private to you**, **Managed buckets**, **External services**, and **Disabled** when an account needs attention), **Pinned** files, **Accounts by service** and **Who can use them**. Select a pinned file to open **Browse** at its folder with the file selected. |
| **Browse** | The file explorer. It opens your favourite account (the one whose top folder you pinned), or the workspace's default account, and you can pick another account from the list in the page header. See [Using Document Accounts](/guides/documents/using-document/). |
| **Your accounts** | Every account you can use, in one list. A **Shared** or **Private** pill on each row says whether the account is shared with you or only yours. Double-click a row to browse it. |
| **Manage** | Accounts you own, with **Name**, **Service**, **Security type**, **Status** and **Description**. A workspace admin sees every document account here and can manage any account they can otherwise manage; system-managed accounts are refused and managed-bucket accounts can't be cloned. |

The rail shows a count beside **Your accounts** and **Manage**. For a workspace admin who holds accounts they don't own, **Manage** shows **admin** instead of a count. The Overview has **Browse files** and **New account** buttons for a quick start.

### Row Actions in Manage

Open a row's **⋯** menu, right-click the row or use the toolbar **Actions** menu for:

- **Open** and **Edit**, which open the account page.
- **Clone…**, **Version history** and **Where used…**. See [Where Used and Re-Point](/guides/documents/account-management/document-account-used-by/).
- **Who can use it**, with **Members**, **Groups**, **Agents** and **Owners**. See [Control Document Account Access](/guides/documents/account-management/control-document-account-access/).
- **Enable** or **Disable**, and **Delete**.

### The Account Page

**New Account**, **Open** and **Edit** show the account as a page, with **Manage Accounts** at the top to go back. It has cards for:

- **General**: the account's name, service, bucket and start path.
- **Access**: the security model and who can use the account. **Members**, **Groups**, **Agents** and **Owners** each have an **Edit** link that opens the same picker as the row menu.
- **Credentials**: write-only fields for the service you chose. A **Credentials saved** note shows the credentials are set, and saved values are never shown. Leave a field blank to keep what is saved. SFTP accounts also have **Test connection**.
- **SSH**: the key settings for SFTP accounts only.

The header has **Browse**, **Where used** and an **Actions** menu with **Clone**, **Version history**, **Enable** or **Disable** and **Delete**. If you leave a page with unsaved changes, PlaidCloud asks whether to discard them.

Old links and bookmarks to document screens still open the matching page.
