---
title: Report Single
description: Gere um único relatório PDF a partir de um passo de fluxo de trabalho do PlaidCloud, com modelos, origens de dados e opções de esquema configuráveis.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## Descrição



Gera um relatório PDF a partir de um modelo RML (Report Markup Language), preenchido com dados de uma ou mais tabelas do PlaidCloud. Utilize-o para relatórios formais e formatados — faturas, demonstrações financeiras, declarações regulamentares, resumos com a imagem da marca.

O modelo RML define o esquema (tamanho da página, tipos de letra, texto fixo, posição das tabelas); as tabelas de entrada fornecem os dados variáveis. Compare com [Reports Batch](/pt-pt/reference/workflow-steps/reports/reports-batch/) quando um modelo tem de produzir muitos relatórios (por exemplo, um por cliente).


## Nomes lidos pelo modelo

O modelo lê cada origem do separador **Dados do relatório**, e cada constante em **Constantes do relatório (valores fixos)**, pelo respetivo nome. As novas origens chamam-se `new_source`, `new_source_2` e assim sucessivamente, nomes que o modelo consegue ler tal como estão; mude-lhes o nome para indicar o que contêm.


## O que é verificado ao guardar

Todos os nomes de origens e constantes têm de ser:

- **Indicados** — um nome em branco é recusado.
- **Próprios** — duas origens, duas constantes, ou uma origem e uma constante não podem partilhar o mesmo nome, porque o modelo veria apenas uma delas: *Source name 'sales' is also a constant name; rename one of them.*
- **Legíveis pelo modelo** — letras, dígitos e carateres de sublinhado, começando por uma letra ou um sublinhado: *Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **Não ser uma palavra reservada pelo modelo** — `True`, `False`, `None`, `true`, `false`, `none`, `not` e `self` são lidas como algo diferente dos seus dados: *Source name 'self' is a word the template reserves, so it can't be read as a name.*


## Exemplos

Ainda sem exemplos...
