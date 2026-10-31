---
title: Merge Multiple PDFs
description: Combine varios archivos PDF en un único documento en un paso de flujo de trabajo de PlaidCloud para ensamblar y consolidar informes.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/merge-multiple-pdfs.md
---

Une los PDF de una carpeta en un único PDF. A diferencia de [Concatenate Files](/es/reference/workflow-steps/document/concatenate-files/), este paso entiende el formato PDF y genera un documento combinado válido.

## Entradas

- **Directorio de entrada**: la carpeta cuyos PDF se combinan, en una cuenta de documentos. En su lugar se puede indicar un único archivo comprimido, como un ZIP de PDF, y se combinan los PDF que contiene.
- **Archivo combinado de salida**: donde se escribe el PDF combinado.

## Cómo funciona

- Los PDF se combinan según el orden de su ruta, y los números se toman por su valor (`page2.pdf` va antes que `page10.pdf`), así que numérelos para controlar el orden. Cada uno conserva sus propias páginas en orden.
- Solo se combinan los archivos con nombre `.pdf`. Todo lo demás de la carpeta se deja fuera, y un archivo comprimido de la carpeta no se abre.
- Los archivos de las subcarpetas se incluyen cuando la cuenta de documentos los lista: las cuentas de S3, Wasabi y Google Cloud Storage listan todo el árbol de carpetas, mientras que las de OneDrive, SFTP y Azure listan solo el nivel superior.
- Se combinan como máximo 100 PDF; si hay más, el paso falla.

## Salida

Un único PDF en la ruta de salida, con todas las páginas de todos los PDF combinados.

## Notas

- Una carpeta sin PDF, o que no existe, hace que el paso termine con una advertencia que indica la carpeta y no combine nada, y el flujo de trabajo continúa.
- La ruta de salida no puede ser la ruta de entrada.

## Usos habituales

- Ensamblar informes mensuales a partir de PDF de informes individuales
- Combinar una portada, el cuerpo y los apéndices en un único entregable
- Agrupar facturas generadas en un archivo por cliente o por período

## Relacionado

- [Compress PDF](/es/reference/workflow-steps/document/compress-pdf/): reduzca el tamaño del resultado combinado
- [Convert Image to PDF](/es/reference/workflow-steps/document/convert-image-to-pdf/): convierta imágenes en PDF antes de combinar
