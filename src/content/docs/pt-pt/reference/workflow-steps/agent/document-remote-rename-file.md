---
title: Document - Remote Rename File
description: Mude o nome de ficheiros em sistemas remotos através de um agente PlaidLink em fluxos de trabalho do PlaidCloud para uma gestão segura de ficheiros atrás de firewalls.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## Descrição



Muda o nome ou move um ficheiro num sistema de ficheiros remoto através de um agente PlaidLink. Funciona inteiramente do lado das instalações; não são transferidos dados de ou para o PlaidCloud.

Padrão comum: mudar o nome de um ficheiro de origem para o marcar como “processado” depois de um passo de importação remota ser bem-sucedido, para que o mesmo fluxo de trabalho não o volte a importar na execução seguinte.


## Exemplos


Primeiro, faça uma seleção no menu pendente “Agent to Use”. 



Em seguida, introduza “Source Path” e “Destination Path”. 



Por fim, selecione “Save and Run Step”.

## Origem em falta

Com um agente PlaidLink atualizado, uma origem que não existe no sistema remoto termina o passo com um aviso, `No file or folder found at <path>; nothing renamed`, em vez de um erro, e o fluxo de trabalho continua. Os agentes que não foram atualizados continuam a fazer o passo falhar.

Um caminho de origem vazio termina o passo com o aviso `No path to rename from; nothing renamed.`, incluindo quando uma pasta no caminho é uma variável que não resultou em nada nesta execução.

Uma origem que seja a raiz do sistema de ficheiros ou uma pasta superior ao diretório de trabalho do agente PlaidLink (`/`, `C:\`, uma raiz de partilha como `\\server\share`, ou `..`) faz o passo falhar com `Refusing to rename from the filesystem root <path>.` ou `Refusing to rename from <path>, which contains the agent's working directory.` Um caminho de destino vazio faz o passo falhar com `No destination path for the rename; it would write into the agent's working directory.` Mudar o nome para a raiz de uma unidade ou de uma partilha, como `E:\` ou `\\nas\drop`, funciona. As raízes e `..` são recusadas com os agentes PlaidLink que já tem implementados; um agente atualizado recusa também qualquer outra pasta que contenha o seu diretório de trabalho, avaliada face ao seu próprio sistema de ficheiros.
