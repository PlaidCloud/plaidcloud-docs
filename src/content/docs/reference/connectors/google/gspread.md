---
title: Google Sheets
description: Set up a Google Sheets connection in PlaidCloud to import, export, and synchronize spreadsheet data within your workflows.
sidebar:
  order: 1
---

## Connection Documentation
Google Sheets is oriented more towards consumers.  For technical documentation, refer to the [developer documentation](https://developers.google.com/workspace/sheets).

## Configuration

These fields appear when creating or editing this connection. Required vs optional depends on the authentication options you enable.

### Identification

| Field | Type | Description |
|---|---|---|
| Name | Text | Display name for this connection. |
| Alias | Text (multi-line) | Optional alias or notes about the connection. |
| Is active | Toggle | Whether the connection is enabled. Disable to pause without deleting. |
| Db read only | Toggle | Restrict the connection to read-only operations. |
| Access type | Select | Read-only, write-only, or read-write access level for this connection. |
