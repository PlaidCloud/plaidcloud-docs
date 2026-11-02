---
title: Export to SQL (passo)
description: Exporte dados para bases de dados SQL externas a partir de um passo de fluxo de trabalho do PlaidCloud, para carregar os resultados em sistemas de bases de dados a jusante.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Descrição



Escreve uma tabela de projeto do PlaidCloud numa conta de documentos como um ficheiro SQL com instruções CREATE TABLE e INSERT. É útil quando precisa de entregar dados a um sistema que ingere scripts SQL em vez de CSV ou Parquet.

Para carregar diretamente numa base de dados remota, utilize antes o passo de exportação de base de dados adequado ou o passo [Agent Remote Import Table into SQL Database](/pt-pt/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/), que são mais rápidos e não exigem um ficheiro intermédio.

## Pré-visualização

A **Pré-visualização** no separador **Origem** mostra até 100 linhas da tabela de origem sem executar o passo. Se a tabela tiver mais linhas, a pré-visualização indica que mostra as primeiras linhas. Se a tabela de origem ainda não existir, a Pré-visualização indica que não há nada para pré-visualizar. A Pré-visualização não está disponível num projeto bloqueado.

## Definições adicionais

Em **Ordem das linhas**, **Ordenar linhas por** (`sort_columns`) ordena as linhas escritas por estas colunas de origem, começando pela primeira chave, cada uma com uma definição de **Coluna**, **Ascendente** e **Nulos**. Uma coluna de chave não tem de ser escrita. **Nulos** é, por predefinição, primeiro em ordem ascendente e último em ordem descendente. Não é utilizado com **Resumir** nem **Distinto**.

## Exemplos


Ainda sem exemplos...
