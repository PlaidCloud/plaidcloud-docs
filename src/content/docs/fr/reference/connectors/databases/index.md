---
title: Connexions aux bases de données et aux data lakes
description: Les connexions aux bases de données et aux data lakes varient selon le service. Chaque connecteur impose ses propres exigences de sécurité et d'accès pour que PlaidCloud puisse s'y connecter.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

PlaidCloud se connecte directement aux bases de données, aux data lakes, aux moteurs de requêtes et aux lakehouses. Les connexions peuvent aussi passer par un agent PlaidLink lorsque la cible se trouve derrière un pare-feu.

Les termes *base de données*, *lakehouse*, *moteur de requêtes* et *entrepôt de données* désignent des technologies sous-jacentes différentes, mais tous exposent une interface de requêtes de type SQL. Nous les traitons donc ici comme une seule catégorie.

## Bases de données relationnelles

- [PostgreSQL](/fr/reference/connectors/databases/postgres/)
- [MySQL](/fr/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/fr/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/fr/reference/connectors/databases/oracle/)
- [IBM DB2](/fr/reference/connectors/databases/ibm-db2/)
- [Informix](/fr/reference/connectors/databases/informix/)

## Entrepôts de données cloud

- [Snowflake](/fr/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/fr/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/fr/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/fr/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/fr/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/fr/reference/connectors/databases/sap-hana/)

## Bases de données analytiques

- [Greenplum](/fr/reference/connectors/databases/greenplum/)
- [Exasol](/fr/reference/connectors/databases/exasol/)
- [Databend](/fr/reference/connectors/databases/databend/) — moteur Lakehouse v1
- [StarRocks](/fr/reference/connectors/databases/starrocks/) — moteur Lakehouse v2
- [Doris](/fr/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/fr/reference/connectors/databases/plaidcloud-lakehouse/)

## Moteurs de requêtes

- [Presto](/fr/reference/connectors/databases/presto/)
- [Trino](/fr/reference/connectors/databases/trino/)
- [Apache Hive](/fr/reference/connectors/databases/hive/)
- [Apache Spark](/fr/reference/connectors/databases/spark/)

## Stockages de documents et de flux

- [MongoDB](/fr/reference/connectors/databases/mongodb/)
- [Apache Kafka](/fr/reference/connectors/databases/apache-kafka/)

## Générique

- [ODBC](/fr/reference/connectors/databases/odbc/) — connexion via un DSN ou un pilote ODBC sur la machine d'un agent PlaidLink
