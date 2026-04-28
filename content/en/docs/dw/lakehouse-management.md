---
title: Lakehouse Management
slug: lakehouse-management
weight: 2.0
description: Manage your StarRocks + Iceberg lakehouse from PlaidCloud — create warehouses, monitor queries, manage users, restart compute, and watch cluster load.
date: 2026-04-28T00:00:00
---


## Description

The **Lakehouse** area provides point-and-click management of your tenant's StarRocks compute and Iceberg catalogs without leaving PlaidCloud. Open it from the **Tools** menu.

The area is split into five tabs: **Warehouses**, **Queries**, **Users**, **Admin**, and **Load**.


## Warehouses

Create, list, and delete the Iceberg warehouses backing your lakehouse.

**To create a warehouse:**

1. Open **Tools > Lakehouse > Warehouses**
2. Click `Add Warehouse`
3. Enter a warehouse name and select the storage backend
4. Click `Create`

**To delete a warehouse:**

1. Select the warehouse row
2. Click `Delete`
3. Confirm in the dialog

{{< note >}}
The default warehouse is protected — it cannot be deleted.
{{< /note >}}


## Queries

Monitor running queries and browse history.

The tab is split top/bottom by a movable divider:

* **Running** — queries executing right now. Auto-polls at the interval you choose from the toolbar.
* **History** — recent completed queries.

**To view a query profile:**

1. Click the `Profile` icon on the query row

**To kill running queries:**

1. Select one or more rows in the **Running** table
2. Click `Kill`
3. Confirm in the dialog


## Users

Manage the database users that connect to the lakehouse from external SQL clients. Both password-based and SSO-provisioned users are listed.

**To add a user:**

1. Open **Tools > Lakehouse > Users**
2. Click `Add User`
3. Enter the username and either a password or the SSO identity
4. Click `Create`


## Admin

Inspect compute workload status and perform restarts.

Workloads are labeled by generation rather than by Kubernetes kind. Each row shows the workload's current status.

**To rolling-restart a workload:**

1. Open **Tools > Lakehouse > Admin**
2. Select the workload
3. Click `Rolling Restart`
4. Read the disruption warning and confirm

{{< note >}}
A rolling restart can briefly interrupt active sessions. Coordinate with users before confirming.
{{< /note >}}


## Load

Watch cluster activity at a glance. Counters and a sparkline are stacked, with the sparkline below the counter row at a 200px minimum height.

The load metrics include active query count and recent activity, sampled on the same auto-poll interval as the **Queries** tab.
