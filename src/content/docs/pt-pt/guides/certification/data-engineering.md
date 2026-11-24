---
title: Percurso de aprendizagem de Engenharia de dados
description: O que ler antes dos laboratórios de Profissional e Especialista de Engenharia de dados da certificação PlaidCloud e o que cada laboratório pede.
sidebar:
  label: Engenharia de dados
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

O percurso de Engenharia de dados trata de construir fluxos de trabalho corretos, orientados por variáveis e rápidos. Comece pelo percurso de [Fundamentos](/pt-pt/guides/certification/foundations/). Para saber como funcionam os laboratórios, consulte [Certificação PlaidCloud](/pt-pt/guides/certification/).

## Profissional

### Leia por esta ordem

1. [Criar fluxo de trabalho](/pt-pt/guides/workflows/create-workflow/)
2. [Passos de fluxo de trabalho](/pt-pt/reference/workflow-steps/), em particular [Table Inner Join](/pt-pt/reference/workflow-steps/tables/table-inner-join/) e [Table Extract](/pt-pt/reference/workflow-steps/tables/table-extract/)
3. [Gerir variáveis do fluxo de trabalho](/pt-pt/guides/workflows/manage-workflow-variables/)
4. [Reutilizar o seu trabalho: variáveis, macros e UDFs](/pt-pt/get-started/tutorials/reuse-variables-macros-udfs/)
5. [Executar um fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/)
6. [Ver o registo do fluxo de trabalho](/pt-pt/guides/workflows/viewing-workflow-log/)

### O que o laboratório pede

O laboratório chama-se *Engenharia de dados: construção mensal de vendas*.

Três tabelas em bruto estão carregadas: linhas de vendas, lojas e produtos. No fluxo de trabalho do laboratório, constrói um resumo mensal com uma linha por região e categoria de produto, com unidades e receitas, para as linhas vendidas de um mês. O mês provém de uma variável do projeto, não de um valor escrito num passo: o laboratório altera a variável e executa o fluxo de trabalho novamente. Utilize apenas passos padrão, sem passos de SQL ou de código.

O laboratório verifica se o fluxo de trabalho é executado, se utiliza apenas passos padrão e se o resumo está correto para o mês e, de novo, para outro mês.

## Especialista

O laboratório de Especialista tem limite de tempo: dispõe de 4 horas a partir do momento em que o inicia.

### Leia por esta ordem

1. [Depurar um fluxo de trabalho](/pt-pt/get-started/tutorials/debug-a-workflow/)
2. [Ver o registo do fluxo de trabalho](/pt-pt/guides/workflows/viewing-workflow-log/)
3. [Gerir erros de passos](/pt-pt/guides/workflows/managing-step-errors/)
4. [Pré-visualizar os dados de um passo](/pt-pt/guides/workflows/preview-step-data/)
5. [Otimizar um fluxo de trabalho](/pt-pt/guides/workflows/optimize-a-workflow/)
6. [Passos de fluxo de trabalho](/pt-pt/reference/workflow-steps/), em particular [Table Inner Join](/pt-pt/reference/workflow-steps/tables/table-inner-join/)

### O que o laboratório pede

O laboratório chama-se *Engenharia de dados Especialista: corrigir e acelerar a compilação noturna*.

Um fluxo de trabalho noturno deixou de ser executado e, antes disso, era demasiado lento. Lê o registo da execução, encontra todas as causas e corrige o fluxo de trabalho para que tenha êxito, produza o resumo correto e termine numa pequena fração do tempo anterior. As linhas sem conta ficam de fora, e as contas listadas duas vezes não podem inflacionar as contagens. Utilize apenas passos padrão e deixe as tabelas de entrada como estão.

O laboratório verifica se o fluxo de trabalho é executado, se utiliza apenas passos padrão, se o resumo está correto, se as tabelas de entrada permanecem inalteradas e se o fluxo de trabalho é suficientemente rápido.
