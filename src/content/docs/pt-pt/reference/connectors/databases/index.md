---
title: Ligações a bases de dados e data lakes
description: As ligações a bases de dados e data lakes variam consoante o serviço. Cada conector tem requisitos de segurança e de acesso específicos para o PlaidCloud se ligar.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/index.md
---

O PlaidCloud liga-se diretamente a bases de dados, data lakes, motores de consulta e lakehouses. As ligações também podem passar por um agente PlaidLink quando o destino se encontra atrás de uma firewall.

Os termos *base de dados*, *lakehouse*, *motor de consulta* e *armazém de dados* designam tecnologias subjacentes diferentes, mas todos expõem uma interface de consulta do tipo SQL, pelo que aqui os tratamos como uma única categoria.

## Bases de dados relacionais

- [PostgreSQL](/pt-pt/reference/connectors/databases/postgres/)
- [MySQL](/pt-pt/reference/connectors/databases/mysql/)
- [Microsoft SQL Server](/pt-pt/reference/connectors/databases/microsoft-sql-server/)
- [Oracle](/pt-pt/reference/connectors/databases/oracle/)
- [IBM DB2](/pt-pt/reference/connectors/databases/ibm-db2/)
- [Informix](/pt-pt/reference/connectors/databases/informix/)

## Armazéns de dados na nuvem

- [Snowflake](/pt-pt/reference/connectors/databases/snowflake/)
- [Amazon Redshift](/pt-pt/reference/connectors/databases/amazon-redshift/)
- [Amazon Athena](/pt-pt/reference/connectors/databases/amazon-athena/)
- [Azure Databricks](/pt-pt/reference/connectors/databases/azure-databricks/)
- [Microsoft Fabric](/pt-pt/reference/connectors/databases/microsoft-fabric/)
- [SAP HANA](/pt-pt/reference/connectors/databases/sap-hana/)

## Bases de dados analíticas

- [Greenplum](/pt-pt/reference/connectors/databases/greenplum/)
- [Exasol](/pt-pt/reference/connectors/databases/exasol/)
- [Databend](/pt-pt/reference/connectors/databases/databend/): motor do Lakehouse v1
- [StarRocks](/pt-pt/reference/connectors/databases/starrocks/): motor do Lakehouse v2
- [Doris](/pt-pt/reference/connectors/databases/doris/)
- [PlaidCloud Lakehouse](/pt-pt/reference/connectors/databases/plaidcloud-lakehouse/)

## Motores de consulta

- [Presto](/pt-pt/reference/connectors/databases/presto/)
- [Trino](/pt-pt/reference/connectors/databases/trino/)
- [Apache Hive](/pt-pt/reference/connectors/databases/hive/)
- [Apache Spark](/pt-pt/reference/connectors/databases/spark/)

## Armazenamentos de documentos e de streaming

- [MongoDB](/pt-pt/reference/connectors/databases/mongodb/)
- [Apache Kafka](/pt-pt/reference/connectors/databases/apache-kafka/)

## Genérico

- [ODBC](/pt-pt/reference/connectors/databases/odbc/): ligue-se através de um DSN ou de um driver ODBC na máquina de um agente PlaidLink
