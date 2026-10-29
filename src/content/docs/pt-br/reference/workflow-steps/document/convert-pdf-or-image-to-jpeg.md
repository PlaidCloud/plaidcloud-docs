---
title: Convert PDF or Image to JPEG
description: Converta páginas de PDF ou imagens para o formato JPEG em uma etapa de fluxo de trabalho do PlaidCloud para uma saída compatível com a web e tarefas de processamento de imagens.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

Converte um PDF ou uma imagem em um JPEG. A primeira página de um PDF se torna o JPEG; uma imagem é recodificada, e uma imagem com várias páginas ou quadros, como um TIFF digitalizado, é convertida a partir do primeiro.

## Entradas

- **Arquivo ou diretório de entrada** — um PDF ou uma imagem (PNG, GIF, TIFF, JPEG ou HEIC), ou uma pasta deles, em uma conta de documentos.
- **Arquivo ou diretório de saída** — onde o JPEG é gravado.

## Saída

Um JPEG por arquivo de entrada. No caso de uma pasta, o JPEG de cada arquivo é gravado em uma pasta com o nome do caminho de saída, sem a extensão, com o nome do próprio arquivo de origem.

## Observações

- Um arquivo de qualquer outro tipo faz a etapa falhar, informando os tipos que ela aceita.
- Se o caminho de entrada não existir ou não tiver arquivos, a etapa termina com um aviso que informa o caminho e não processa nada, e o fluxo de trabalho continua.
- O caminho de saída não pode ser o caminho de entrada.

## Usos comuns

- Gerar imagens de pré-visualização para exibição na web
- Produzir versões somente imagem de PDFs para sistemas que não processam PDF

## Relacionados

- [Convert image to PDF](/pt-br/reference/workflow-steps/document/convert-image-to-pdf/)
- [Compress PDF](/pt-br/reference/workflow-steps/document/compress-pdf/)
- [Crop image to headshot](/pt-br/reference/workflow-steps/document/crop-image-to-headshot/)
