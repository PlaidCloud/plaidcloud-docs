---
title: Azure Databricks
slug: azure-databricks
description: Configure an Azure Databricks connection in PlaidCloud to integrate Spark-based analytics and lakehouse data into workflows.
weight: 1.0
date: 2025-10-21T07:39:51
---


## Upstream Documentation
Azure Databricks documentation is [here](https://learn.microsoft.com/en-us/azure/databricks/).

## Security Requirements
Documentation under development

## Obtain Credentials
In order to obtain the connection credentials necessary for PlaidCloud to communicate with a Databricks warehouse, follow the steps below:
 1. Open the Databricks console
 2. Under the User Settings in the upper right, select "Settings"
 3. Navigate to the "Developers" section
 4. Generate an Access Token with a sufficient lifespan specified
 5. Navigate to the "SQL Warehouses" area
 6. Select the warehouse required for connecting
 7. Capture the connection details including host, and http path
 8. Navigate to the warehouse data area
 9. Capture the initial catalog and initial schema information

With the information above, the connection form can be completed and tested with the Databricks warehouse

## Create Database Connector
Documentation under development
