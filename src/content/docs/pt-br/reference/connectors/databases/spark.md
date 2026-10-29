---
title: Apache Spark
description: Configure uma conexão de banco de dados Apache Spark no PlaidCloud para executar consultas distribuídas e integrar big data aos fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

**Apache Spark** é o mecanismo de computação distribuída comumente usado para ETL em grandes conjuntos de dados. Use este conector para ler e gravar dados por meio de endpoints do Spark SQL (normalmente o Spark Thrift Server). Para o Spark gerenciado pelo Databricks, prefira o conector [Azure Databricks](../azure-databricks/).

## Documentação do Fornecedor
[A documentação do Apache Spark](https://spark.apache.org/documentation.html).

O [projeto Apache](https://spark.apache.org/).

## Configuração Inicial

Este conector usa um fluxo de autenticação específico do fornecedor e é configurado diretamente na tela **Conexões** do seu espaço de trabalho. Os campos de configuração exibidos dependem das credenciais que o administrador do seu tenant provisionou para a integração.

Consulte a [documentação do spark](https://spark.apache.org/docs/latest/) do fornecedor para ver os detalhes mais recentes da configuração.

Se precisar de ajuda para configurar este conector no seu tenant, entre em contato com a sua equipe de conta — as credenciais específicas do conector, as URLs de ambiente e qualquer provisionamento prévio necessário normalmente precisam ser coordenados com o suporte do PlaidCloud.
