---
title: Etapa Document - Remote Import File
description: Importe arquivos de sistemas remotos por meio de um agente PlaidLink em fluxos de trabalho do PlaidCloud para obtenção segura de arquivos atrás de firewalls.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## Descrição



Obtém um arquivo de um sistema de arquivos remoto por meio de um agente PlaidLink e o armazena em uma conta de documentos do PlaidCloud. É usada quando os arquivos de origem vêm de compartilhamentos de arquivos internos, de servidores locais ou de trás de um firewall.

O agente lê o arquivo localmente e o transmite ao PlaidCloud, onde as etapas seguintes do fluxo de trabalho podem processá-lo.


## Exemplos


Primeiro, faça uma seleção na lista suspensa “Agent to Use”. Em seguida, informe o caminho do arquivo ou da pasta em “File or Folder Path for Import”. Depois, informe a pasta de destino em “Folder Destination”. Opcionalmente, escolha uma **Compactação** para compactar o arquivo ao chegar: Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO ou Deflate (zlib). Por fim, selecione “Save and Run Step”.

## Arquivo ou pasta de origem ausente

Quando não existe nada no caminho do compartilhamento remoto, a etapa termina com o aviso `No file or folder found at <path>; nothing imported.`, em vez de um erro. O fluxo de trabalho continua para a próxima etapa, e as configurações de nova tentativa e de erro da etapa (ir para uma etapa ou continuar) não são executadas para uma origem ausente. Isso funciona com os agentes PlaidLink que você já implantou.

Um caminho vazio termina da mesma forma, com o aviso `No path to import from; nothing imported.`. Isso inclui um caminho cuja pasta é uma variável que não resolveu para nada nesta execução, como `{folder}/archive`.

Um caminho que seja a raiz do sistema de arquivos ou uma pasta pai do diretório de trabalho do agente PlaidLink (`/`, `C:\`, a raiz de um compartilhamento como `\\server\share`, ou `..`) faz a etapa falhar antes que qualquer coisa seja enviada, com `Refusing to import from the filesystem root <path>.` ou `Refusing to import from <path>, which contains the agent's working directory.` As raízes e `..` são recusadas pelos agentes PlaidLink que você já implantou; um agente atualizado também recusa qualquer outra pasta que contenha seu diretório de trabalho, avaliada em relação ao seu próprio sistema de arquivos.

Outras falhas ainda fazem a etapa falhar: permissão negada, um envio malsucedido ao PlaidCloud ou, em um agente PlaidLink atualizado, um servidor ou compartilhamento inacessível.

Como nada é importado, um documento de uma execução anterior permanece onde estava. Para executar uma etapa seguinte somente quando o arquivo deste período chegou, siga uma destas opções:

- Adicione à etapa seguinte uma [condição de etapa](/pt-br/guides/workflows/step-conditions/#condições-de-caminho-de-documento) **file exists in Document**, com o caminho do Documento definido como um caminho por período, como um que inclua o período no nome do arquivo.
- Exclua o documento importado depois que o fluxo de trabalho o utilizar, para que uma origem ausente não deixe um arquivo antigo para trás.
