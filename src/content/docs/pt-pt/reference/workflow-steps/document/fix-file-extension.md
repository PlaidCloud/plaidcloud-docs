---
title: Fix File Extension (passo)
description: Corrija extensões de ficheiros num passo de fluxo de trabalho PlaidCloud, detetando o tipo real do ficheiro e mudando-lhe o nome com a extensão adequada.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

Lê o que um ficheiro realmente contém e, quando isso contradiz a sua extensão, muda-lhe o nome com a extensão que o respetivo tipo normalmente tem — um PDF guardado como `.dat` passa a `.pdf`. Útil quando um sistema de origem entrega ficheiros com extensões erradas ou em falta.

## Entradas

- **Ficheiro ou diretório de entrada** — um ficheiro, ou uma pasta cujos ficheiros são verificados um a um, numa conta de documentos. Os ficheiros são renomeados no local onde estão, pelo que não existe localização de saída.

## Como funciona

O passo identifica o tipo de cada ficheiro a partir do seu conteúdo e só muda o nome do ficheiro quando ao nome atual falta uma extensão, tem uma extensão provisória (`.dat`, `.tmp` ou `.bin`) ou indica um tipo diferente que o passo reconhece.

Os tipos que reconhece são PDF; imagens JPEG, PNG, GIF, TIFF, BMP, WebP e HEIC; documentos Excel (`.xlsx`, `.xls`), Word (`.docx`, `.doc`) e PowerPoint (`.pptx`); arquivos ZIP e GZip; e CSV, JSON, HTML, XML e texto simples.

Um ficheiro mantém o nome quando:

- a sua extensão já é adequada ao conteúdo — `.jpg` e `.jpeg` servem ambas para um JPEG, `.tif` e `.tiff` para um TIFF;
- a sua extensão é uma que o passo não reconhece, como `.sql`, `.log` ou `.ai`, porque o conteúdo por si só não distingue um script SQL de qualquer outro texto, nem um ficheiro Illustrator de um PDF;
- contém texto simples sob uma extensão de texto como `.csv`, `.tsv` ou `.json`;
- contém um formato de texto sob a extensão de outro — XML num ficheiro `.html`, CSV num ficheiro `.json` — porque o conteúdo não permite distingui-los de forma fiável. Só um ficheiro `.txt`, ou um sem extensão ou com extensão provisória, é renomeado para um formato de texto;
- é um ficheiro ZIP com nome de documento do Office, uma vez que os ficheiros `.xlsx`, `.docx` e `.pptx` são, por dentro, ficheiros ZIP;
- não é possível determinar o seu tipo, como num ficheiro vazio.

Um arquivo é avaliado pelo seu próprio conteúdo: os seus membros não são abertos nem renomeados. Os ficheiros cujo nome começa por `.` são ignorados.

## Exemplos

| Ficheiro | Conteúdo | Resultado |
|---|---|---|
| `invoice.dat` | PDF | renomeado para `invoice.pdf` |
| `photo.png` | JPEG | renomeado para `photo.jpg` |
| `export.txt` | CSV | renomeado para `export.csv` |
| `readme` | texto simples | renomeado para `readme.txt` |
| `query.sql` | texto simples | inalterado |
| `budget.xlsx` | ZIP | inalterado |

## Notas

- Se o caminho de entrada não existir ou não tiver ficheiros, o passo termina com um aviso que indica o caminho e não processa nada, e o fluxo de trabalho continua.

## Relacionado

- [Concatenar ficheiros](/pt-pt/reference/workflow-steps/document/concatenate-files/)
- [Guia de documentos](/pt-pt/guides/documents/)
