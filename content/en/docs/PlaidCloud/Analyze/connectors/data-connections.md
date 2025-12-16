---
title: Data Connections
slug: data-connections
description: Use this table reference for more information on external system connections and databases
date: 2022-01-25T07:39:49
---


## Description

PlaidCloud connects to external systems by using various data connections directly or through PlaidLink agents.

For more details on each data connection type, please navigate to the specific data connection documentation.

## Relational Databases


### Databricks

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | databricks |

### Greenplum

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | greenplum |

### Microsoft SQL Server

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | sqlserver |

### MySQL

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | mysql |

### ODBC

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | odbc |

### Oracle

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | oracle |

### Postgres

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | postgres |

### Amazon Redshift

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | redshift |

### SAP HANA

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | hana |

### Exasol

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | exasol |

### IBM DB2

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | db2 |

### Informix

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | informix |

## Hadoop Based Databases

### Hive

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | hive |

### Presto

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | presto |

### Spark

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Database |
| **Reference** | spark |

## Team Collaboration Tools

### Microsoft Teams

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Notification |
| **Reference** | teams |

### Slack

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Notification |
| **Reference** | slack |


## Cloud Services

### OAuth Connection

| Parameter | Value |
|-----------|-------|
| **Connection Type** | oAuth |
| **Reference** | oauth |

### Quandl

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Quandl |
| **Reference** | quandl |

## Google Related

### Google Big Query

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Google Big Query |
| **Reference** | gbq |

### Google Spreadsheet

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Google Spreadsheet |
| **Reference** | gspread |


## Databricks Related

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


## Oracle EBS Related

Oracle EBS utilizes the standard Oracle database connection specified above.  This connection provides the connectivity
to query, load, and execute PL/SQL programs in Oracle.

If the EBS instance has the REST API interface available, this can be accessed using the same approach as Oracle Cloud described below.


## Oracle Cloud Related

Oracle Cloud utilizes standard RESTful requests to perform queries, data loading, and other operations.  A REST connection using OAuth2
tokens is used for these interactions.  This uses the standard oAuth connection specified above.


## Salesforce Related

Salesforce utilizes standard RESTful requests to perform all operations.  A REST connection using OAuth2
tokens is used for these interactions.  This uses the Salesforce specific connection type.

## Workday Related

Workday utilizes standard RESTful requests to perform all operations.  A REST connection using OAuth2
tokens is used for these interactions.  This uses the standard oAuth connection specified above.


## JD Edwards Legacy Version Related

| Parameter | Value |
|-----------|-------|
| **Connection Type** | JD Edwards Legacy |
| **Reference** | jde_legacy |


## JD Edwards Related

JD Edwards utilizes the standard Oracle database connection specified above.  This connection provides the connectivity
to query, load, and execute PL/SQL programs in Oracle.


## Infor Related

| Parameter | Value |
|-----------|-------|
| **Connection Type** | Infor |
| **Reference** | infor |


## SAP Related

### SAP Analytics Cloud

| Parameter | Value |
|-----------|-------|
| **Connection Type** | SAP Analytics Cloud |
| **Reference** | sap_sac |

### SAP ECC

| Parameter | Value |
|-----------|-------|
| **Connection Type** | SAP ECC |
| **Reference** | sap_ecc |

### SAP Profitability and Cost Management (PCM)

| Parameter | Value |
|-----------|-------|
| **Connection Type** | SAP PCM |
| **Reference** | sap_pcm |

### SAP Profitability and Performance Management (PaPM)

| Parameter | Value |
|-----------|-------|
| **Connection Type** | SAP PaPM |
| **Reference** | sap_papm |
