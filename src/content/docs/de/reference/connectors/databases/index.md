---
title: Datenbank- und Data-Lake-Verbindungen
description: Datenbank- und Data-Lake-Verbindungen unterscheiden sich je nach Dienst. Jeder Connector hat eigene Sicherheits- und Zugriffsanforderungen für die Verbindung mit PlaidCloud.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

PlaidCloud verbindet sich direkt mit Datenbanken, Data Lakes, Abfrage-Engines und Lakehouses. Verbindungen können auch über einen PlaidLink-Agent laufen, wenn sich das Ziel hinter einer Firewall befindet.

Die Begriffe *Datenbank*, *Lakehouse*, *Abfrage-Engine* und *Data Warehouse* bezeichnen unterschiedliche zugrunde liegende Technologien, bieten aber alle eine SQL-artige Abfrageschnittstelle. Wir behandeln sie hier daher als eine Kategorie.

## Relationale Datenbanken

- [PostgreSQL](/de/reference/connectors/databases/postgres/)
- [MySQL](/de/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/de/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/de/reference/connectors/databases/oracle/)
- [IBM DB2](/de/reference/connectors/databases/ibm-db2/)
- [Informix](/de/reference/connectors/databases/informix/)

## Cloud-Data-Warehouses

- [Snowflake](/de/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/de/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/de/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/de/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/de/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/de/reference/connectors/databases/sap-hana/)

## Analytische Datenbanken

- [Greenplum](/de/reference/connectors/databases/greenplum/)
- [Exasol](/de/reference/connectors/databases/exasol/)
- [Databend](/de/reference/connectors/databases/databend/) — Lakehouse-v1-Engine
- [StarRocks](/de/reference/connectors/databases/starrocks/) — Lakehouse-v2-Engine
- [Doris](/de/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/de/reference/connectors/databases/plaidcloud-lakehouse/)

## Abfrage-Engines

- [Presto](/de/reference/connectors/databases/presto/)
- [Trino](/de/reference/connectors/databases/trino/)
- [Apache Hive](/de/reference/connectors/databases/hive/)
- [Apache Spark](/de/reference/connectors/databases/spark/)

## Dokumenten- und Streaming-Speicher

- [MongoDB](/de/reference/connectors/databases/mongodb/)
- [Apache Kafka](/de/reference/connectors/databases/apache-kafka/)

## Generisch

- [ODBC](/de/reference/connectors/databases/odbc/) — Verbindung über einen DSN oder einen ODBC-Treiber auf dem Rechner eines PlaidLink-Agents
