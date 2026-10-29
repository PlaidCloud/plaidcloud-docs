---
title: Dimension Export
description: Exporte dados de dimensão do PlaidCloud em uma etapa de fluxo de trabalho para salvar estruturas hierárquicas como arquivos ou transferi-las para outros sistemas.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-export.md
---

## Descrição

Achata uma dimensão em uma tabela tabular do PlaidCloud — uma linha por membro, com colunas para pai, nível, valor, aliases e propriedades. Use esta etapa quando precisar consultar, juntar ou alimentar a estrutura da dimensão em sistemas downstream que não conseguem ler diretamente o formato hierárquico do PlaidCloud.

Uso comum: exporte a dimensão como uma tabela e depois grave-a em um sistema externo (ferramenta de BI, banco de dados de relatórios, entrega de arquivos) com uma etapa de exportação comum.

## Exportação de todas as hierarquias

Escolha **Todas as hierarquias** para trazer todas as hierarquias para uma única tabela. O resultado ganha uma coluna `hierarchy` que indica a qual hierarquia cada linha pertence, e as linhas são ordenadas com a hierarquia principal primeiro, seguida das alternativas em ordem alfabética.
