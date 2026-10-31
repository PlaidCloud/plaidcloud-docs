---
title: Report Single
description: Gere um único relatório em PDF a partir de uma etapa de fluxo de trabalho do PlaidCloud usando modelos, fontes de dados e opções de layout configuráveis.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/report-single.md
---

## Descrição



Renderiza um relatório em PDF a partir de um modelo RML (Report Markup Language), preenchido com dados de uma ou mais tabelas do PlaidCloud. Use-a para relatórios formais e formatados — faturas, demonstrações financeiras, declarações regulatórias, resumos com a identidade da marca.

O modelo RML define o layout (tamanho da página, fontes, texto fixo, posição das tabelas); as tabelas de entrada fornecem os dados variáveis. Compare com [Reports Batch](/pt-br/reference/workflow-steps/reports/reports-batch/) quando um modelo precisar produzir vários relatórios (por exemplo, um por cliente).


## Nomes que o Modelo Lê

O modelo lê cada fonte da guia **Dados do relatório**, e cada constante em **Constantes do relatório (valores fixos)**, pelo respectivo nome. As novas fontes são nomeadas `new_source`, `new_source_2` e assim por diante, e o modelo pode lê-las como estão; renomeie-as para indicar o que contêm.


## O Que É Verificado ao Salvar

Todo nome de fonte e de constante deve ser:

- **Informado** — um nome em branco é recusado.
- **Exclusivo** — duas fontes, duas constantes, ou uma fonte e uma constante não podem compartilhar um nome, porque o modelo veria apenas uma delas: *Source name 'sales' is also a constant name; rename one of them.*
- **Legível pelo modelo** — letras, dígitos e sublinhados, começando com uma letra ou um sublinhado: *Constant name 'fiscal year' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*
- **Não ser uma palavra reservada pelo modelo** — `True`, `False`, `None`, `true`, `false`, `none`, `not` e `self` são lidas como algo diferente dos seus dados: *Source name 'self' is a word the template reserves, so it can't be read as a name.*


## Exemplos

Ainda não há exemplos...
