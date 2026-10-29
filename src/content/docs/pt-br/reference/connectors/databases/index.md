---
title: Conexões de banco de dados e data lake
description: As conexões de banco de dados e data lake variam conforme o serviço. Cada conector tem requisitos próprios de segurança e acesso para o PlaidCloud se conectar.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

O PlaidCloud se conecta diretamente a bancos de dados, data lakes, mecanismos de consulta e lakehouses. As conexões também podem passar por um agente PlaidLink quando o destino está atrás de um firewall.

Os termos *banco de dados*, *lakehouse*, *mecanismo de consulta* e *data warehouse* descrevem tecnologias diferentes, mas todos expõem uma interface de consulta no estilo SQL, por isso os tratamos como uma única categoria aqui.

## Bancos de Dados Relacionais

- [PostgreSQL](/pt-br/reference/connectors/databases/postgres/)
- [MySQL](/pt-br/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/pt-br/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/pt-br/reference/connectors/databases/oracle/)
- [IBM DB2](/pt-br/reference/connectors/databases/ibm-db2/)
- [Informix](/pt-br/reference/connectors/databases/informix/)

## Data Warehouses na Nuvem

- [Snowflake](/pt-br/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/pt-br/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/pt-br/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/pt-br/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/pt-br/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/pt-br/reference/connectors/databases/sap-hana/)

## Bancos de Dados Analíticos

- [Greenplum](/pt-br/reference/connectors/databases/greenplum/)
- [Exasol](/pt-br/reference/connectors/databases/exasol/)
- [Databend](/pt-br/reference/connectors/databases/databend/) — mecanismo do Lakehouse v1
- [StarRocks](/pt-br/reference/connectors/databases/starrocks/) — mecanismo do Lakehouse v2
- [Doris](/pt-br/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/pt-br/reference/connectors/databases/plaidcloud-lakehouse/)

## Mecanismos de Consulta

- [Presto](/pt-br/reference/connectors/databases/presto/)
- [Trino](/pt-br/reference/connectors/databases/trino/)
- [Apache Hive](/pt-br/reference/connectors/databases/hive/)
- [Apache Spark](/pt-br/reference/connectors/databases/spark/)

## Armazenamentos de Documentos e Streaming

- [MongoDB](/pt-br/reference/connectors/databases/mongodb/)
- [Apache Kafka](/pt-br/reference/connectors/databases/apache-kafka/)

## Genérico

- [ODBC](/pt-br/reference/connectors/databases/odbc/) — conecte-se por um DSN ou por um driver ODBC na máquina de um agente PlaidLink
