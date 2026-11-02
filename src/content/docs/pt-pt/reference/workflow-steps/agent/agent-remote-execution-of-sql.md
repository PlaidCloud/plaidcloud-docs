---
title: Passo Agent Remote Execution of SQL
description: Execute consultas SQL remotamente através de um agente PlaidLink em fluxos de trabalho do PlaidCloud para operações seguras em bases de dados protegidas por firewalls.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## Descrição

Executa SQL numa base de dados a que o PlaidCloud só consegue chegar através de um agente PlaidLink — normalmente porque a base de dados está atrás de uma firewall, numa rede privada ou num centro de dados local. O agente executa o SQL localmente e comunica o sucesso ou a falha ao PlaidCloud.

Use-o para acionar procedimentos armazenados remotos, rotinas de atualização ou tarefas de manutenção como parte de um fluxo de trabalho do PlaidCloud sem expor a base de dados de origem à Internet pública.

## Pré-visualizar a consulta

No passo **Execução remota: SQL**, **Pré-visualização** no separador **Origem** mostra até 100 linhas sem executar a instrução, para que possa verificar um `SELECT` antes de o executar. A pré-visualização preenche as variáveis da mesma forma que uma execução, mas não suporta formatos de variáveis como `{x:>9}`. Só lê dados: uma instrução que escreve, ou uma função que a pré-visualização não consegue verificar como só de leitura, é recusada com *A pré-visualização só suporta funções SQL padrão. Execute o passo para ver os resultados.* A pré-visualização não está disponível num projeto bloqueado, nem para instruções que usam marcadores `:name` com uma tabela de indutores. Não está disponível para o passo baseado em agente que esta página descreve, porque só o agente consegue chegar a essas bases de dados.

## Executar uma instrução uma vez por linha

O passo **Execução remota: SQL**, que se liga diretamente à base de dados em vez de através de um agente, pode executar a sua instrução uma vez por cada linha de uma tabela, por exemplo para chamar um procedimento armazenado por cada linha de entrada. Defina **Executar o SQL** como **Uma vez por linha**, escolha uma **Tabela de indutores** e preencha **Parâmetros**. Escreva cada valor na instrução como um marcador `:name`, como `CALL load_region(:region, :period)`, e mapeie cada marcador em **Parâmetro** para a **Coluna de drivers** que o fornece. Cada valor é enviado para a base de dados como um parâmetro associado, nunca colado no texto da instrução.

Cada parâmetro precisa de um nome e de uma coluna do indutor, e um parâmetro não pode ser listado duas vezes. O formulário avisa quando um `:name` na instrução não tem mapeamento ou quando um mapeamento não está na instrução. A tabela de indutores tem de ser uma tabela, não uma vista. Uma tabela de indutores sem linhas termina com um aviso e não executa nada, e uma com mais de 100 000 linhas faz o passo falhar sem executar nenhuma delas, por isso filtre-a primeiro.

## Executar um script numa transação

No passo **Execução remota: SQL**, marque **Executar o SQL como um script de instruções numa transação: todas aplicadas ou nenhuma** (`transaction`) para executar o SQL como um script de instruções, uma após outra, numa única transação, de modo que todas as instruções sejam aplicadas ou nenhuma.
