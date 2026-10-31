---
title: Conectores de dados e serviços
description: Conecte o PlaidCloud a fontes de dados e serviços externos, incluindo bancos de dados, ERPs, APIs REST, armazenamento em nuvem e repositórios Git.
sidebar:
  label: Conectores
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

O PlaidCloud se conecta a fontes de dados e serviços externos por meio de conectores específicos. Cada conector cuida dos detalhes de autenticação, protocolo e formato de dados de uma família de provedores.

## Categorias

### Bancos de dados e data lakes

Bancos de dados relacionais, data warehouses em nuvem, mecanismos de consulta e formatos de lakehouse.

- [Bancos de dados](/pt-br/reference/connectors/databases/) — PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, Redshift, BigQuery, Databricks, MongoDB, Kafka e mais de 15 outros
- [Tabelas abertas](/pt-br/reference/connectors/open-tables/) — formatos de tabela aberta Apache Iceberg, Delta Lake, Hudi e Hive

### Serviços em nuvem e SaaS

- [REST](/pt-br/reference/connectors/rest/) — Salesforce, NetSuite, Workday, QuickBooks, Stripe, Dynamics e mais
- [Sistemas ERP](/pt-br/reference/connectors/erp/) — SAP ECC / S/4HANA, Oracle EBS/Fusion, Infor, JD Edwards
- [Serviços em nuvem](/pt-br/reference/connectors/cloud-services/) — serviços de dados de terceiros
- [Google](/pt-br/reference/connectors/google/) — BigQuery, Planilhas Google
- [Colaboração](/pt-br/reference/connectors/collaboration/) — Slack, Microsoft Teams, Tableau
- [Fontes Singer](/pt-br/reference/connectors/singer-sources/) — mais de 130 fontes Singer-tap: Stripe, GitHub, HubSpot, bancos de dados e mais

### Desenvolvimento e controle de código-fonte

- [Provedores Git](/pt-br/reference/connectors/git/) — PlaidCloud Git (gerenciado e integrado), além de GitHub, GitLab, Bitbucket, Azure Repos e CodeCommit

## Relacionados

- [Guia de conexões](/pt-br/guides/connections/) — passo a passo orientado a tarefas para criar e gerenciar conexões
- [Referência de etapas de fluxo de trabalho](/pt-br/reference/workflow-steps/) — o que fazer com uma conexão depois de configurada
