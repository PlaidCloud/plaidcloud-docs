---
title: Percurso de aprendizagem de Análise
description: O que ler antes dos laboratórios de Profissional e Especialista de Análise da certificação PlaidCloud e o que cada laboratório pede.
sidebar:
  label: Análise
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/analytics.md
---

O percurso de Análise trata de indicadores que dão uma única resposta certa, qualquer que seja a forma de os decompor, e de significados partilhados entre tabelas. Comece pelo percurso de [Fundamentos](/pt-pt/guides/certification/foundations/). Para saber como funcionam os laboratórios, consulte [Certificação PlaidCloud](/pt-pt/guides/certification/).

## Profissional

### Leia por esta ordem

1. [Executar um fluxo de trabalho](/pt-pt/guides/workflows/run-a-workflow/)
2. [Ver o registo do fluxo de trabalho](/pt-pt/guides/workflows/viewing-workflow-log/)
3. [Definições de indicadores](/pt-pt/integrations/ai-coding-agents/metric-definitions/), incluindo como derivar um indicador de outros
4. [Construir um painel de controlo a partir de uma tabela publicada](/pt-pt/get-started/tutorials/build-a-dashboard/), para o painel de controlo opcional

### O que o laboratório pede

O laboratório chama-se *Análise: definir métricas para três perguntas*.

Executa um fluxo de trabalho que prepara uma tabela de vendas e depois define indicadores nessa tabela, cada um com região e canal na sua granularidade: receitas por região, valor médio das encomendas por canal, derivado de uma contagem de encomendas, e custo como percentagem das receitas por região, derivado de um indicador de custo. Cada indicador é construído sobre a tabela preparada, não sobre a tabela em bruto. Um painel de controlo para as três respostas é um bom passo seguinte, mas não é classificado.

O laboratório verifica se o fluxo de trabalho é executado e se cada um dos três indicadores dá a resposta certa.

## Especialista

O laboratório de Especialista tem limite de tempo: dispõe de 4 horas a partir do momento em que o inicia.

### Leia por esta ordem

1. [Definições de indicadores](/pt-pt/integrations/ai-coding-agents/metric-definitions/)
2. [Modelo de dados e elementos do projeto](/pt-pt/guides/projects/data-model/)
3. [Caminhos de análise](/pt-pt/integrations/ai-coding-agents/analysis-paths/)

### O que o laboratório pede

O laboratório chama-se *Análise Especialista: métricas que concordam*.

Dois indicadores dão respostas diferentes consoante a forma como são decompostos, e o total das receitas é superior à soma das encomendas. Repara-os para que cada um devolva uma única resposta correta por região e por produto, mantendo os respetivos nomes. Depois transforma as colunas que significam o mesmo num único elemento partilhado: um para a região, nas tabelas que a contêm com nomes de coluna diferentes, e outro para o produto.

O laboratório verifica se o fluxo de trabalho é executado, se as receitas por região e por produto e as unidades por produto estão certas e se os elementos abrangem as colunas certas.
