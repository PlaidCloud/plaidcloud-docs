---
title: Compress PDF
description: Compacte arquivos PDF em uma etapa de fluxo de trabalho do PlaidCloud para reduzir o tamanho do arquivo mantendo a qualidade do documento e economizando armazenamento.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

Reduz o tamanho de um PDF armazenado em uma conta de documentos. É útil para diminuir documentos digitalizados grandes antes de arquivá-los, anexá-los a notificações ou movê-los entre contas de documentos.

## Entradas

- **Arquivo ou diretório de entrada** — um PDF, ou uma pasta de PDFs, em uma conta de documentos.
- **Arquivo ou diretório de saída** — onde o PDF compactado é gravado.

## Como funciona

O PDF é reescrito com as imagens reduzidas à resolução de tela (72 dpi) e com as fontes incorporadas como subconjuntos, o que pode reduzir drasticamente documentos digitalizados; o texto continua nítido. As páginas são ajustadas ao tamanho US Letter.

## Saída

Um PDF compactado no caminho de saída. No caso de uma pasta, cada PDF é gravado abaixo do caminho de saída, mantendo sua posição em relação à pasta de entrada.

## Observações

- O caminho de saída não pode ser o caminho de entrada, de modo que a origem nunca é sobrescrita.
- Se o caminho de entrada não existir ou não tiver arquivos, a etapa termina com um aviso que informa o caminho e não processa nada, e o fluxo de trabalho continua.
- Um PDF que não pode ser compactado faz a etapa falhar, informando o arquivo e o motivo.

## Usos comuns

- Reduzir faturas, recibos ou contratos digitalizados antes do armazenamento de longo prazo
- Reduzir o tamanho do PDF antes de enviá-lo por e-mail ou anexá-lo a notificações
- Preparar documentos para envio a sistemas downstream com limite de tamanho

## Relacionados

- [Convert PDF or image to JPEG](/pt-br/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/pt-br/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Guia de documentos](/pt-br/guides/documents/)
