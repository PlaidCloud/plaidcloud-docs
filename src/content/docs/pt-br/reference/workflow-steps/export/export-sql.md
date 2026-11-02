---
title: Etapa Export to SQL
description: Exporte dados para bancos de dados SQL externos a partir de uma etapa de fluxo de trabalho do PlaidCloud para carregar resultados em sistemas de banco de dados downstream.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Descrição



Grava uma tabela de projeto do PlaidCloud em uma conta de documentos como um arquivo SQL contendo instruções CREATE TABLE e INSERT. Útil quando você precisa entregar dados a um sistema que ingere scripts SQL em vez de CSV ou Parquet.

Para carregar diretamente em um banco de dados remoto, use a etapa de exportação de banco de dados apropriada ou [Agent Remote Import](/pt-br/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/); elas são mais rápidas e não exigem um arquivo intermediário.

## Pré-visualização

**Pré-visualização** mostra até 100 linhas da consulta que a etapa lê da tabela de origem, sem executá-la. Clique em **Pré-visualização** na guia **Origem**. Se houver mais linhas, a pré-visualização informa que mostra as primeiras linhas e que você precisa executar a etapa para ler todas. A pré-visualização preenche as variáveis do mesmo modo que uma execução, mas não oferece suporte a formatos de variável como `{x:>9}`.

A pré-visualização apenas lê dados. Se a consulta usar uma função que a pré-visualização não consegue verificar como somente leitura, ela mostra *A pré-visualização só oferece suporte a funções SQL padrão. Execute a etapa para ver os resultados.* Execute a etapa para ver o resultado. A pré-visualização não está disponível em um projeto bloqueado.

## Configurações adicionais

Em **Ordem das linhas**, **Ordenar linhas por** (`sort_columns`) ordena as linhas gravadas por estas colunas de origem, a primeira chave primeiro, cada uma com uma configuração de **Coluna**, **Crescente** e **Nulos**. Uma coluna-chave não precisa ser gravada. **Nulos** assume por padrão primeiro em ordem crescente e último em ordem decrescente. Não é usada com **Resumir** ou **Distintos**.

## Exemplos


Ainda não há exemplos...
