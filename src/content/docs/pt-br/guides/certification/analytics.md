---
title: Trilha de aprendizagem de Análise
description: O que ler antes dos laboratórios Profissional e Especialista de Análise do PlaidCloud e o que cada laboratório pede que você faça.
sidebar:
  label: Análise
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/analytics.md
---

A trilha de Análise trata de métricas que dão uma única resposta certa, não importa como sejam detalhadas, e de significados compartilhados entre tabelas. Comece pela trilha de aprendizagem de [Fundamentos](/pt-br/guides/certification/foundations/). Para saber como os laboratórios funcionam, consulte [Certificação PlaidCloud](/pt-br/guides/certification/).

## Profissional

### Leia nesta ordem

1. [Executar um fluxo de trabalho](/pt-br/guides/workflows/run-a-workflow/)
2. [Ver o log do fluxo de trabalho](/pt-br/guides/workflows/viewing-workflow-log/)
3. [Definições de métricas](/pt-br/integrations/ai-coding-agents/metric-definitions/), incluindo como derivar uma métrica de outras
4. [Crie um painel a partir de uma tabela publicada](/pt-br/get-started/tutorials/build-a-dashboard/), para o painel opcional

### O que o laboratório pede

O laboratório se chama *Análise: definir métricas para três perguntas*.

Você executa um fluxo de trabalho que prepara uma tabela de vendas e, em seguida, define métricas nessa tabela, cada uma com região e canal na sua granularidade: receita por região, valor médio dos pedidos por canal, derivado de uma contagem de pedidos, e custo como parcela da receita por região, derivado de uma métrica de custo. Cada métrica é construída sobre a tabela preparada, não sobre a bruta. Um painel com as três respostas é um bom próximo passo, mas não é avaliado.

O laboratório verifica se o fluxo de trabalho é executado e se cada uma das três métricas dá a resposta certa.

## Especialista

O laboratório Especialista tem tempo limitado: você tem 4 horas a partir do momento em que o inicia.

### Leia nesta ordem

1. [Definições de métricas](/pt-br/integrations/ai-coding-agents/metric-definitions/)
2. [Modelo de dados e elementos de projeto](/pt-br/guides/projects/data-model/)
3. [Caminhos de análise](/pt-br/integrations/ai-coding-agents/analysis-paths/)

### O que o laboratório pede

O laboratório se chama *Análise Especialista: métricas que concordam*.

Duas métricas dão respostas diferentes dependendo de como são detalhadas, e o total da receita é maior do que a soma dos pedidos. Você as repara para que cada uma retorne uma única resposta correta por região e por produto, mantendo seus nomes. Em seguida, transforma as colunas que significam a mesma coisa em um único elemento compartilhado: um para região, nas tabelas que a guardam com nomes de coluna diferentes, e um para produto.

O laboratório verifica se o fluxo de trabalho é executado, se a receita por região e por produto e as unidades por produto estão certas e se os elementos cobrem as colunas certas.
