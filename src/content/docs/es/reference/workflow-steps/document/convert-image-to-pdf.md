---
title: Convert Image to PDF
description: Convierte archivos de imagen en documentos PDF en un paso de flujo de trabajo de PlaidCloud para obtener una salida de documentos estandarizada y formatos listos para archivar.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-image-to-pdf.md
---

Convierte una imagen (PNG, GIF, TIFF, JPEG o HEIC) en un PDF de una página, o reajusta un PDF existente a un tamaño de página estándar.

## Entradas

- **Archivo o directorio de entrada**: una imagen o un PDF, o una carpeta de ellos, en una cuenta de documentos.
- **Destino**: dónde se escribe el PDF.
- **Tamaño de página**: US Letter, US Legal, A3, A4 o A5.
- **Compresión**: **Lossy** reduce las imágenes a resolución de pantalla y puede reducir el archivo de forma drástica; **Lossless**, el valor predeterminado, conserva exactamente los datos de la imagen.

## Cómo funciona

- Una imagen se coloca en una página del tamaño elegido, escalada para caber en ella sin modificar sus proporciones. Una imagen con varias páginas o fotogramas, como un TIFF escaneado, se convierte a partir de la primera.
- Con **Lossy**, el resultado se comprime a continuación, y un PDF de entrada se ajusta al tamaño de página elegido durante la compresión.
- Con **Lossless**, un PDF de entrada pasa sin cambios y conserva su propio tamaño de página.

## Salida

Un PDF por cada archivo de entrada. En el caso de una carpeta, el PDF de cada archivo se escribe en una carpeta con el nombre del destino, sin su extensión, con el nombre propio del archivo de origen. Para combinar varios en un solo documento, haga que este paso vaya seguido del paso [Merge Multiple PDFs](/es/reference/workflow-steps/document/merge-multiple-pdfs/).

## Notas

- Si la ruta de entrada no existe o no contiene archivos, el paso termina con una advertencia que indica la ruta y no procesa nada, y el flujo de trabajo continúa.
- El destino no puede ser la ruta de entrada.

## Usos habituales

- Estandarizar imágenes de recibos o facturas en un formato de archivo
- Preparar imágenes de evidencia para sistemas que solo aceptan PDF como entrada

## Relacionado

- [Paso Convert PDF or Image to JPEG](/es/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Paso Compress PDF](/es/reference/workflow-steps/document/compress-pdf/)
- [Paso Merge Multiple PDFs](/es/reference/workflow-steps/document/merge-multiple-pdfs/)
