---
title: Compress PDF
description: Comprime archivos PDF en un paso de flujo de trabajo de PlaidCloud para reducir el tamaño del archivo manteniendo la calidad del documento y ahorrando espacio de almacenamiento.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/compress-pdf.md
---

Reduce el tamaño de un PDF almacenado en una cuenta de documentos. Resulta útil para recortar documentos escaneados de gran tamaño antes de archivarlos, adjuntarlos a notificaciones o moverlos entre cuentas de documentos.

## Entradas

- **Archivo o directorio de entrada**: un PDF, o una carpeta de PDF, en una cuenta de documentos.
- **Archivo o directorio de salida**: dónde se escribe el PDF comprimido.

## Cómo funciona

El PDF se reescribe con sus imágenes reducidas a resolución de pantalla (72 ppp) y con sus fuentes incrustadas como subconjuntos, lo que puede reducir drásticamente los documentos escaneados; el texto se mantiene nítido. Las páginas se ajustan al tamaño US Letter.

## Salida

Un PDF comprimido en la ruta de salida. En el caso de una carpeta, cada PDF se escribe bajo la ruta de salida, conservando su posición relativa a la carpeta de entrada.

## Notas

- La ruta de salida no puede ser la ruta de entrada, de modo que el origen nunca se sobrescribe.
- Si la ruta de entrada no existe o no contiene archivos, el paso termina con una advertencia que indica la ruta y no procesa nada, y el flujo de trabajo continúa.
- Un PDF que no se puede comprimir hace que el paso falle, indicando el archivo y el motivo.

## Usos habituales

- Reducir facturas, recibos o contratos escaneados antes de almacenarlos a largo plazo
- Reducir el tamaño de un PDF antes de enviarlo por correo electrónico o adjuntarlo a notificaciones
- Preparar documentos para cargarlos en sistemas posteriores con límites de tamaño

## Relacionado

- [Paso Convert PDF or Image to JPEG](/es/reference/workflow-steps/document/convert-pdf-or-image-to-jpeg/)
- [Paso Merge Multiple PDFs](/es/reference/workflow-steps/document/merge-multiple-pdfs/)
- [Guía de documentos](/es/guides/documents/)
