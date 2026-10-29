---
title: Fix File Extension
description: Corrija extensões de arquivo em uma etapa de fluxo de trabalho do PlaidCloud detectando o tipo real do arquivo e renomeando-o com a extensão adequada.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

Lê o que um arquivo realmente contém e, quando isso contradiz a extensão, renomeia o arquivo com a extensão que seu tipo normalmente tem: um PDF salvo como `.dat` passa a ser `.pdf`. É útil quando um sistema de origem entrega arquivos com extensões erradas ou ausentes.

## Entradas

- **Arquivo ou diretório de entrada** — um arquivo, ou uma pasta cujos arquivos são verificados um a um, em uma conta de documentos. Os arquivos são renomeados onde estão, portanto não há local de saída.

## Como funciona

A etapa identifica o tipo de cada arquivo pelo conteúdo e só renomeia o arquivo quando o nome atual não tem extensão, tem uma extensão provisória (`.dat`, `.tmp` ou `.bin`) ou indica outro tipo que a etapa reconhece.

Os tipos reconhecidos são PDF; imagens JPEG, PNG, GIF, TIFF, BMP, WebP e HEIC; documentos do Excel (`.xlsx`, `.xls`), Word (`.docx`, `.doc`) e PowerPoint (`.pptx`); arquivos compactados ZIP e GZip; e CSV, JSON, HTML, XML e texto simples.

Um arquivo mantém o nome quando:

- a extensão já é compatível com o conteúdo: `.jpg` e `.jpeg` servem para um JPEG, `.tif` e `.tiff` para um TIFF;
- a extensão não é reconhecida pela etapa, como `.sql`, `.log` ou `.ai`, porque só o conteúdo não distingue um script SQL de qualquer outro texto, nem um arquivo do Illustrator de um PDF;
- contém texto simples sob uma extensão de texto, como `.csv`, `.tsv` ou `.json`;
- contém um formato de texto sob a extensão de outro, como XML em um arquivo `.html` ou CSV em um arquivo `.json`, porque o conteúdo não permite distingui-los com segurança. Somente um arquivo `.txt`, ou um sem extensão ou com extensão provisória, é renomeado para um formato de texto;
- é um arquivo ZIP com nome de documento do Office, já que os arquivos `.xlsx`, `.docx` e `.pptx` são arquivos ZIP por dentro;
- não é possível determinar seu tipo, como no caso de um arquivo vazio.

Um arquivo compactado é avaliado pelo próprio conteúdo: seus membros não são abertos nem renomeados. Arquivos cujos nomes começam com `.` são ignorados.

## Exemplos

| Arquivo | Conteúdo | Resultado |
|---|---|---|
| `invoice.dat` | PDF | renomeado para `invoice.pdf` |
| `photo.png` | JPEG | renomeado para `photo.jpg` |
| `export.txt` | CSV | renomeado para `export.csv` |
| `readme` | texto simples | renomeado para `readme.txt` |
| `query.sql` | texto simples | inalterado |
| `budget.xlsx` | ZIP | inalterado |

## Observações

- Se o caminho de entrada não existir ou não tiver arquivos, a etapa termina com um aviso que informa o caminho e não processa nada, e o fluxo de trabalho continua.

## Relacionados

- [Concatenate files](/pt-br/reference/workflow-steps/document/concatenate-files/)
- [Guia de documentos](/pt-br/guides/documents/)
