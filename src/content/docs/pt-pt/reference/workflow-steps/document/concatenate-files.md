---
title: Concatenate Files
description: Concatene vários ficheiros num único ficheiro num passo de fluxo de trabalho do PlaidCloud, para combinar saídas de texto, CSV ou outros documentos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

Combina dois ou mais ficheiros de uma conta de documentos num único ficheiro de saída. Funciona byte a byte — útil para formatos de texto simples (CSV, ficheiros de registo, JSON Lines) em que a simples concatenação produz uma saída válida.

## Entradas

- **Ficheiros de origem** — lista de ficheiros a concatenar, por ordem
- **Caminho de saída** — destino do ficheiro combinado
- **Separador** — sequência de bytes opcional inserida entre os ficheiros de origem (normalmente uma mudança de linha)

## Saída

Um único ficheiro com o conteúdo de todos os ficheiros de origem pela ordem indicada, unidos pelo separador configurado.

Um ficheiro de origem que não exista é deixado de fora do ficheiro combinado, e o passo termina com um aviso que o identifica, pelo que o fluxo de trabalho continua.

## Utilizações comuns

- Combinar ficheiros de registo diários num arquivo mensal
- Fundir ficheiros CSV que partilham um esquema (retire os cabeçalhos de todos exceto do primeiro)
- Juntar exportações JSON Lines de várias origens antes do processamento

## Não é adequado para

- PDF — use antes [Merge multiple PDFs](/pt-pt/reference/workflow-steps/document/merge-multiple-pdfs/)
- Formatos binários com cabeçalhos (XLSX, ZIP, ficheiros de imagem) — concatenar bytes não produz um ficheiro válido

## Relacionado

- [Merge multiple PDFs](/pt-pt/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Guia de documentos](/pt-pt/guides/documents/)
