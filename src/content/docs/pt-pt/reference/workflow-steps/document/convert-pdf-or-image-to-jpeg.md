---
title: Convert PDF or Image to JPEG
description: Converta páginas PDF ou imagens para o formato JPEG num passo de fluxo de trabalho do PlaidCloud, para uma saída compatível com a Web e tarefas de processamento de imagem.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

Converte um PDF ou uma imagem num JPEG. A primeira página de um PDF passa a ser o JPEG; uma imagem é recodificada, e uma imagem com várias páginas ou fotogramas, como um TIFF digitalizado, é convertida a partir do primeiro.

## Entradas

- **Ficheiro ou diretório de entrada** — um PDF ou uma imagem (PNG, GIF, TIFF, JPEG ou HEIC), ou uma pasta deles, numa conta de documentos.
- **Ficheiro ou diretório de saída** — onde o JPEG é escrito.

## Saída

Um JPEG por ficheiro de entrada. No caso de uma pasta, o JPEG de cada ficheiro é escrito numa pasta com o nome do caminho de saída, sem a extensão, com o nome do próprio ficheiro de origem.

## Notas

- Um ficheiro de qualquer outro tipo faz o passo falhar, indicando os tipos que aceita.
- Se o caminho de entrada não existir ou não tiver ficheiros, o passo termina com um aviso que indica o caminho e não processa nada, e o fluxo de trabalho continua.
- O caminho de saída não pode ser o caminho de entrada.

## Utilizações comuns

- Gerar imagens de pré-visualização para apresentação na Web
- Produzir versões apenas de imagem de PDF para sistemas que não conseguem tratar PDF

## Relacionado

- [Convert image to PDF](/pt-pt/reference/workflow-steps/document/convert-image-to-pdf/)
- [Compress PDF](/pt-pt/reference/workflow-steps/document/compress-pdf/)
- [Crop image to headshot](/pt-pt/reference/workflow-steps/document/crop-image-to-headshot/)
