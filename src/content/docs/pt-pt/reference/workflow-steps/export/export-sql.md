---
title: Passo Export to SQL
description: Exporte dados para bases de dados SQL externas a partir de um passo de fluxo de trabalho do PlaidCloud para carregar resultados em sistemas de bases de dados a jusante.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-sql.md
---

## Descrição



Escreve uma tabela de projeto do PlaidCloud numa conta de documentos como um ficheiro SQL com instruções CREATE TABLE e INSERT. Útil quando precisa de entregar dados a um sistema que ingere scripts SQL em vez de CSV ou Parquet.

Para carregar diretamente numa base de dados remota, use antes o passo de exportação de base de dados adequado ou [Agent Remote Import](/pt-pt/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database/) — são mais rápidos e não exigem um ficheiro intermédio.

## Pré-visualização

**Pré-visualização** mostra até 100 linhas da consulta que o passo lê da tabela de origem, sem a executar. Clique em **Pré-visualização** no separador **Origem**. Se houver mais linhas, a pré-visualização indica que mostra as primeiras linhas e que tem de executar o passo para as ler todas. A pré-visualização preenche as variáveis da mesma forma que uma execução, mas não suporta formatos de variáveis como `{x:>9}`.

A pré-visualização só lê dados. Se a consulta usar uma função que a pré-visualização não consegue verificar como só de leitura, mostra *A pré-visualização só suporta funções SQL padrão. Execute o passo para ver os resultados.* Execute o passo para ver o resultado. A pré-visualização não está disponível num projeto bloqueado.

## Definições adicionais

Em **Ordem das linhas**, **Ordenar linhas por** (`sort_columns`) ordena as linhas escritas por estas colunas de origem, a primeira chave primeiro, cada uma com uma definição de **Coluna**, **Ascendente** e **Nulos**. Uma coluna-chave não precisa de ser escrita. **Nulos** assume por predefinição primeiro em ordem ascendente e último em ordem descendente. Não é usado com **Resumir** nem **Distinto**.

## Exemplos


Ainda não há exemplos...
