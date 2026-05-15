---
title: Quickbooks REST Connector
description: Configure a QuickBooks REST API connection in PlaidCloud to integrate accounting and financial data into your analysis workflows.
sidebar:
  order: 1
---

## API Documentation
The API documentation is for this connector is located [here](https://developer.intuit.com/app/developer/qbo/docs/learn/explore-the-quickbooks-online-api).

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
