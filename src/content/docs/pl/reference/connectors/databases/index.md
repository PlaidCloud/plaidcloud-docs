---
title: Połączenia z bazami danych i jeziorami danych
description: Połączenia z bazami danych i jeziorami danych różnią się w zależności od usługi. Każdy konektor ma własne wymagania dotyczące zabezpieczeń i dostępu, które PlaidCloud musi spełnić, aby się połączyć.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

PlaidCloud łączy się bezpośrednio z bazami danych, jeziorami danych, silnikami zapytań i lakehouse'ami. Połączenia mogą też być kierowane przez agenta PlaidLink, gdy cel znajduje się za zaporą sieciową.

Terminy *baza danych*, *lakehouse*, *silnik zapytań* i *hurtownia danych* opisują różne technologie, ale wszystkie udostępniają interfejs zapytań w stylu SQL, dlatego traktujemy je tutaj jako jedną kategorię.

## Relacyjne bazy danych

- [PostgreSQL](/pl/reference/connectors/databases/postgres/)
- [MySQL](/pl/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/pl/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/pl/reference/connectors/databases/oracle/)
- [IBM DB2](/pl/reference/connectors/databases/ibm-db2/)
- [Informix](/pl/reference/connectors/databases/informix/)

## Chmurowe hurtownie danych

- [Snowflake](/pl/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/pl/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/pl/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/pl/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/pl/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/pl/reference/connectors/databases/sap-hana/)

## Analityczne bazy danych

- [Greenplum](/pl/reference/connectors/databases/greenplum/)
- [Exasol](/pl/reference/connectors/databases/exasol/)
- [Databend](/pl/reference/connectors/databases/databend/) — silnik Lakehouse v1
- [StarRocks](/pl/reference/connectors/databases/starrocks/) — silnik Lakehouse v2
- [Doris](/pl/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/pl/reference/connectors/databases/plaidcloud-lakehouse/)

## Silniki zapytań

- [Presto](/pl/reference/connectors/databases/presto/)
- [Trino](/pl/reference/connectors/databases/trino/)
- [Apache Hive](/pl/reference/connectors/databases/hive/)
- [Apache Spark](/pl/reference/connectors/databases/spark/)

## Magazyny dokumentów i strumieni

- [MongoDB](/pl/reference/connectors/databases/mongodb/)
- [Apache Kafka](/pl/reference/connectors/databases/apache-kafka/)

## Ogólne

- [ODBC](/pl/reference/connectors/databases/odbc/) — połączenie przez DSN lub sterownik ODBC na komputerze agenta PlaidLink
