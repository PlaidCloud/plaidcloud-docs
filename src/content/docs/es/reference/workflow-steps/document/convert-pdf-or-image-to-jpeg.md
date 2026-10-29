---
title: Convert PDF or Image to JPEG
description: Convierte páginas de PDF o imágenes al formato JPEG en un paso de flujo de trabajo de PlaidCloud para obtener una salida compatible con la web y realizar tareas de procesamiento de imágenes.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg.md
---

Convierte un PDF o una imagen en un JPEG. La primera página de un PDF se convierte en el JPEG; una imagen se recodifica, y una con varias páginas o fotogramas, como un TIFF escaneado, se convierte a partir de la primera.

## Entradas

- **Archivo o directorio de entrada**: un PDF o una imagen (PNG, GIF, TIFF, JPEG o HEIC), o una carpeta de ellos, en una cuenta de documentos.
- **Archivo o directorio de salida**: dónde se escribe el JPEG.

## Salida

Un JPEG por cada archivo de entrada. En el caso de una carpeta, el JPEG de cada archivo se escribe en una carpeta con el nombre de la ruta de salida, sin su extensión, con el nombre propio del archivo de origen.

## Notas

- Un archivo de cualquier otro tipo hace que el paso falle, indicando los tipos que acepta.
- Si la ruta de entrada no existe o no contiene archivos, el paso termina con una advertencia que indica la ruta y no procesa nada, y el flujo de trabajo continúa.
- La ruta de salida no puede ser la ruta de entrada.

## Usos habituales

- Generar imágenes de vista previa para mostrar en la web
- Producir versiones de solo imagen de PDF para sistemas que no pueden manejar PDF

## Relacionado

- [Paso Convert Image to PDF](/es/reference/workflow-steps/document/convert-image-to-pdf/)
- [Paso Compress PDF](/es/reference/workflow-steps/document/compress-pdf/)
- [Paso Crop Image to Headshot](/es/reference/workflow-steps/document/crop-image-to-headshot/)
