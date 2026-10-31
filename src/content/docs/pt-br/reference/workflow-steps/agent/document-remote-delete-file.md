---
title: Etapa Document - Remote Delete File
description: Exclua arquivos em sistemas remotos por meio de um agente PlaidLink em fluxos de trabalho do PlaidCloud para gerenciamento seguro de arquivos atrás de firewalls.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## Descrição



Exclui um arquivo em um sistema de arquivos que fica atrás de um firewall, acessado por meio de um agente PlaidLink. O agente executa a exclusão localmente no sistema de arquivos local.

Use esta etapa para a limpeza após operações de exportação locais, ou como parte de integrações baseadas em arquivos que precisam remover os arquivos de origem já processados.


## Exemplos


Primeiro, faça uma seleção na lista suspensa “Agent to Use”. Em seguida, informe o caminho do arquivo ou da pasta em “File or Folder Path for Delete”. Por fim, selecione “Save and Run Step”.

## Caminho ausente

Com um agente PlaidLink atualizado, um caminho que não existe no sistema remoto termina a etapa com o aviso `Nothing to delete at <path>`, em vez de um erro, e o fluxo de trabalho continua. Os agentes que não foram atualizados ainda fazem a etapa falhar.

Um caminho vazio termina a etapa com o aviso `No path to delete; nothing deleted.` e não exclui nada. Isso inclui um caminho cuja pasta é uma variável que não resolveu para nada nesta execução, como `{folder}/archive`.

Um caminho que seja a raiz do sistema de arquivos ou uma pasta pai do diretório de trabalho do agente PlaidLink (`/`, `C:\`, a raiz de um compartilhamento como `\\server\share`, ou `..`) faz a etapa falhar antes que qualquer coisa seja excluída, com `Refusing to delete the filesystem root <path>.` ou `Refusing to delete <path>, which contains the agent's working directory.` As raízes e `..` são recusadas pelos agentes PlaidLink que você já implantou; um agente atualizado também recusa qualquer outra pasta que contenha seu diretório de trabalho, avaliada em relação ao seu próprio sistema de arquivos.
