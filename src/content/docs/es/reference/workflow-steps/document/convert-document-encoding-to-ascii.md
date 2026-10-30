---
title: Convert Document Encoding to ASCII
description: Convierte la codificación de un archivo de documento a ASCII en un paso de flujo de trabajo de PlaidCloud para garantizar la compatibilidad con sistemas que requieren texto ASCII.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-ascii.md
---

## Descripción

Reescribe un archivo de texto como ASCII simple. Resulta especialmente útil si el origen de la información tiene codificaciones mixtas o si otras herramientas no admiten determinadas codificaciones.

## Cómo funciona

- Se detecta la codificación del origen. Un archivo UTF-8 se lee como UTF-8, y los caracteres de Windows pegados en él (por ejemplo, las comillas tipográficas de Word o Excel) se conservan intactos, sean cuantos sean. Un archivo en otra codificación se lee con la codificación detectada a partir de su primera parte que no es UTF-8 válido.
- Las letras acentuadas conservan su letra base (`café` pasa a ser `cafe`), y los caracteres sin forma ASCII se descartan.
- Una línea que contiene solo unas comillas dobles se une al final de la línea anterior.
- Un archivo cuya codificación no se puede detectar hace que el paso falle, indicando el archivo.
- Si la ruta de entrada no existe o no contiene archivos, el paso termina con una advertencia que indica la ruta y no procesa nada, y el flujo de trabajo continúa.

## Ejemplos

Seleccione el archivo de entrada y examine el archivo dentro de esa ubicación. Seleccione la ubicación de salida que desee y examine para elegir la ubicación del archivo. Guarde y ejecute.
