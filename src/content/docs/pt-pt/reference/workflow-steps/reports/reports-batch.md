---
title: Reports Batch
description: Gere relatórios PDF em lote a partir de um passo de fluxo de trabalho do PlaidCloud, para produzir vários relatórios a partir de modelos com diferentes dados de entrada.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## Descrição



Gera muitos relatórios PDF a partir de um único modelo RML, orientados por uma tabela de controlo. É produzido um relatório por cada linha da tabela de controlo, sendo os valores das colunas de cada linha utilizados como parâmetros na geração desse relatório.

Utilização comum: extratos de clientes (um PDF por cliente), demonstrações financeiras por unidade (um PDF por unidade de negócio), faturas (um PDF por encomenda). Compare com [Report Single](/pt-pt/reference/workflow-steps/reports/report-single/) para a geração de relatórios avulsos.


## Nomes lidos pelo modelo

O modelo lê cada origem do separador **Dados do relatório**, e cada coluna de destino do mapeamento **Origem de dados dos valores de registos do lote**, pelo respetivo nome. Não existe uma secção de constantes: cada linha do lote fornece os valores do modelo para o seu relatório. As novas origens chamam-se `new_source`, `new_source_2` e assim sucessivamente, nomes que o modelo consegue ler tal como estão.


## O que é verificado ao guardar

Todos os nomes de origens e de colunas do lote têm de ser indicados, próprios e legíveis pelo modelo — as mesmas regras de [Report Single](/pt-pt/reference/workflow-steps/reports/report-single/), com colunas do lote no lugar das constantes: *Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

Se guardar com uma tabela de origem do lote escolhida mas com o mapeamento do lote vazio, o mapeamento é preenchido a partir dessa tabela, tal como faria Populate.


## Tabela do lote vazia

Quando a tabela de origem do lote não tem linhas, o passo termina com êxito com um aviso que indica a tabela do lote, e não é produzido nenhum relatório.


## Exemplos

Ainda sem exemplos...
