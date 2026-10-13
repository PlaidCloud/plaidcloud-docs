---
title: Tableau Connection
description: Connect PlaidCloud to Tableau Server or Tableau Cloud with a personal access token so workflows can publish data sources.
sidebar:
  order: 3
---

A Tableau connection holds the address of a Tableau Server or Tableau Cloud site and a personal access token. The [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/) step uses it to publish `.hyper` extracts as data sources.

## Before You Start

In Tableau, create a personal access token for the account that should publish: choose **My Account Settings**, then **Personal Access Tokens**. Copy the token secret when Tableau shows it, because Tableau doesn't show it again. The account needs permission to publish data sources to the project you will publish into.

## Create the Connection

1. Open **Analyze**, choose **Tools → External Data Connections**, and select **+ New Connection → Tableau**.
2. Enter the connection's name and description.
3. Enter the connection settings:

| Field | What to Enter |
| --- | --- |
| **Server URL** | The address of the server or Tableau Cloud pod, such as `https://prod-useast-a.online.tableau.com`. A bare host is read as `https`, and an `http` address is refused. |
| **Site** | The site's content URL, the part of the browser address after `#/site/`. Leave blank for the Default site. |
| **Personal Access Token Name** | The name you gave the token in Tableau. |
| **Personal Access Token Secret** | The token secret. It is stored encrypted and shows blank when you reopen the connection. Leave it blank to keep the saved secret. |

4. Select **Create**.

The server must be reachable from the internet. PlaidCloud doesn't connect to a Tableau server on a private network.

## Related

- [Publish to Tableau](/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/reference/workflow-steps/export/export-hyper/)
