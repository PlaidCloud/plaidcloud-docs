---
title: Export to XML
description: Exporte datos como archivos XML desde un paso de flujo de trabajo de PlaidCloud para el intercambio de datos estructurados y la integración de sistemas.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/export/export-to-xml.md
---

## Descripción

Escribe una tabla de proyecto de PlaidCloud en una cuenta de documentos como un archivo XML. Úselo cuando los sistemas posteriores requieran entrada XML, algo habitual en integraciones empresariales antiguas, presentaciones ante organismos públicos o formatos específicos de intercambio de datos de un sector.

La estructura XML refleja la tabla: un elemento por fila y elementos secundarios para cada columna. Para tener más control sobre la estructura, use un enfoque con plantillas mediante [Document Text Substitution](/es/reference/workflow-steps/document/document-text-substitution/) sobre un archivo de plantilla.

## Si el archivo existe

En **Si el archivo existe**, **Un archivo que ya existe** (`if_exists`) determina qué ocurre cuando el archivo ya existe. **Sobrescribirlo** (`overwrite`, predeterminado) reemplaza un archivo que ya existe; **Hacer fallar el paso sin escribir nada** (`fail`) detiene el paso sin escribir nada cuando ya existe un archivo que se iba a escribir.
