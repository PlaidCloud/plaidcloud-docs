---
title: Document - Remote Export File
description: Exporte ficheiros para sistemas remotos através de um agente PlaidLink em fluxos de trabalho do PlaidCloud para transferências seguras de ficheiros atrás de firewalls.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## Descrição



Escreve um ficheiro de uma conta de documentos do PlaidCloud num sistema de ficheiros remoto através de um agente PlaidLink. Útil para entregar relatórios, extrações ou ficheiros processados a sistemas que não são acessíveis diretamente a partir do PlaidCloud — unidades partilhadas internas, servidores SFTP nas instalações ou diretórios de aplicações especializadas.

O agente recebe o ficheiro do PlaidCloud e escreve-o no destino local configurado.


## Exemplos


Primeiro, faça uma seleção no menu pendente “Agent to Use”. Em seguida, procure o caminho do ficheiro ou da pasta em “File or Folder to Export”. Depois, introduza a localização em “Export Path Destination”. Por fim, selecione “Save and Run Step”.

## Segurança do caminho

Um caminho de exportação vazio faz o passo falhar com `No destination path for the export; it would write into the agent's working directory.` Isto inclui um caminho que resultou em nada porque uma variável nele estava vazia. Exportar para a raiz de uma unidade ou de uma partilha, como `E:\` ou `\\nas\drop`, funciona.

Com **Descomprimir o arquivo à chegada** selecionado, o passo descompacta todos os arquivos na pasta de destino e remove-os. Por isso, recusa um destino que seja a raiz do sistema de ficheiros ou um ficheiro diretamente nela (`Refusing to unpack an export into the filesystem root <path>.`), ou a própria pasta do agente PlaidLink (`Refusing to unpack an export into <path>, which contains the agent's working directory.`). Escolha antes uma subpasta dedicada.

As verificações de caminho vazio e de raiz funcionam com os agentes PlaidLink que já tem implementados. Recusar a própria pasta do agente requer um agente PlaidLink atualizado.
