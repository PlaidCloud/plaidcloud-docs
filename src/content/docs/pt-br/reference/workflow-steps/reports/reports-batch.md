---
title: Reports Batch
description: Gere relatórios em PDF em lote a partir de uma etapa de fluxo de trabalho do PlaidCloud para produzir vários relatórios a partir de modelos com diferentes entradas de dados.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## Descrição



Renderiza vários relatórios em PDF a partir de um único modelo RML, orientado por uma tabela de controle. É produzido um relatório por linha da tabela de controle, e os valores das colunas de cada linha são usados como parâmetros na renderização daquele relatório.

Uso comum: extratos de clientes (um PDF por cliente), demonstrações financeiras por unidade (um PDF por unidade de negócios), faturas (um PDF por pedido). Compare com [Report Single](/pt-br/reference/workflow-steps/reports/report-single/) para a geração de relatórios avulsos.


## Nomes que o Modelo Lê

O modelo lê cada fonte da guia **Dados do relatório**, e cada coluna de destino do mapeamento **Fonte de dados dos valores de registro do lote**, pelo respectivo nome. Não há seção de constantes: cada linha do lote fornece os valores do modelo para o seu relatório. As novas fontes são nomeadas `new_source`, `new_source_2` e assim por diante, e o modelo pode lê-las como estão.


## O Que É Verificado ao Salvar

Todo nome de fonte e de coluna do lote deve ser informado, exclusivo e legível pelo modelo — as mesmas regras de [Report Single](/pt-br/reference/workflow-steps/reports/report-single/), com colunas do lote no lugar de constantes: *Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

Salvar com uma tabela de origem do lote escolhida, mas com o mapeamento do lote vazio, preenche o mapeamento a partir dessa tabela, como Populate faria.


## Tabela de Lote Vazia

Quando a tabela de origem do lote não tem linhas, a etapa termina com sucesso, com um aviso que nomeia a tabela do lote, e nenhum relatório é produzido.


## Exemplos

Ainda não há exemplos...
