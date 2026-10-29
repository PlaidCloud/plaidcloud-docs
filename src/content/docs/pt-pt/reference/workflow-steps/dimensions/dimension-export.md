---
title: Dimension Export
description: Exporte dados de dimensão do PlaidCloud num passo de fluxo de trabalho para guardar estruturas hierárquicas como ficheiros ou transferi-las para outros sistemas.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## Descrição

Converte uma dimensão numa tabela PlaidCloud tabular — uma linha por membro, com colunas para elemento superior, nível, valor, aliases e propriedades. Use-o quando precisar de consultar, juntar ou fornecer a estrutura da dimensão a sistemas a jusante que não conseguem ler diretamente o formato hierárquico do PlaidCloud.

Utilização comum: exportar a dimensão como tabela e, em seguida, escrevê-la num sistema externo (ferramenta de BI, base de dados de relatórios, entrega de ficheiros) com um passo de exportação normal.

## Exportar todas as hierarquias

Escolha **Todas as hierarquias** para reunir todas as hierarquias numa única tabela. O resultado ganha uma coluna `hierarchy` que indica a hierarquia a que cada linha pertence, e as linhas são ordenadas com a hierarquia principal primeiro, seguida das alternativas por ordem alfabética.
