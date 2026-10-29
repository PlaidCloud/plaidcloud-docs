---
title: Export to SQL
description: Exporte dados para bancos de dados SQL externos a partir de uma etapa de fluxo de trabalho do PlaidCloud, para carregar resultados em sistemas de banco de dados posteriores.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Descrição



Grava uma tabela de projeto do PlaidCloud em uma conta de documentos como um arquivo SQL contendo instruções CREATE TABLE e INSERT. É útil quando você precisa entregar dados a um sistema que ingere scripts SQL em vez de CSV ou Parquet.

Para carregar diretamente em um banco de dados remoto, use a etapa de exportação de banco de dados apropriada ou [Agent Remote Import](/pt-br/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/); elas são mais rápidas e não exigem um arquivo intermediário.

## Configurações adicionais

Em **Ordem das linhas**, **Ordenar linhas por** (`sort_columns`) ordena as linhas gravadas por estas colunas de origem, a primeira chave primeiro, cada uma com uma configuração de **Coluna**, **Crescente** e **Nulos**. Uma coluna de chave não precisa ser gravada. **Nulos** assume por padrão primeiro em ordem crescente e por último em ordem decrescente. Não é usada com **Resumir** ou **Distintos**.

## Exemplos


Ainda não há exemplos...
