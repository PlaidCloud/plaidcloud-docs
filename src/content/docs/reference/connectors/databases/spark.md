---
title: Apache Spark
description: Set up an Apache Spark database connection in PlaidCloud to run distributed queries and integrate big data into workflows.
sidebar:
  order: 1
---

**Apache Spark** is the distributed compute engine commonly used for ETL over large datasets. Use this connector to read and write data through Spark SQL endpoints (typically Spark Thrift Server). For Databricks-managed Spark, prefer the [Azure Databricks](../azure-databricks/) connector.

## Upstream Documentation
The Apache Spark documentation is [here](https://spark.apache.org/documentation.html).

The Apache project is [here](https://spark.apache.org/).

## Setup

This connector uses a vendor-specific authentication flow and is configured directly from the **Connections** screen in your workspace. The configuration fields shown depend on the credentials your tenant administrator has provisioned for the integration.

See the upstream [spark documentation](https://spark.apache.org/docs/latest/) for the latest setup specifics.

If you need help setting up this connector for your tenant, contact your account team — connector-specific credentials, environment URLs, and any required pre-provisioning typically need to be coordinated with PlaidCloud support.