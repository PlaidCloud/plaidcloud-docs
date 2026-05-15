---
title: Database and Data Lake Connections
description: Database and Data Lake connections vary by service. Each connector has specific security and access requirements for PlaidCloud to connect.
---

PlaidCloud connects directly to databases, data lakes, query engines, and lakehouses. Connections can also route through a PlaidLink Agent when the target sits behind a firewall.

The terms *database*, *lakehouse*, *query engine*, and *data warehouse* describe different underlying technologies but all expose a SQL-style query interface — so we treat them as one category here.

## Relational Databases

- [PostgreSQL](/reference/connectors/databases/postgres/)
- [MySQL](/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/reference/connectors/databases/oracle/)
- [IBM DB2](/reference/connectors/databases/ibm-db2/)
- [Informix](/reference/connectors/databases/informix/)

## Cloud Data Warehouses

- [Snowflake](/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/reference/connectors/databases/sap-hana/)

## Analytical Databases

- [Greenplum](/reference/connectors/databases/greenplum/)
- [Exasol](/reference/connectors/databases/exasol/)
- [Databend](/reference/connectors/databases/databend/) — Lakehouse v1 engine
- [StarRocks](/reference/connectors/databases/starrocks/) — Lakehouse v2 engine
- [Doris](/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/reference/connectors/databases/plaidcloud-lakehouse/)

## Query Engines

- [Presto](/reference/connectors/databases/presto/)
- [Trino](/reference/connectors/databases/trino/)
- [Apache Hive](/reference/connectors/databases/hive/)
- [Apache Spark](/reference/connectors/databases/spark/)

## Generic

- [ODBC](/reference/connectors/databases/odbc/) — connect to any database with an ODBC driver
