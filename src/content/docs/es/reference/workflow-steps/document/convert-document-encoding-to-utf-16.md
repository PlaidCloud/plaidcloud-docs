---
title: Convert Document Encoding to UTF-16
description: Convierte la codificación de un archivo de documento a UTF-16 en un paso de flujo de trabajo de PlaidCloud para admitir juegos de caracteres multibyte y texto Unicode.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding-to-utf-16.md
---

## Descripción

Reescribe un archivo de texto en UTF-16. Resulta útil cuando un sistema posterior requiere UTF-16, o cuando un origen mezcla codificaciones que otras herramientas rechazan.

## Entradas

- **Archivo o directorio de entrada**: el archivo de texto o el archivo comprimido, o una carpeta de ellos, que se va a convertir.
- **Destino**: dónde se escribe el archivo convertido.
- **Compresión**: Sin compresión, Zip, GZip o BZip2 para la salida.
- **Conservar subcarpetas**: para una carpeta, márquela para escribir cada archivo de una subcarpeta en la subcarpeta equivalente del destino.
- **Endianness (orden de bytes)**: Little endian o Big endian.
- **Include BOM**: márquela para que el archivo comience con una marca de orden de bytes (`FF FE` para little endian, `FE FF` para big endian). Déjela sin marcar para no incluir ninguna marca.

## Cómo funciona

- Se detecta la codificación del origen. Un archivo UTF-8 se lee como UTF-8, y los caracteres de Windows pegados en él (por ejemplo, las comillas tipográficas de Word o Excel) se conservan intactos, sean cuantos sean. Un archivo en otra codificación se lee con la codificación detectada a partir de su primera parte que no es UTF-8 válido.
- El texto se escribe sin cambios: las letras acentuadas, los símbolos y los demás caracteres se conservan exactamente como estaban.
- Un archivo cuya codificación no se puede detectar hace que el paso falle, indicando el archivo.
- Si la ruta de entrada no existe o no contiene archivos, el paso termina con una advertencia que indica la ruta y no procesa nada, y el flujo de trabajo continúa.
- Un archivo comprimido — por ejemplo, un archivo zip, gzip o bzip2 — se expande primero, y cada archivo que contiene se convierte.
- En el caso de una carpeta, cada archivo se convierte y se escribe en el destino con su propio nombre. Marque **Conservar subcarpetas** para escribir en su lugar un archivo de una subcarpeta en la subcarpeta equivalente del destino; el contenido de un archivo comprimido va entonces a la subcarpeta en la que estaba el archivo comprimido.
- Si dos archivos se escribieran en el mismo lugar del destino, el paso falla antes de escribir el segundo, en lugar de dejar que reemplace al primero. El mensaje nombra ambos archivos, o el archivo comprimido del que proceden los dos, y el lugar; si marcar **Conservar subcarpetas** los escribiría en lugares distintos, lo indica.

## Ejemplos

Seleccione el archivo de entrada y examine el archivo dentro de esa ubicación. Seleccione la ubicación de salida que desee, elija el orden de bytes y marque **Include BOM** si el sistema receptor espera una marca. Guarde y ejecute.
