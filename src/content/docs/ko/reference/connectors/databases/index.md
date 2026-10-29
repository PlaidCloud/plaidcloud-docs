---
title: 데이터베이스 및 데이터 레이크 연결
description: 데이터베이스 및 데이터 레이크 연결은 서비스마다 다릅니다. 각 커넥터에는 PlaidCloud가 연결하기 위한 고유한 보안 및 액세스 요구 사항이 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

PlaidCloud는 데이터베이스, 데이터 레이크, 쿼리 엔진, Lakehouse에 직접 연결합니다. 대상이 방화벽 뒤에 있는 경우 PlaidLink 에이전트를 통해 연결을 라우팅할 수도 있습니다.

*데이터베이스*, *Lakehouse*, *쿼리 엔진*, *데이터 웨어하우스*는 서로 다른 기반 기술을 가리키지만 모두 SQL 방식의 쿼리 인터페이스를 제공하므로, 여기서는 하나의 범주로 다룹니다.

## 관계형 데이터베이스

- [PostgreSQL](/ko/reference/connectors/databases/postgres/)
- [MySQL](/ko/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/ko/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/ko/reference/connectors/databases/oracle/)
- [IBM DB2](/ko/reference/connectors/databases/ibm-db2/)
- [Informix](/ko/reference/connectors/databases/informix/)

## 클라우드 데이터 웨어하우스

- [Snowflake](/ko/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/ko/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/ko/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/ko/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/ko/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/ko/reference/connectors/databases/sap-hana/)

## 분석 데이터베이스

- [Greenplum](/ko/reference/connectors/databases/greenplum/)
- [Exasol](/ko/reference/connectors/databases/exasol/)
- [Databend](/ko/reference/connectors/databases/databend/) — Lakehouse v1 엔진
- [StarRocks](/ko/reference/connectors/databases/starrocks/) — Lakehouse v2 엔진
- [Doris](/ko/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/ko/reference/connectors/databases/plaidcloud-lakehouse/)

## 쿼리 엔진

- [Presto](/ko/reference/connectors/databases/presto/)
- [Trino](/ko/reference/connectors/databases/trino/)
- [Apache Hive](/ko/reference/connectors/databases/hive/)
- [Apache Spark](/ko/reference/connectors/databases/spark/)

## 문서 및 스트리밍 저장소

- [MongoDB](/ko/reference/connectors/databases/mongodb/)
- [Apache Kafka](/ko/reference/connectors/databases/apache-kafka/)

## 일반

- [ODBC](/ko/reference/connectors/databases/odbc/) — PlaidLink 에이전트 컴퓨터의 DSN 또는 ODBC 드라이버를 통해 연결합니다
