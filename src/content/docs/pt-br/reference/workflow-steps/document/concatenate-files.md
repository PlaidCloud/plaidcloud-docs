---
title: Concatenate Files
description: Concatene vários arquivos em um único arquivo em uma etapa de fluxo de trabalho do PlaidCloud para combinar saídas de texto, CSV ou de outros documentos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

Combina dois ou mais arquivos de uma conta de documentos em um único arquivo de saída. Opera byte a byte — é útil para formatos de texto simples (CSV, arquivos de log, JSON Lines) em que a simples concatenação produz uma saída válida.

## Entradas

- **Arquivos de origem** — lista de arquivos a concatenar, em ordem
- **Caminho de saída** — destino do arquivo combinado
- **Separador** — sequência de bytes opcional inserida entre os arquivos de origem (geralmente uma quebra de linha)

## Saída

Um único arquivo com o conteúdo de todos os arquivos de origem na ordem listada, unidos pelo separador configurado.

Um arquivo de origem que não existe fica de fora do arquivo combinado, e a etapa termina com um aviso que o identifica, de modo que o fluxo de trabalho continua.

## Usos comuns

- Combinar arquivos de log diários em um arquivo mensal
- Mesclar arquivos CSV que compartilham o mesmo esquema (remova os cabeçalhos de todos, exceto do primeiro)
- Juntar exportações JSON Lines de várias origens antes do processamento

## Não é indicado para

- PDFs — use [Merge multiple PDFs](/pt-br/reference/workflow-steps/document/merge-multiple-pdfs/)
- Formatos binários com cabeçalhos (XLSX, ZIP, arquivos de imagem) — concatenar bytes não produz um arquivo válido

## Relacionados

- [Merge multiple PDFs](/pt-br/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Guia de documentos](/pt-br/guides/documents/)
