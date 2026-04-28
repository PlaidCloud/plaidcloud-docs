---
title: Clone a Connection
slug: clone-connection
weight: 2.0
description: Clone an existing external data connection in PlaidCloud to reuse its configuration as the starting point for a new connection.
date: 2026-04-28T00:00:00
---


## Description

Cloning duplicates the configuration of an existing connection — host, port, options, credentials reference — so you can edit a few fields and save it as a new connection rather than re-entering every setting.

Cloning works for every external data connection type: database, ERP, REST, cloud service, Git, and document.


## Clone a Connection

1. Go to **Tools > Connections** (or **Project > Connections** for project-scoped connectors)
2. Select the connection you want to copy
3. Click `Clone` in the toolbar
4. Edit the new connection's name and any fields that should differ
5. Click `Save`


## Owner-only Actions

`Edit`, `Clone`, and `Delete` are restricted to the connection owner. If you don't see those actions on a connection, you are not the owner — ask the owner to clone it for you, or have them transfer ownership.

{{< note >}}
Cloning copies the configuration but not any test results or run history. Test the cloned connection before relying on it in a workflow.
{{< /note >}}
