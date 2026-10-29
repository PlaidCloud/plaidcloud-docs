---
title: Etapa Agent Remote Import Table into SQL Database
description: Importe dados de tabelas do PlaidCloud para bancos de dados SQL remotos por meio de um agente PlaidLink para carga segura de dados atrás de firewalls.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## Descrição



Envia uma tabela de projeto do PlaidCloud para um banco de dados acessível somente por meio de um agente PlaidLink. O agente recebe os dados do PlaidCloud e realiza a carga localmente — útil para manter um banco de dados operacional local sincronizado com a análise do PlaidCloud.

Uso típico: o PlaidCloud produz uma previsão atualizada ou um resultado de alocação, e o agente o carrega no ERP local, no data mart ou no banco de dados de relatórios operacionais.


## Como os dados chegam ao agente

Um agente PlaidLink na versão 1.2.33 ou posterior recebe as linhas da tabela como um único arquivo Parquet. Números, datas, carimbos de data/hora e valores verdadeiro/falso chegam com seus próprios tipos. Outras colunas, como colunas de hora, intervalo e JSON, chegam como texto. Um valor de texto vazio chega vazio (NULL), como sempre foi.

Um agente mais antigo recebe as linhas como um arquivo compactado delimitado por tabulação, como antes. [Atualize o agente](/pt-br/reference/cli/plaidlink/upgrade/) para receber Parquet.

## Exemplos

Ainda não há exemplos...
