---
title: Etapa Agent Remote Execution of SQL
description: Execute consultas SQL remotamente por meio de um agente PlaidLink em fluxos de trabalho do PlaidCloud para operações de banco de dados seguras atrás de firewalls.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Descrição

Executa SQL em um banco de dados que o PlaidCloud só consegue alcançar por meio de um agente PlaidLink, normalmente porque o banco de dados fica atrás de um firewall, em uma rede privada ou em um data center local. O agente executa o SQL localmente e informa o sucesso ou a falha ao PlaidCloud.

Use-a para acionar stored procedures remotas, rotinas de atualização ou tarefas de manutenção como parte de um fluxo de trabalho do PlaidCloud sem expor o banco de dados de origem à internet pública.

## Pré-visualizar a consulta

Na etapa **Execução remota: SQL**, **Pré-visualização** na guia **Origem** mostra até 100 linhas sem executar a instrução, para você verificar um `SELECT` antes de executá-lo. A pré-visualização preenche as variáveis do mesmo modo que uma execução, mas não oferece suporte a formatos de variável como `{x:>9}`. Ela apenas lê dados: uma instrução que grava, ou uma função que a pré-visualização não consegue verificar como somente leitura, é recusada com *A pré-visualização só oferece suporte a funções SQL padrão. Execute a etapa para ver os resultados.* A pré-visualização não está disponível em um projeto bloqueado, nem para instruções que usam marcadores `:name` com uma tabela de direcionadores. Ela não está disponível para a etapa baseada em agente descrita nesta página, porque somente o agente consegue alcançar esses bancos de dados.

## Executar uma instrução uma vez por linha

A etapa **Execução remota: SQL**, que se conecta diretamente ao banco de dados em vez de passar por um agente, pode executar sua instrução uma vez para cada linha de uma tabela, por exemplo para chamar uma stored procedure para cada linha de entrada. Defina **Executar o SQL** como **Uma vez por linha**, escolha uma **Tabela de direcionadores** e preencha **Parâmetros**. Escreva cada valor na instrução como um marcador `:name`, como `CALL load_region(:region, :period)`, e mapeie cada marcador em **Parâmetro** para a **Coluna de direcionador** que o fornece. Cada valor é enviado ao banco de dados como um parâmetro vinculado, nunca colado no texto da instrução.

Todo parâmetro precisa de um nome e de uma coluna de direcionador, e um parâmetro não pode ser listado duas vezes. O formulário avisa quando um `:name` na instrução não tem mapeamento ou quando um mapeamento não está na instrução. A tabela de direcionadores deve ser uma tabela, não uma visão. Uma tabela de direcionadores sem linhas termina com um aviso e não executa nada, e uma com mais de 100.000 linhas faz a etapa falhar sem executar nenhuma delas, então filtre-a antes.

## Executar um script em uma transação

Na etapa **Execução remota: SQL**, marque **Executar o SQL como um script de instruções em uma transação: todas aplicadas ou nenhuma** (`transaction`) para executar o SQL como um script de instruções, uma após a outra, em uma única transação, de modo que todas as instruções sejam aplicadas ou nenhuma seja.
