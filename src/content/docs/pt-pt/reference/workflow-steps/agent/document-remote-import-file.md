---
title: Document - Remote Import File
description: Importe ficheiros de sistemas remotos através de um agente PlaidLink em fluxos de trabalho do PlaidCloud para uma obtenção segura de ficheiros atrás de firewalls.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## Descrição



Obtém um ficheiro de um sistema de ficheiros remoto através de um agente PlaidLink e guarda-o numa conta de documentos do PlaidCloud. Utilizado quando os ficheiros de origem se encontram em partilhas de ficheiros internas, em servidores nas instalações ou atrás de uma firewall.

O agente lê o ficheiro localmente e envia-o em fluxo contínuo para o PlaidCloud, onde os passos seguintes do fluxo de trabalho o podem processar.


## Exemplos


Primeiro, faça uma seleção no menu pendente “Agent to Use”. Em seguida, introduza o caminho do ficheiro ou da pasta em “File or Folder Path for Import”. Depois, introduza a pasta de destino em “Folder Destination”. Opcionalmente, escolha uma **Compressão** para comprimir o ficheiro à medida que chega: Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO ou Deflate (zlib). Por fim, selecione “Save and Run Step”.

## Ficheiro ou pasta de origem em falta

Quando não existe nada no caminho da partilha remota, o passo termina com um aviso, `No file or folder found at <path>; nothing imported.`, em vez de um erro. O fluxo de trabalho continua para o passo seguinte, e as definições de repetição e de comportamento em caso de erro do passo (ir para um passo, ou continuar) não são aplicadas a uma origem em falta. Isto funciona com os agentes PlaidLink que já tem implementados.

Um caminho vazio termina da mesma forma, com o aviso `No path to import from; nothing imported.`. Isto inclui um caminho cuja pasta é uma variável que não resultou em nada nesta execução, como `{folder}/archive`.

Um caminho que seja a raiz do sistema de ficheiros ou uma pasta superior ao diretório de trabalho do agente PlaidLink (`/`, `C:\`, uma raiz de partilha como `\\server\share`, ou `..`) faz o passo falhar antes de ser carregado o que quer que seja, com `Refusing to import from the filesystem root <path>.` ou `Refusing to import from <path>, which contains the agent's working directory.` As raízes e `..` são recusadas com os agentes PlaidLink que já tem implementados; um agente atualizado recusa também qualquer outra pasta que contenha o seu diretório de trabalho, avaliada face ao seu próprio sistema de ficheiros.

Outras falhas continuam a fazer o passo falhar: permissão negada, um carregamento falhado para o PlaidCloud ou, num agente PlaidLink atualizado, um servidor ou partilha inacessível.

Como nada é importado, um documento de uma execução anterior permanece onde estava. Para executar um passo seguinte apenas quando o ficheiro deste período chegou, pode:

- Adicionar uma [condição de passo](/pt-pt/guides/workflows/step-conditions/#condições-de-caminho-de-documento) **file exists in Document** ao passo seguinte, com o caminho do Documento definido para um caminho por período, como um que inclua o período no nome do ficheiro.
- Eliminar o documento importado depois de o fluxo de trabalho o utilizar, para que uma origem em falta não deixe um ficheiro antigo para trás.
