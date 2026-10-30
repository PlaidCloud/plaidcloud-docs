---
title: Convert Image to PDF
description: Converta arquivos de imagem em documentos PDF em uma etapa de fluxo de trabalho do PlaidCloud para uma saída de documentos padronizada e em formatos prontos para arquivamento.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

Transforma uma imagem (PNG, GIF, TIFF, JPEG ou HEIC) em um PDF de uma página ou reajusta um PDF existente para um tamanho de página padrão.

## Entradas

- **Arquivo ou diretório de entrada** — uma imagem ou PDF, ou uma pasta deles, em uma conta de documentos.
- **Destino** — onde o PDF é gravado.
- **Tamanho da página** — US Letter, US Legal, A3, A4 ou A5.
- **Compactação** — **Lossy** reduz as imagens à resolução de tela e pode diminuir bastante o arquivo; **Lossless**, o padrão, mantém exatamente os dados da imagem.

## Como funciona

- Uma imagem é colocada em uma página do tamanho escolhido, redimensionada para caber nela sem alterar suas proporções. Uma imagem com várias páginas ou quadros, como um TIFF digitalizado, é convertida a partir do primeiro.
- Com **Lossy**, o resultado é então compactado, e um PDF de entrada é ajustado ao tamanho de página escolhido durante a compactação.
- Com **Lossless**, um PDF de entrada passa sem alterações, mantendo o próprio tamanho de página.

## Saída

Um PDF por arquivo de entrada. No caso de uma pasta, o PDF de cada arquivo é gravado em uma pasta com o nome do destino, sem a extensão, com o nome do próprio arquivo de origem. Para combinar vários em um único documento, faça esta etapa ser seguida por [Merge multiple PDFs](/pt-br/reference/workflow-steps/document/merge-multiple-pdfs/).

## Observações

- Se o caminho de entrada não existir ou não tiver arquivos, a etapa termina com um aviso que informa o caminho e não processa nada, e o fluxo de trabalho continua.
- O destino não pode ser o caminho de entrada.

## Usos comuns

- Padronizar imagens de recibos ou faturas em um formato de arquivamento
- Preparar imagens de evidência para sistemas que só aceitam PDF como entrada

## Relacionados

- [Convert PDF or image to JPEG](/pt-br/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Compress PDF](/pt-br/reference/workflow-steps/document/compress-pdf/)
- [Merge multiple PDFs](/pt-br/reference/workflow-steps/document/merge-multiple-pdfs/)
