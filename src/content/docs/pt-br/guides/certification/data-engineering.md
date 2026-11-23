---
title: Trilha de aprendizagem de Engenharia de dados
description: O que ler antes dos laboratórios Profissional e Especialista de Engenharia de dados do PlaidCloud e o que cada laboratório pede que você faça.
sidebar:
  label: Engenharia de dados
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

A trilha de Engenharia de dados trata de construir fluxos de trabalho corretos, guiados por variáveis e rápidos. Comece pela trilha de aprendizagem de [Fundamentos](/pt-br/guides/certification/foundations/). Para saber como os laboratórios funcionam, consulte [Certificação PlaidCloud](/pt-br/guides/certification/).

## Profissional

### Leia nesta ordem

1. [Criar fluxo de trabalho](/pt-br/guides/workflows/create-workflow/)
2. [Etapas de fluxo de trabalho](/pt-br/reference/workflow-steps/), em especial [Etapa Table Inner Join](/pt-br/reference/workflow-steps/tables/table-inner-join/) e [Etapa Table Extract](/pt-br/reference/workflow-steps/tables/table-extract/)
3. [Gerenciar variáveis de fluxo de trabalho](/pt-br/guides/workflows/manage-workflow-variables/)
4. [Reutilize seu trabalho: variáveis, macros e UDFs](/pt-br/get-started/tutorials/reuse-variables-macros-udfs/)
5. [Executar um fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/)
6. [Ver o log do fluxo de trabalho](/pt-br/guides/workflows/viewing-workflow-log/)

### O que o laboratório pede

O laboratório se chama *Engenharia de dados: construção mensal de vendas*.

Três tabelas brutas são carregadas: linhas de vendas, lojas e produtos. No fluxo de trabalho do laboratório, você constrói um resumo mensal com uma linha por região e categoria de produto, com unidades e receita, para as linhas vendidas de um mês. O mês vem de uma variável de projeto, não de um valor digitado em uma etapa: o laboratório altera a variável e executa o fluxo de trabalho novamente. Use apenas etapas padrão, sem etapas de SQL ou de código.

O laboratório verifica se o fluxo de trabalho é executado, se usa apenas etapas padrão e se o resumo está certo para o mês e novamente para outro mês.

## Especialista

O laboratório Especialista tem tempo limitado: você tem 4 horas a partir do momento em que o inicia.

### Leia nesta ordem

1. [Depure um fluxo de trabalho](/pt-br/get-started/tutorials/debug-a-workflow/)
2. [Ver o log do fluxo de trabalho](/pt-br/guides/workflows/viewing-workflow-log/)
3. [Gerenciar erros de etapas](/pt-br/guides/workflows/managing-step-errors/)
4. [Pré-visualizar dados da etapa](/pt-br/guides/workflows/preview-step-data/)
5. [Otimizar um fluxo de trabalho](/pt-br/guides/workflows/optimize-a-workflow/)
6. [Etapas de fluxo de trabalho](/pt-br/reference/workflow-steps/), em especial [Etapa Table Inner Join](/pt-br/reference/workflow-steps/tables/table-inner-join/)

### O que o laboratório pede

O laboratório se chama *Engenharia de dados Especialista: corrigir e acelerar a compilação noturna*.

Um fluxo de trabalho noturno parou de ser executado e, antes disso, estava lento demais. Você lê o log da execução, encontra todas as causas e corrige o fluxo de trabalho para que ele seja concluído com sucesso, produza o resumo certo e termine em uma pequena fração do tempo anterior. As linhas sem conta ficam de fora, e as contas listadas duas vezes não devem inflar as contagens. Use apenas etapas padrão e deixe as tabelas de entrada como estão.

O laboratório verifica se o fluxo de trabalho é executado, se usa apenas etapas padrão, se o resumo está certo, se as tabelas de entrada não foram alteradas e se o fluxo de trabalho é rápido o suficiente.
