---
title: Convert Image to PDF
description: Converta ficheiros de imagem em documentos PDF num passo de fluxo de trabalho do PlaidCloud, para uma saída de documentos normalizada e em formatos prontos para arquivo.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

Transforma uma imagem (PNG, GIF, TIFF, JPEG ou HEIC) num PDF de uma página, ou reajusta um PDF existente a um tamanho de página padrão.

## Entradas

- **Ficheiro ou diretório de entrada** — uma imagem ou um PDF, ou uma pasta deles, numa conta de documentos.
- **Destino** — onde o PDF é escrito.
- **Tamanho da página** — US Letter, US Legal, A3, A4 ou A5.
- **Compressão** — **Lossy** reduz as imagens à resolução de ecrã e pode reduzir drasticamente o ficheiro; **Lossless**, a predefinição, mantém exatamente os dados da imagem.

## Como funciona

- Uma imagem é colocada numa página do tamanho escolhido, redimensionada para caber nela sem alterar as proporções. Uma imagem com várias páginas ou fotogramas, como um TIFF digitalizado, é convertida a partir do primeiro.
- Com **Lossy**, o resultado é depois comprimido, e um PDF de entrada é ajustado ao tamanho de página escolhido à medida que é comprimido.
- Com **Lossless**, um PDF de entrada passa sem alterações, mantendo o seu próprio tamanho de página.

## Saída

Um PDF por ficheiro de entrada. No caso de uma pasta, o PDF de cada ficheiro é escrito numa pasta com o nome do destino, sem a extensão, com o nome do próprio ficheiro de origem. Para combinar vários num único documento, faça seguir este passo de [Merge multiple PDFs](/pt-pt/reference/workflow-steps/document/merge-multiple-pdfs/).

## Notas

- Se o caminho de entrada não existir ou não tiver ficheiros, o passo termina com um aviso que indica o caminho e não processa nada, e o fluxo de trabalho continua.
- O destino não pode ser o caminho de entrada.

## Utilizações comuns

- Normalizar imagens de recibos ou faturas num formato de arquivo
- Preparar imagens de prova para sistemas que só aceitam PDF como entrada

## Relacionado

- [Convert PDF or image to JPEG](/pt-pt/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Compress PDF](/pt-pt/reference/workflow-steps/document/compress-pdf/)
- [Merge multiple PDFs](/pt-pt/reference/workflow-steps/document/merge-multiple-pdfs/)
