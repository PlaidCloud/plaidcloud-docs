---
title: Document - Remote Delete File
description: Elimine ficheiros em sistemas remotos através de um agente PlaidLink em fluxos de trabalho do PlaidCloud para uma gestão segura de ficheiros atrás de firewalls.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## Descrição



Elimina um ficheiro num sistema de ficheiros que está atrás de uma firewall, acedido através de um agente PlaidLink. O agente efetua a eliminação localmente no sistema de ficheiros das instalações.

Utilize-o para a limpeza após operações de exportação nas instalações, ou como parte de integrações baseadas em ficheiros que precisam de remover os ficheiros de origem já processados.


## Exemplos


Primeiro, faça uma seleção no menu pendente “Agent to Use”. Em seguida, introduza o caminho do ficheiro ou da pasta em “File or Folder Path for Delete”. Por fim, selecione “Save and Run Step”.

## Caminho em falta

Com um agente PlaidLink atualizado, um caminho que não existe no sistema remoto termina o passo com um aviso, `Nothing to delete at <path>`, em vez de um erro, e o fluxo de trabalho continua. Os agentes que não foram atualizados continuam a fazer o passo falhar.

Um caminho vazio termina o passo com o aviso `No path to delete; nothing deleted.` e não elimina nada. Isto inclui um caminho cuja pasta é uma variável que não resultou em nada nesta execução, como `{folder}/archive`.

Um caminho que seja a raiz do sistema de ficheiros ou uma pasta superior ao diretório de trabalho do agente PlaidLink (`/`, `C:\`, uma raiz de partilha como `\\server\share`, ou `..`) faz o passo falhar antes de eliminar o que quer que seja, com `Refusing to delete the filesystem root <path>.` ou `Refusing to delete <path>, which contains the agent's working directory.` As raízes e `..` são recusadas com os agentes PlaidLink que já tem implementados; um agente atualizado recusa também qualquer outra pasta que contenha o seu diretório de trabalho, avaliada face ao seu próprio sistema de ficheiros.
