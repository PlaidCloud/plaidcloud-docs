---
title: Compress PDF
description: Comprima ficheiros PDF num passo de fluxo de trabalho do PlaidCloud para reduzir o tamanho do ficheiro, mantendo a qualidade do documento, com maior eficiência de armazenamento.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

Reduz o tamanho de um PDF guardado numa conta de documentos. É útil para reduzir documentos digitalizados grandes antes de os arquivar, de os anexar a notificações ou de os mover entre contas de documentos.

## Entradas

- **Ficheiro ou diretório de entrada** — um PDF, ou uma pasta de PDF, numa conta de documentos.
- **Ficheiro ou diretório de saída** — onde o PDF comprimido é escrito.

## Como funciona

O PDF é reescrito com as imagens reduzidas à resolução de ecrã (72 dpi) e os tipos de letra incorporados como subconjuntos, o que pode reduzir drasticamente os documentos digitalizados; o texto mantém-se nítido. As páginas são ajustadas ao tamanho US Letter.

## Saída

Um PDF comprimido no caminho de saída. No caso de uma pasta, cada PDF é escrito abaixo do caminho de saída, mantendo a sua posição relativa à pasta de entrada.

## Notas

- O caminho de saída não pode ser o caminho de entrada, pelo que a origem nunca é substituída.
- Se o caminho de entrada não existir ou não tiver ficheiros, o passo termina com um aviso que indica o caminho e não processa nada, e o fluxo de trabalho continua.
- Um PDF que não possa ser comprimido faz o passo falhar, indicando o ficheiro e o motivo.

## Utilizações comuns

- Reduzir faturas, recibos ou contratos digitalizados antes do armazenamento a longo prazo
- Reduzir o tamanho do PDF antes de o enviar por e-mail ou de o anexar a notificações
- Preparar documentos para carregamento em sistemas a jusante com limite de tamanho

## Relacionado

- [Convert PDF or image to JPEG](/pt-pt/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge multiple PDFs](/pt-pt/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Guia de documentos](/pt-pt/guides/documents/)
