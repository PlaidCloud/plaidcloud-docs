---
title: Getting Started with PySpark
description: Get started using PySpark in PlaidCloud for distributed data processing within user-defined functions and Jupyter Notebooks.
sidebar:
  order: 2
---

## PySpark Documentation
PySpark is similar to using Pandas but allows for distributed compute and is not RAM bound.  PySpark is available in both UDFs and Jupyter Notebooks.

## Spark Cluster
By default, workspaces do not have the Spark cluster enabled.  To activate the Spark Cluster, go to the Workspace management app and enable the "Spark Compute Cluster" service.

Once activated, Spark jobs can be submitted to the cluster.

The cluster can be monitored from the `spark` sub-domain for the Workspace (e.g. `https://spark.my_workspace.plaid.cloud`)
