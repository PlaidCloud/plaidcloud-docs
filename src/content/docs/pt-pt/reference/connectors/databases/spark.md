---
title: Apache Spark
description: Configure uma ligação a uma base de dados Apache Spark no PlaidCloud para executar consultas distribuídas e integrar big data nos fluxos de trabalho.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

O **Apache Spark** é o motor de computação distribuída habitualmente utilizado para ETL sobre grandes conjuntos de dados. Utilize este conector para ler e escrever dados através de pontos finais Spark SQL (normalmente o Spark Thrift Server). Para o Spark gerido pelo Databricks, prefira o conector [Azure Databricks](../azure-databricks/).

## Documentação do fabricante
[A documentação do Apache Spark](https://spark.apache.org/documentation.html).

O [projeto Apache](https://spark.apache.org/).

## Configuração

Este conector utiliza um fluxo de autenticação específico do fornecedor e é configurado diretamente a partir do ecrã **Ligações** da sua área de trabalho. Os campos de configuração apresentados dependem das credenciais que o administrador do seu inquilino aprovisionou para a integração.

Consulte a [documentação do spark](https://spark.apache.org/docs/latest/) do fabricante para obter os detalhes de configuração mais recentes.

Se precisar de ajuda para configurar este conector para o seu inquilino, contacte a sua equipa de conta: as credenciais específicas do conector, os URL de ambiente e qualquer pré-aprovisionamento necessário têm normalmente de ser coordenados com o suporte do PlaidCloud.
