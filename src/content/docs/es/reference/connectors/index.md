---
title: Conectores de datos y servicios
description: Conecte PlaidCloud a orígenes de datos y servicios externos, incluidos bases de datos, ERP, API REST, almacenamiento en la nube y repositorios de Git.
sidebar:
  label: Conectores
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

PlaidCloud se conecta a orígenes de datos y servicios externos mediante conectores diseñados para cada caso. Cada conector se encarga de la autenticación, el protocolo y las particularidades de los datos de una familia de proveedores.

## Categorías

### Bases de datos y lagos de datos

Bases de datos relacionales, almacenes en la nube, motores de consulta y formatos de lakehouse.

- [Bases de datos](/es/reference/connectors/databases/) — PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, Redshift, BigQuery, Databricks, MongoDB, Kafka y más de 15 adicionales
- [Tablas abiertas](/es/reference/connectors/open-tables/) — formatos de tabla abiertos Apache Iceberg, Delta Lake, Hudi y Hive

### Servicios en la nube y SaaS

- [REST](/es/reference/connectors/rest/) — Salesforce, NetSuite, Workday, QuickBooks, Stripe, Dynamics y más
- [Sistemas ERP](/es/reference/connectors/erp/) — SAP ECC / S/4HANA, Oracle EBS/Fusion, Infor, JD Edwards
- [Servicios en la nube](/es/reference/connectors/cloud-services/) — servicios de datos de terceros
- [Google](/es/reference/connectors/google/) — BigQuery, Google Sheets
- [Colaboración](/es/reference/connectors/collaboration/) — Slack, Microsoft Teams, Tableau
- [Orígenes de Singer](/es/reference/connectors/singer-sources/) — más de 130 orígenes basados en Singer-tap: Stripe, GitHub, HubSpot, bases de datos y más

### Desarrollo y control de código fuente

- [Proveedores de Git](/es/reference/connectors/git/) — PlaidCloud Git (administrado, integrado), además de GitHub, GitLab, Bitbucket, Azure Repos y CodeCommit

## Temas relacionados

- [Guía de conexiones](/es/guides/connections/) — tutorial orientado a tareas para crear y administrar conexiones
- [Referencia de pasos de flujo de trabajo](/es/reference/workflow-steps/) — qué hacer con una conexión una vez configurada
