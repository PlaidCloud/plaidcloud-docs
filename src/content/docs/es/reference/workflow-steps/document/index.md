---
title: Pasos de documento
description: Administre documentos en los flujos de trabajo de PlaidCloud con pasos para conversión, copia, cambio de nombre y eliminación de archivos, y operaciones con PDF.
sidebar:
  label: Pasos de documento
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/index.md
---

Pasos de flujo de trabajo para operar con archivos almacenados en cuentas de documentos. Úselos para mover, transformar y convertir documentos junto con sus flujos de trabajo de datos.

## Operaciones con archivos

- [Copy Document File](/es/reference/workflow-steps/document/copy-document-file/) · [Copy Document Directory](/es/reference/workflow-steps/document/copy-document-directory/)
- [Create Document Directory](/es/reference/workflow-steps/document/create-document-directory/)
- [Delete Document File](/es/reference/workflow-steps/document/delete-document-file/) · [Delete Document Directory](/es/reference/workflow-steps/document/delete-document-directory/)
- [Listado de directorio](/es/reference/workflow-steps/document/directory-listing/): escribe una tabla con los archivos de una carpeta
- [Update Excel Cells](/es/reference/workflow-steps/document/document-excel-update/): escribe valores en celdas elegidas de un libro, o les da formato
- [Fix File Extension](/es/reference/workflow-steps/document/fix-file-extension/)
- [Rename Document File](/es/reference/workflow-steps/document/rename-document-file/) · [Rename Document Directory](/es/reference/workflow-steps/document/rename-document-directory/)

Los pasos de copia y de cambio de nombre tratan un origen ausente como algo normal. Cuando falta el archivo, o la carpeta que se va a copiar o renombrar, o cuando la carpeta está vacía, el paso no hace nada, termina con una advertencia que indica la ruta y el flujo de trabajo continúa. Una ejecución programada sobre una carpeta que ese día no tiene archivos ya no falla.

## Cifrado

- [Encrypt File · Decrypt File](/es/reference/workflow-steps/document/encrypt-decrypt-file/): AES, Blowfish o la contraseña de un libro de Excel

## Operaciones con PDF

- [Compress PDF](/es/reference/workflow-steps/document/compress-pdf/)
- [Convert Image to PDF](/es/reference/workflow-steps/document/convert-image-to-pdf/)
- [Convert PDF or Image to JPEG](/es/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Merge Multiple PDFs](/es/reference/workflow-steps/document/merge-multiple-pdfs/)

## Operaciones con imágenes

- [Crop Image to Headshot](/es/reference/workflow-steps/document/crop-image-to-headshot/)

## Operaciones con texto

- [Concatenate Files](/es/reference/workflow-steps/document/concatenate-files/): une varios archivos en uno
- [Document Text Substitution](/es/reference/workflow-steps/document/document-text-substitution/): buscar y reemplazar dentro de un documento

## Conversión de codificación

- [Convert Document Encoding](/es/reference/workflow-steps/document/convert-document-encoding/): elija la codificación de destino
- [Convert Document Encoding to ASCII](/es/reference/workflow-steps/document/convert-document-encoding-to-ascii/)
- [Convert Document Encoding to UTF-16](/es/reference/workflow-steps/document/convert-document-encoding-to-utf-16/)
- [Convert Document Encoding to UTF-8](/es/reference/workflow-steps/document/convert-document-encoding-to-utf-8/)

## Véase también

- [Convert Dashboard to PDF](/es/reference/workflow-steps/document/dashboard-to-pdf/)
- [Delete Old Files](/es/reference/workflow-steps/document/document-delete-old-files/)
- [Cuentas de documentos](/es/guides/documents/adding-accounts/): conecte cuentas de documentos antes de usar estos pasos
- [Guía de documentos](/es/guides/documents/): tutoriales orientados a tareas para las mismas operaciones
