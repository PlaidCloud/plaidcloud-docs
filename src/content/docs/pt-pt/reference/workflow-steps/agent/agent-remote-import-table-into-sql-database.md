---
title: Agent Remote Import Table into SQL Database
description: Importe dados de tabelas do PlaidCloud para bases de dados SQL remotas através de um agente PlaidLink para um carregamento seguro de dados atrás de firewalls.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-import-table-into-sql-database.md
---

## Descrição



Envia uma tabela de projeto do PlaidCloud para uma base de dados acessível apenas através de um agente PlaidLink. O agente recebe os dados do PlaidCloud e efetua o carregamento localmente — útil para manter sincronizada com a análise do PlaidCloud uma base de dados operacional nas instalações.

Utilização típica: o PlaidCloud produz uma previsão ou um resultado de alocação atualizados e o agente carrega-os no ERP, no data mart ou na base de dados de relatórios operacionais nas instalações.


## Como os dados chegam ao agente

Um agente PlaidLink na versão 1.2.33 ou posterior recebe as linhas da tabela num único ficheiro Parquet. Os números, as datas, os carimbos de data/hora e os valores verdadeiro/falso chegam com os seus próprios tipos. As outras colunas, como as de hora, intervalo e JSON, chegam como texto. Um valor de texto vazio chega vazio (NULL), como sempre aconteceu.

Um agente mais antigo recebe as linhas num ficheiro comprimido delimitado por tabulações, como antes. [Atualize o agente](/pt-pt/reference/cli/plaidlink/upgrade/) para receber Parquet.

## Exemplos

Ainda sem exemplos...
