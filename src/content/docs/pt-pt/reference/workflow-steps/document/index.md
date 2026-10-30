---
title: Passos de documentos
description: Gira documentos em fluxos de trabalho PlaidCloud com passos para conversão, cópia, mudança de nome e eliminação de ficheiros e operações com PDF.
sidebar:
  label: Passos de documentos
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

Passos de fluxo de trabalho para operar sobre ficheiros guardados em contas de documentos. Utilize-os para mover, transformar e converter documentos a par dos seus fluxos de trabalho de dados.

## Operações com ficheiros

- [Copy document file](/pt-pt/reference/workflow-steps/document/copy-document-file/) · [Copy document directory](/pt-pt/reference/workflow-steps/document/copy-document-directory/)
- [Create document directory](/pt-pt/reference/workflow-steps/document/create-document-directory/)
- [Delete document file](/pt-pt/reference/workflow-steps/document/delete-document-file/) · [Delete document directory](/pt-pt/reference/workflow-steps/document/delete-document-directory/)
- [Listagem de diretório](/pt-pt/reference/workflow-steps/document/directory-listing/) — escreve uma tabela com os ficheiros de uma pasta
- [Update Excel cells](/pt-pt/reference/workflow-steps/document/document-excel-update/) — escreve valores em células escolhidas de um livro, ou formata-as
- [Fix file extension](/pt-pt/reference/workflow-steps/document/fix-file-extension/)
- [Rename document file](/pt-pt/reference/workflow-steps/document/rename-document-file/) · [Rename document directory](/pt-pt/reference/workflow-steps/document/rename-document-directory/)

Os passos de cópia e de mudança de nome tratam uma origem em falta como normal. Quando o ficheiro, ou a pasta a copiar ou a renomear, não existe, ou a pasta está vazia, o passo não faz nada, termina com um aviso que indica o caminho e o fluxo de trabalho continua. Uma execução agendada sobre uma pasta que nesse dia não tem ficheiros deixa de falhar.

## Encriptação

- [Encrypt file · Decrypt file](/pt-pt/reference/workflow-steps/document/encrypt-decrypt-file/) — AES, Blowfish ou uma palavra-passe de livro Excel

## Operações com PDF

- [Compress PDF](/pt-pt/reference/workflow-steps/document/compress-pdf/)
- [Convert image to PDF](/pt-pt/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or image to JPEG](/pt-pt/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/pt-pt/reference/workflow-steps/document/merge-multiple-pdfs/)

## Operações com imagens

- [Crop image to headshot](/pt-pt/reference/workflow-steps/document/crop-image-to-headshot/)

## Operações com texto

- [Concatenate files](/pt-pt/reference/workflow-steps/document/concatenate-files/) — junta vários ficheiros num só
- [Document text substitution](/pt-pt/reference/workflow-steps/document/document-text-substitution/) — localizar e substituir dentro de um documento

## Conversão de codificação

- [Convert document encoding](/pt-pt/reference/workflow-steps/document/convert-document-encoding/) — escolhe a codificação de destino
- [Convert document encoding to ASCII](/pt-pt/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert document encoding to UTF-16](/pt-pt/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert document encoding to UTF-8](/pt-pt/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## Ver também

- [Convert Dashboard to PDF](/pt-pt/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Files](/pt-pt/reference/workflow-steps/document/document-delete-old-files/)
- [Contas de documentos](/pt-pt/guides/documents/adding-accounts/) — ligue contas de documentos antes de utilizar estes passos
- [Guia de documentos](/pt-pt/guides/documents/) — instruções orientadas para tarefas, para as mesmas operações
