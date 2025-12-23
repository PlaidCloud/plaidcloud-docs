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

| Connection | Kind     | Reference  |
|------------|----------|------------|
| Amazon Athena | Database | athena |
| Amazon Redshift | Database | redshift |
| Databend | Database | databend |
| Databricks | Database | databricks |
| Exasol | Database | exasol |
| Greenplum | Database | greenplum |
| Hive | Database | hive |
| IBM DB2 | Database | db2 |
| Informix | Database | informix |
| Microsoft SQL Server | Database | sqlserver |
| MySQL | Database | mysql |
| ODBC | Database | odbc |
| Oracle | Database | oracle |
| PlaidCloud Lakehouse | Database | plaid |
| Presto | Database | presto |
| Postgres | Database | postgres |
| SAP HANA | Database | hana |
| Spark | Database | spark |
| StarRocks | Database | starrocks |


## Team Collaboration Tools

| Connection | Kind     | Reference  |
|------------|----------|------------|
| Microsoft Teams | Notification | teams |
| Slack | Notification | slack |

## ERP Systems

| Connection | Kind     | Reference  |
|------------|----------|------------|
| Infor | ERP | infor |
| JD Edwards Legacy | ERP | jde_legacy |
| Oracle EBS| ERP | oracle_ebs |
| Oracle Fusion | ERP | oracle_fusion |
| SAP Analytics Cloud | ERP | sap_sac |
| SAP ECC | ERP | sap_ecc |
| SAP S/4HANA | ERP | sap_s4 |
| SAP Profitability and Cost Management (PCM) | ERP | sap_pcm |
| SAP Profitability and Performance Management (PaPM) | ERP | sap_papm |


## Cloud Services

| Connection | Kind     | Reference  |
|------------|----------|------------|
| Quandl | Cloud Services | quandl |


## Google Related

| Connection | Kind     | Reference  |
|------------|----------|------------|
| Google Big Query | Google | gbq |
| Google Sheets | Google | gspread |

## RESTful Related

| Connection | Kind     | Reference  |
|------------|----------|------------|
| Generic | REST | rest |
| Basic Auth | REST | basic |
| Salesforce | REST | salesforce |
| Postman | REST | postman |
| Sage Intacct | REST | sage |
| Ramp | REST | ramp |
| Paycor | REST | paycor |
| Stripe | REST | stripe |
| Quickbooks | REST | quickbooks |
| Bill.com | REST | bill |
| Microsoft Dynamics | REST | dynamics |
| Workday | REST | workday |
| NetSuite | REST | netsuite |
| Epicore Eclipse | REST | eclipse |

## Git Repository Related

| Connection | Kind     | Reference  |
|------------|----------|------------|
| AWS CodeCommit | Git | codecommit |
| Azure Repos | Git | azure-repos |
| GitHub | Git | github |
| GitLab | Git | gitlab |
| Bitbucket | Git | bitbucket |

## Open Table Format Related

| Connection | Kind     | Reference  |
|------------|----------|------------|
| Apache Hive | Open Table Format | hive |
| Apache Hudi | Open Table Format | hudi |
| Apache Iceberg | Open Table Format | iceberg |
| Delta Lake | Open Table Format | deltalake |


## Oracle EBS Related

Oracle EBS utilizes the standard Oracle database connection specified above.  This connection provides the connectivity
to query, load, and execute PL/SQL programs in Oracle.

If the EBS instance has the REST API interface available, this can be accessed using the same approach as Oracle Cloud REST connection too.
