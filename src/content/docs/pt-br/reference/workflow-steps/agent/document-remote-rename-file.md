---
title: Etapa Document - Remote Rename File
description: Renomeie arquivos em sistemas remotos por meio de um agente PlaidLink em fluxos de trabalho do PlaidCloud para gerenciamento seguro de arquivos atrás de firewalls.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## Descrição



Renomeia ou move um arquivo em um sistema de arquivos remoto por meio de um agente PlaidLink. Opera inteiramente no lado local; nenhum dado é transferido de ou para o PlaidCloud.

Padrão comum: renomear um arquivo de origem para marcá-lo como “processado” depois que uma etapa de importação remota é bem-sucedida, para que o mesmo fluxo de trabalho não o importe novamente na próxima execução.


## Exemplos


Primeiro, faça uma seleção na lista suspensa “Agent to Use”. 



Em seguida, informe “Source Path” e “Destination Path”. 



Por fim, selecione “Save and Run Step”.

## Origem ausente

Com um agente PlaidLink atualizado, uma origem que não existe no sistema remoto termina a etapa com o aviso `No file or folder found at <path>; nothing renamed`, em vez de um erro, e o fluxo de trabalho continua. Os agentes que não foram atualizados ainda fazem a etapa falhar.

Um caminho de origem vazio termina a etapa com o aviso `No path to rename from; nothing renamed.`, inclusive quando uma pasta no caminho é uma variável que não resolveu para nada nesta execução.

Uma origem que seja a raiz do sistema de arquivos ou uma pasta pai do diretório de trabalho do agente PlaidLink (`/`, `C:\`, a raiz de um compartilhamento como `\\server\share`, ou `..`) faz a etapa falhar com `Refusing to rename from the filesystem root <path>.` ou `Refusing to rename from <path>, which contains the agent's working directory.` Um caminho de destino vazio faz a etapa falhar com `No destination path for the rename; it would write into the agent's working directory.` Renomear para a raiz de uma unidade ou de um compartilhamento, como `E:\` ou `\\nas\drop`, funciona. As raízes e `..` são recusadas pelos agentes PlaidLink que você já implantou; um agente atualizado também recusa qualquer outra pasta que contenha seu diretório de trabalho, avaliada em relação ao seu próprio sistema de arquivos.
