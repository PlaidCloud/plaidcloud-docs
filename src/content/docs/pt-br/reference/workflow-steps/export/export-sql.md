---
title: Export to SQL (etapa)
description: Exporte dados para bancos de dados SQL externos a partir de uma etapa de fluxo de trabalho do PlaidCloud para carregar resultados em sistemas de banco de dados downstream.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Descrição



Grava uma tabela de projeto do PlaidCloud em uma conta de documentos como um arquivo SQL contendo instruções CREATE TABLE e INSERT. É útil quando você precisa entregar dados a um sistema que ingere scripts SQL em vez de CSV ou Parquet.

Para carregar diretamente em um banco de dados remoto, use a etapa de exportação de banco de dados adequada ou o [Agent Remote Import](/pt-br/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) (etapa). Elas são mais rápidas e não exigem um arquivo intermediário.

## Pré-visualização

**Pré-visualização** na guia **Origem** mostra até 100 linhas da tabela de origem sem executar a etapa. Se a tabela tiver mais linhas, a pré-visualização informa que mostra as primeiras linhas. Se a tabela de origem ainda não existir, a pré-visualização informa que não há nada para visualizar. A pré-visualização não está disponível em um projeto bloqueado.

## Configurações adicionais

Em **Ordem das linhas**, **Ordenar linhas por** (`sort_columns`) ordena as linhas gravadas por essas colunas de origem, começando pela primeira chave, cada uma com as configurações **Coluna**, **Crescente** e **Nulos**. Uma coluna-chave não precisa ser gravada. **Nulos** assume por padrão primeiro na ordem crescente e último na decrescente. Não é usado com **Resumir** ou **Distintos**.

## Exemplos


Ainda não há exemplos...
