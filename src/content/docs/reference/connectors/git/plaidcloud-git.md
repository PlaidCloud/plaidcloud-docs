---
title: PlaidCloud Git Connector
description: Connect a Panel app, Dash app, or workflow to a repository in PlaidCloud Git — the managed built-in Git service — with no server URL or credentials to configure.
sidebar:
  order: 0
---

**PlaidCloud Git** is the managed Git service built into your workspace. A PlaidCloud Git connection points a Panel or Dash deployment — or a workflow — at one of your repositories. Because the service is managed, it needs **no server URL, username, or token**: PlaidCloud supplies the host and authenticates on your behalf.

For the end-to-end walkthrough of serving an app from one of these connections, see [Deploy a Panel App From PlaidCloud Git](/guides/panel-apps/deploy-from-git/) or [Deploy a Dash App From PlaidCloud Git](/guides/dash-apps/deploy-from-git/). To create repositories and push code, see the [PlaidCloud Git guides](/guides/git/).

## Configuration

From **Tools > Connections**, click **New Connection** and choose **PlaidCloud Git**. The form drops the authentication, SSL, and SSH sections that external Git providers show — credentials are platform-derived — leaving the connection's identity, usage, and repository target.

### Identification

| Field | Type | Description |
|---|---|---|
| Account Name | Text | Display name for this connection. |
| Memo | Text | Optional note about what the connection is for. |

### Repository

| Field | Type | Description |
|---|---|---|
| Repository | Picker | The repository to use. Click **Refresh** to list your workspace repositories — for example `apps` or `udfs` — and choose one. |
| Default Branch | Picker | The branch to read from, chosen from the branches in the selected repository. |
| Start Path | Picker | Optional. Browse the selected repository and choose a folder to scope every file lookup to a subdirectory. |

**Usage** (`Active` / `Read Only`) and the **Security Model** (who in the workspace may use the connection) are the standard connection settings — see the [connection guide](/guides/connections/plaidcloud-git/) and [Create and Manage a Connection](/guides/connections/create-connection/).

## Common Uses

- Serving a [HoloViz Panel app](/guides/panel-apps/deploy-from-git/) or a [Plotly Dash app](/guides/dash-apps/deploy-from-git/) from your workspace's `apps` repository.
- Sourcing user-defined functions, configuration, or templated files that live in PlaidCloud Git.

## Related

- [PlaidCloud Git Connection](/guides/connections/plaidcloud-git/) — task guide for creating the connection, with usage and security model
- [Deploy a Panel App From PlaidCloud Git](/guides/panel-apps/deploy-from-git/) — the full path from repository to served app
- [Deploy a Dash App From PlaidCloud Git](/guides/dash-apps/deploy-from-git/) — the same path for a Plotly Dash app
- [PlaidCloud Git guides](/guides/git/) — repositories, issues, pull requests, and more
- [Git Repository Connections](/reference/connectors/git/) — external Git providers (GitHub, GitLab, and others)
