---
title: Crop Image to Headshot
description: Recorta imágenes a un retrato cuadrado en un paso de flujo de trabajo de PlaidCloud para estandarizar los retratos de directorios e identificaciones.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/crop-image-to-headshot.md
---

Recorta una imagen a un cuadrado centrado y la escala a un JPEG de 500 × 500 píxeles. Resulta útil para normalizar directorios de empleados o miembros en los que las fotos de origen varían en relación de aspecto.

## Entradas

- **Archivo o directorio de entrada**: una imagen, o una carpeta de imágenes, en una cuenta de documentos.
- **Archivo o directorio de salida**: dónde se escribe el retrato.

## Salida

Un JPEG de 500 × 500 recortado desde el centro del origen. En el caso de una carpeta, el retrato de cada archivo se escribe en una carpeta con el nombre de la ruta de salida, sin su extensión.

## Notas

- El recorte se toma desde el centro de la imagen; no busca un rostro, así que encuadre las fotos de origen con el sujeto centrado.
- Un archivo que no se puede leer como imagen se copia a la salida sin cambios en lugar de hacer que el paso falle.
- Si la ruta de entrada no existe o no contiene archivos, el paso termina con una advertencia que indica la ruta y no procesa nada, y el flujo de trabajo continúa.
- La ruta de salida no puede ser la ruta de entrada.

## Usos habituales

- Estandarizar las fotos de un directorio de empleados
- Generar imágenes de avatar coherentes para un portal interno
- Recortar fotos para identificaciones y credenciales

## Relacionado

- [Paso Convert PDF or Image to JPEG](/es/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Paso Fix File Extension](/es/reference/workflow-steps/document/fix-file-extension/)
