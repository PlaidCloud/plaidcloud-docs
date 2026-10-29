---
title: Conexiones de bases de datos y data lakes
description: Las conexiones de bases de datos y data lakes varían según el servicio. Cada conector tiene requisitos específicos de seguridad y acceso para que PlaidCloud pueda conectarse.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

PlaidCloud se conecta directamente a bases de datos, data lakes, motores de consultas y lakehouses. Las conexiones también pueden enrutarse a través de un agente de PlaidLink cuando el destino se encuentra detrás de un firewall.

Los términos *base de datos*, *lakehouse*, *motor de consultas* y *almacén de datos* describen tecnologías subyacentes distintas, pero todos exponen una interfaz de consultas de tipo SQL, por lo que aquí los tratamos como una sola categoría.

## Bases de datos relacionales

- [PostgreSQL](/es/reference/connectors/databases/postgres/)
- [MySQL](/es/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/es/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/es/reference/connectors/databases/oracle/)
- [IBM DB2](/es/reference/connectors/databases/ibm-db2/)
- [Informix](/es/reference/connectors/databases/informix/)

## Almacenes de datos en la nube

- [Snowflake](/es/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/es/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/es/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/es/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/es/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/es/reference/connectors/databases/sap-hana/)

## Bases de datos analíticas

- [Greenplum](/es/reference/connectors/databases/greenplum/)
- [Exasol](/es/reference/connectors/databases/exasol/)
- [Databend](/es/reference/connectors/databases/databend/) — motor de Lakehouse v1
- [StarRocks](/es/reference/connectors/databases/starrocks/) — motor de Lakehouse v2
- [Doris](/es/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/es/reference/connectors/databases/plaidcloud-lakehouse/)

## Motores de consultas

- [Presto](/es/reference/connectors/databases/presto/)
- [Trino](/es/reference/connectors/databases/trino/)
- [Apache Hive](/es/reference/connectors/databases/hive/)
- [Apache Spark](/es/reference/connectors/databases/spark/)

## Almacenes de documentos y de streaming

- [MongoDB](/es/reference/connectors/databases/mongodb/)
- [Apache Kafka](/es/reference/connectors/databases/apache-kafka/)

## Genérico

- [ODBC](/es/reference/connectors/databases/odbc/) — conéctese mediante un DSN o un controlador ODBC en el equipo de un agente de PlaidLink
