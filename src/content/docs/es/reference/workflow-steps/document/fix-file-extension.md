---
title: Fix File Extension
description: Corrija las extensiones de archivo en un paso de flujo de trabajo de PlaidCloud detectando el tipo real del archivo y cambiándole el nombre con la extensión adecuada.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/fix-file-extension.md
---

Lee lo que un archivo contiene realmente y, cuando eso contradice su extensión, le cambia el nombre con la extensión que suele llevar su tipo: un PDF guardado como `.dat` pasa a ser `.pdf`. Es útil cuando un sistema de origen entrega archivos con extensiones incorrectas o ausentes.

## Entradas

- **Archivo o directorio de entrada**: un archivo, o una carpeta cuyos archivos se comprueban uno por uno, en una cuenta de documentos. Los archivos cambian de nombre donde están, por lo que no hay ubicación de salida.

## Cómo funciona

El paso identifica el tipo de cada archivo a partir de su contenido y solo le cambia el nombre cuando al nombre actual le falta la extensión, tiene una extensión de marcador de posición (`.dat`, `.tmp` o `.bin`) o indica un tipo distinto que el paso reconoce.

Los tipos que reconoce son PDF; imágenes JPEG, PNG, GIF, TIFF, BMP, WebP y HEIC; documentos de Excel (`.xlsx`, `.xls`), Word (`.docx`, `.doc`) y PowerPoint (`.pptx`); archivos comprimidos ZIP y GZip; y CSV, JSON, HTML, XML y texto sin formato.

Un archivo conserva su nombre cuando:

- su extensión ya se corresponde con su contenido: `.jpg` y `.jpeg` encajan ambas con un JPEG, y `.tif` y `.tiff` con un TIFF;
- su extensión es una que el paso no reconoce, como `.sql`, `.log` o `.ai`, porque el contenido por sí solo no permite distinguir un script SQL de cualquier otro texto, ni un archivo de Illustrator de un PDF;
- contiene texto sin formato con una extensión de texto como `.csv`, `.tsv` o `.json`;
- contiene un formato de texto con la extensión de otro (XML en un archivo `.html`, CSV en un archivo `.json`), porque el contenido no permite distinguirlos de forma fiable. Solo se cambia el nombre a un formato de texto a un archivo `.txt`, o a uno sin extensión o con una extensión de marcador de posición;
- es un archivo ZIP con nombre de documento de Office, ya que los archivos `.xlsx`, `.docx` y `.pptx` son archivos ZIP por dentro;
- no se puede determinar su tipo, como ocurre con un archivo vacío.

Un archivo comprimido se juzga por su propio contenido: sus miembros no se abren ni se renombran. Se omiten los archivos cuyos nombres empiezan por `.`.

## Ejemplos

| Archivo | Contenido | Resultado |
|---|---|---|
| `invoice.dat` | PDF | se renombra a `invoice.pdf` |
| `photo.png` | JPEG | se renombra a `photo.jpg` |
| `export.txt` | CSV | se renombra a `export.csv` |
| `readme` | texto sin formato | se renombra a `readme.txt` |
| `query.sql` | texto sin formato | sin cambios |
| `budget.xlsx` | ZIP | sin cambios |

## Notas

- Si la ruta de entrada no existe o no contiene archivos, el paso termina con una advertencia que indica la ruta y no procesa nada, y el flujo de trabajo continúa.

## Relacionado

- [Concatenate files](/es/reference/workflow-steps/document/concatenate-files/)
- [Guía de documentos](/es/guides/documents/)
