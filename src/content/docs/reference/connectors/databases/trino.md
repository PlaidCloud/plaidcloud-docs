---
title: Trino
description: Set up a Trino distributed query engine connection in PlaidCloud to run federated queries across multiple data sources.
sidebar:
  order: 1
---

**Trino** (formerly PrestoSQL) is the distributed SQL query engine commonly used over data lakes. Use this connector to query Trino deployments from PlaidCloud workflows. Authentication uses HTTP Basic Auth or JWT; the catalog and schema you target determine which underlying data source the query hits.

## Upstream Documentation
[The Trino documentation](https://trino.io/docs/current/index.html).

## Setup

This connector uses a vendor-specific authentication flow and is configured directly from the **Connections** screen in your workspace. The configuration fields shown depend on the credentials your tenant administrator has provisioned for the integration.

See the upstream [trino documentation](https://trino.io/docs/current/) for the latest setup specifics.

If you need help setting up this connector for your tenant, contact your account team — connector-specific credentials, environment URLs, and any required pre-provisioning typically need to be coordinated with PlaidCloud support.