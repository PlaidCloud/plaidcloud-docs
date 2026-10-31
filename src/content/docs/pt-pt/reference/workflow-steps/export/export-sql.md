---
title: Export to SQL (passo)
description: Exporte dados para bases de dados SQL externas a partir de um passo de fluxo de trabalho PlaidCloud, para carregar resultados em sistemas de bases de dados a jusante.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Descrição



Escreve uma tabela de projeto PlaidCloud numa conta de documentos como um ficheiro SQL com instruções CREATE TABLE e INSERT. Útil quando precisa de entregar dados a um sistema que ingere scripts SQL em vez de CSV ou Parquet.

Para carregar diretamente numa base de dados remota, utilize antes o passo de exportação de base de dados adequado ou [Agent Remote Import Table into SQL Database (passo)](/pt-pt/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) — são mais rápidos e não exigem um ficheiro intermédio.

## Definições adicionais

Em **Ordem das linhas**, **Ordenar linhas por** (`sort_columns`) ordena as linhas escritas por estas colunas de origem, começando pela primeira chave, cada uma com uma definição de **Coluna**, **Ascendente** e **Nulos**. Uma coluna de chave não tem de ser escrita. **Nulos** assume por predefinição primeiro na ordem ascendente e último na descendente. Não é utilizado com **Resumir** ou **Distinto**.

## Exemplos


Ainda não há exemplos...
