---
title: Etapas de documento
description: Gerencie documentos em fluxos de trabalho do PlaidCloud com etapas de conversão, cópia, renomeação, exclusão de arquivos e operações com PDF.
sidebar:
  label: Etapas de documento
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

Etapas de fluxo de trabalho para operar em arquivos armazenados em contas de documentos. Use-as para mover, transformar e converter documentos junto com seus fluxos de trabalho de dados.

## Operações com arquivos

- [Copy document file](/pt-br/reference/workflow-steps/document/copy-document-file/) · [Copy document directory](/pt-br/reference/workflow-steps/document/copy-document-directory/)
- [Create document directory](/pt-br/reference/workflow-steps/document/create-document-directory/)
- [Delete document file](/pt-br/reference/workflow-steps/document/delete-document-file/) · [Delete document directory](/pt-br/reference/workflow-steps/document/delete-document-directory/)
- [Listagem de diretório](/pt-br/reference/workflow-steps/document/directory-listing/) — grava uma tabela com os arquivos de uma pasta
- [Update Excel cells](/pt-br/reference/workflow-steps/document/document-excel-update/) — grava valores em células escolhidas de uma pasta de trabalho, ou as formata
- [Fix file extension](/pt-br/reference/workflow-steps/document/fix-file-extension/)
- [Rename document file](/pt-br/reference/workflow-steps/document/rename-document-file/) · [Rename document directory](/pt-br/reference/workflow-steps/document/rename-document-directory/)

As etapas de cópia e renomeação tratam uma origem ausente como algo normal. Quando o arquivo, ou a pasta a copiar ou renomear, não existe, ou a pasta está vazia, a etapa não faz nada, termina com um aviso que informa o caminho e o fluxo de trabalho continua. Uma execução agendada sobre uma pasta que não tem arquivos naquele dia não falha mais.

## Criptografia

- [Encrypt file · Decrypt file](/pt-br/reference/workflow-steps/document/encrypt-decrypt-file/) — AES, Blowfish ou uma senha de pasta de trabalho do Excel

## Operações com PDF

- [Compress PDF](/pt-br/reference/workflow-steps/document/compress-pdf/)
- [Convert image to PDF](/pt-br/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or image to JPEG](/pt-br/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/pt-br/reference/workflow-steps/document/merge-multiple-pdfs/)

## Operações com imagens

- [Crop image to headshot](/pt-br/reference/workflow-steps/document/crop-image-to-headshot/)

## Operações com texto

- [Concatenate files](/pt-br/reference/workflow-steps/document/concatenate-files/) — une vários arquivos em um só
- [Document text substitution](/pt-br/reference/workflow-steps/document/document-text-substitution/) — localizar e substituir dentro de um documento

## Conversão de codificação

- [Convert document encoding](/pt-br/reference/workflow-steps/document/convert-document-encoding/) — escolha a codificação de destino
- [Convert document encoding to ASCII](/pt-br/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert document encoding to UTF-16](/pt-br/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert document encoding to UTF-8](/pt-br/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## Veja também

- [Convert Dashboard to PDF](/pt-br/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Files](/pt-br/reference/workflow-steps/document/document-delete-old-files/)
- [Contas de documentos](/pt-br/guides/documents/adding-accounts/) — conecte contas de documentos antes de usar estas etapas
- [Guia de documentos](/pt-br/guides/documents/) — passo a passo orientado a tarefas para as mesmas operações
