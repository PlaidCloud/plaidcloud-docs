---
title: Etapa Agent Remote Execution of SQL
description: Execute consultas SQL remotamente por meio de um agente PlaidLink em fluxos de trabalho do PlaidCloud para operações seguras em bancos de dados protegidos por firewall.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Descrição

Executa SQL em um banco de dados que o PlaidCloud só consegue acessar por meio de um agente PlaidLink — normalmente porque o banco de dados está atrás de um firewall, em uma rede privada ou em um data center local. O agente executa o SQL localmente e informa o sucesso ou a falha de volta ao PlaidCloud.

Use esta etapa para acionar procedimentos armazenados remotos, rotinas de atualização ou tarefas de manutenção como parte de um fluxo de trabalho do PlaidCloud, sem expor o banco de dados de origem à internet pública.

## Executar uma instrução uma vez por linha

A etapa **Execução remota: SQL**, que se conecta diretamente ao banco de dados em vez de passar por um agente, pode executar sua instrução uma vez para cada linha de uma tabela, por exemplo para chamar um procedimento armazenado para cada linha de entrada. Defina **Executar o SQL** como **Uma vez por linha**, escolha uma **Tabela de direcionadores** e preencha os **Parâmetros**. Escreva cada valor da instrução como um espaço reservado `:name`, como `CALL load_region(:region, :period)`, e mapeie cada espaço reservado em **Parâmetro** para a **Coluna de direcionador** que o fornece. Cada valor é enviado ao banco de dados como um parâmetro vinculado, nunca colado no texto da instrução.

Todo parâmetro precisa de um nome e de uma coluna de direcionador, e um parâmetro não pode ser listado duas vezes. O formulário avisa quando um `:name` da instrução não tem mapeamento ou quando um mapeamento não está na instrução. A tabela de direcionadores precisa ser uma tabela, não uma visão. Uma tabela de direcionadores sem linhas termina com um aviso e não executa nada, e uma com mais de 100.000 linhas faz a etapa falhar sem executar nenhuma delas, portanto filtre-a antes.

## Executar um script em uma transação

Na etapa **Execução remota: SQL**, marque **Executar o SQL como um script de instruções em uma transação: todas aplicadas ou nenhuma** (`transaction`) para executar o SQL como um script de instruções, uma após a outra, em uma única transação, de modo que todas as instruções sejam aplicadas ou nenhuma seja.
