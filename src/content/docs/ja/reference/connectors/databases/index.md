---
title: データベースとデータレイクの接続
description: データベースとデータレイクの接続はサービスごとに異なります。各コネクタには、PlaidCloudが接続するための固有のセキュリティ要件とアクセス要件があります。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

PlaidCloudは、データベース、データレイク、クエリエンジン、レイクハウスに直接接続します。接続先がファイアウォールの内側にある場合は、PlaidLinkエージェント経由で接続することもできます。

*データベース*、*レイクハウス*、*クエリエンジン*、*データウェアハウス*は、基盤となる技術がそれぞれ異なりますが、いずれもSQL形式のクエリインターフェースを備えているため、ここでは1つのカテゴリとして扱います。

## リレーショナルデータベース

- [PostgreSQL](/ja/reference/connectors/databases/postgres/)
- [MySQL](/ja/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/ja/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/ja/reference/connectors/databases/oracle/)
- [IBM DB2](/ja/reference/connectors/databases/ibm-db2/)
- [Informix](/ja/reference/connectors/databases/informix/)

## クラウドデータウェアハウス

- [Snowflake](/ja/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/ja/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/ja/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/ja/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/ja/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/ja/reference/connectors/databases/sap-hana/)

## 分析データベース

- [Greenplum](/ja/reference/connectors/databases/greenplum/)
- [Exasol](/ja/reference/connectors/databases/exasol/)
- [Databend](/ja/reference/connectors/databases/databend/) — Lakehouse v1エンジン
- [StarRocks](/ja/reference/connectors/databases/starrocks/) — Lakehouse v2エンジン
- [Doris](/ja/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/ja/reference/connectors/databases/plaidcloud-lakehouse/)

## クエリエンジン

- [Presto](/ja/reference/connectors/databases/presto/)
- [Trino](/ja/reference/connectors/databases/trino/)
- [Apache Hive](/ja/reference/connectors/databases/hive/)
- [Apache Spark](/ja/reference/connectors/databases/spark/)

## ドキュメントストアとストリーミングストア

- [MongoDB](/ja/reference/connectors/databases/mongodb/)
- [Apache Kafka](/ja/reference/connectors/databases/apache-kafka/)

## 汎用

- [ODBC](/ja/reference/connectors/databases/odbc/) — DSN、またはPlaidLinkエージェントのマシン上のODBCドライバー経由で接続します
