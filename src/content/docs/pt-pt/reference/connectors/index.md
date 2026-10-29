---
title: Conectores de dados e serviços
description: Ligue o PlaidCloud a origens de dados e serviços externos, incluindo bases de dados, ERP, APIs REST, armazenamento na nuvem e repositórios Git.
sidebar:
  label: Conectores
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/index.md
---

O PlaidCloud liga-se a origens de dados e serviços externos através de conectores concebidos para o efeito. Cada conector trata da autenticação, do protocolo e das particularidades do formato de dados de uma família de fornecedores.

## Categorias

### Bases de dados e data lakes

Bases de dados relacionais, armazéns na nuvem, motores de consulta e formatos de lakehouse.

- [Bases de dados](/pt-pt/reference/connectors/databases/) — PostgreSQL, MySQL, SQL Server, Oracle, Snowflake, Redshift, BigQuery, Databricks, MongoDB, Kafka e mais de 15 outras
- [Tabelas abertas](/pt-pt/reference/connectors/open-tables/) — formatos de tabela aberta Apache Iceberg, Delta Lake, Hudi e Hive

### Serviços na nuvem e SaaS

- [REST](/pt-pt/reference/connectors/rest/) — Salesforce, NetSuite, Workday, QuickBooks, Stripe, Dynamics e mais
- [Sistemas ERP](/pt-pt/reference/connectors/erp/) — SAP ECC / S/4HANA, Oracle EBS/Fusion, Infor, JD Edwards
- [Serviços na nuvem](/pt-pt/reference/connectors/cloud-services/) — serviços de dados de terceiros
- [Google](/pt-pt/reference/connectors/google/) — BigQuery, Google Sheets
- [Colaboração](/pt-pt/reference/connectors/collaboration/) — Slack, Microsoft Teams, Tableau
- [Origens Singer](/pt-pt/reference/connectors/singer-sources/) — mais de 130 origens Singer-tap: Stripe, GitHub, HubSpot, bases de dados e mais

### Desenvolvimento e controlo de código-fonte

- [Fornecedores Git](/pt-pt/reference/connectors/git/) — PlaidCloud Git (gerido, integrado), além de GitHub, GitLab, Bitbucket, Azure Repos e CodeCommit

## Relacionado

- [Guia de ligações](/pt-pt/guides/connections/) — passo a passo orientado para tarefas para criar e gerir ligações
- [Referência de passos de fluxo de trabalho](/pt-pt/reference/workflow-steps/) — o que fazer com uma ligação depois de configurada
