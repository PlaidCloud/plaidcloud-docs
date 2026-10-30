---
title: 数据库与数据湖连接
description: 数据库和数据湖连接因服务而异。每个连接器都有各自的安全和访问要求，PlaidCloud 才能连接。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

PlaidCloud 可直接连接数据库、数据湖、查询引擎和 Lakehouse。当目标位于防火墙之后时，连接也可以通过 PlaidLink 代理路由。

*数据库*、*Lakehouse*、*查询引擎*和*数据仓库*这些术语对应不同的底层技术，但都提供 SQL 风格的查询接口，因此这里将它们归为一类。

## 关系型数据库

- [PostgreSQL](/zh-cn/reference/connectors/databases/postgres/)
- [MySQL](/zh-cn/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/zh-cn/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/zh-cn/reference/connectors/databases/oracle/)
- [IBM DB2](/zh-cn/reference/connectors/databases/ibm-db2/)
- [Informix](/zh-cn/reference/connectors/databases/informix/)

## 云数据仓库

- [Snowflake](/zh-cn/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/zh-cn/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/zh-cn/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/zh-cn/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/zh-cn/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/zh-cn/reference/connectors/databases/sap-hana/)

## 分析型数据库

- [Greenplum](/zh-cn/reference/connectors/databases/greenplum/)
- [Exasol](/zh-cn/reference/connectors/databases/exasol/)
- [Databend](/zh-cn/reference/connectors/databases/databend/) — Lakehouse v1 引擎
- [StarRocks](/zh-cn/reference/connectors/databases/starrocks/) — Lakehouse v2 引擎
- [Doris](/zh-cn/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/zh-cn/reference/connectors/databases/plaidcloud-lakehouse/)

## 查询引擎

- [Presto](/zh-cn/reference/connectors/databases/presto/)
- [Trino](/zh-cn/reference/connectors/databases/trino/)
- [Apache Hive](/zh-cn/reference/connectors/databases/hive/)
- [Apache Spark](/zh-cn/reference/connectors/databases/spark/)

## 文档与流式存储

- [MongoDB](/zh-cn/reference/connectors/databases/mongodb/)
- [Apache Kafka](/zh-cn/reference/connectors/databases/apache-kafka/)

## 通用

- [ODBC](/zh-cn/reference/connectors/databases/odbc/) — 通过 DSN 或 PlaidLink 代理所在机器上的 ODBC 驱动程序进行连接
