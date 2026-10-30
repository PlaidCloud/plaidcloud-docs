---
title: Concatenate Files
description: Concatena varios archivos en un solo archivo en un paso de flujo de trabajo de PlaidCloud para combinar texto, CSV u otras salidas de documentos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/concatenate-files.md
---

Combina dos o más archivos de una cuenta de documentos en un único archivo de salida. Opera byte a byte, lo que resulta útil para formatos de texto sin formato (CSV, archivos de registro, JSON Lines) en los que una simple concatenación produce una salida válida.

## Entradas

- **Archivos de origen**: lista de archivos que se van a concatenar, en orden
- **Ruta de salida**: destino del archivo combinado
- **Separador**: secuencia de bytes opcional que se inserta entre los archivos de origen (normalmente un salto de línea)

## Salida

Un único archivo con el contenido de todos los archivos de origen en el orden indicado, unidos por el separador configurado.

Un archivo de origen que no existe se omite del archivo combinado, y el paso termina con una advertencia que lo nombra, de modo que el flujo de trabajo continúa.

## Usos habituales

- Combinar archivos de registro diarios en un archivo mensual
- Fusionar archivos CSV que comparten un esquema (elimine los encabezados de todos salvo el primero)
- Unir exportaciones JSON Lines de varios orígenes antes de procesarlas

## No es adecuado para

- PDF: use en su lugar el paso [Merge Multiple PDFs](/es/reference/workflow-steps/document/merge-multiple-pdfs/)
- Formatos binarios con encabezados (XLSX, ZIP, archivos de imagen): concatenar bytes no produce un archivo válido

## Relacionado

- [Paso Merge Multiple PDFs](/es/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Guía de documentos](/es/guides/documents/)
