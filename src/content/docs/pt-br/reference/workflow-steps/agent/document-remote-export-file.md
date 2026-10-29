---
title: Etapa Document - Remote Export File
description: Exporte arquivos para sistemas remotos por meio de um agente PlaidLink em fluxos de trabalho do PlaidCloud para transferências seguras de arquivos atrás de firewalls.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## Descrição



Grava um arquivo de uma conta de documentos do PlaidCloud em um sistema de arquivos remoto por meio de um agente PlaidLink. Útil para entregar relatórios, extrações ou arquivos processados a sistemas que o PlaidCloud não alcança diretamente — compartilhamentos de rede internos, servidores SFTP locais ou diretórios de aplicativos especializados.

O agente recebe o arquivo do PlaidCloud e o grava no destino local configurado.


## Exemplos


Primeiro, faça uma seleção na lista suspensa “Agent to Use”. Em seguida, procure o caminho do arquivo ou da pasta em “File or Folder to Export”. Depois, informe o local em “Export Path Destination”. Por fim, selecione “Save and Run Step”.

## Segurança do caminho

Um caminho de exportação vazio faz a etapa falhar com `No destination path for the export; it would write into the agent's working directory.` Isso inclui um caminho que não resolveu para nada porque uma variável nele estava vazia. Exportar para a raiz de uma unidade ou de um compartilhamento, como `E:\` ou `\\nas\drop`, funciona.

Com **Descompactar o arquivo compactado na chegada** selecionado, a etapa descompacta todos os arquivos compactados na pasta de destino e os remove. Por isso, ela recusa um destino que seja a raiz do sistema de arquivos ou um arquivo diretamente nela (`Refusing to unpack an export into the filesystem root <path>.`), ou a própria pasta do agente PlaidLink (`Refusing to unpack an export into <path>, which contains the agent's working directory.`). Escolha uma subpasta dedicada.

As verificações de caminho vazio e de raiz funcionam com os agentes PlaidLink que você já implantou. Recusar a própria pasta do agente exige um agente PlaidLink atualizado.
