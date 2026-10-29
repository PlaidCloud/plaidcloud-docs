---
title: Document Text Substitution
description: Realice sustituciones de buscar y reemplazar texto en documentos dentro de un paso de flujo de trabajo de PlaidCloud para transformar contenido de forma automática.
sidebar:
  order: 15
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-text-substitution.md
---

## Descripción

Buscar y reemplazar dentro de un archivo de texto. Reemplace cadenas concretas o marcadores de posición por nuevos valores; es útil para crear plantillas (reemplazar un marcador como `CUSTOMER_NAME` por un nombre real) o para depurar texto (eliminar u ocultar cadenas específicas).

Funciona con archivos de texto UTF-8 (TXT, CSV, JSON, XML, HTML, RML) de cualquier tamaño. Un archivo que no sea texto UTF-8, como un PDF o un documento de Office, hace que el paso falle.

## Entradas

- **Archivo o directorio de entrada**: el archivo, o una carpeta de archivos, que se va a modificar.
- **Archivo o directorio de destino**: donde se escribe el resultado. El resultado siempre se escribe en la cuenta de documentos de la entrada; el destino establece la ruta.
- **Compresión**: Sin compresión, Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO o Deflate (zlib) para la salida. Snappy y LZ4 se escriben en el formato de bloques que leen Spark y Hadoop, y LZO como un archivo `lzop`.
- **Orden de las operaciones de reemplazo de texto**: una fila por reemplazo, cada una con el texto original y su reemplazo. En el reemplazo se pueden usar variables.

## Cómo funciona

- Los reemplazos se ejecutan de arriba abajo y cada uno actúa sobre el resultado de los anteriores, de modo que un reemplazo puede cambiar texto que introdujo una fila anterior.
- La coincidencia es exacta y distingue mayúsculas de minúsculas, y se reemplaza cada aparición.
- Se ignora una fila cuyo texto original está vacío.
- En el caso de una carpeta, cada archivo se escribe en una carpeta con el nombre del destino, sin su extensión, con el nombre propio del archivo.
- Si la ruta de entrada no existe o no contiene archivos, el paso termina con una advertencia que indica la ruta y no procesa nada, y el flujo de trabajo continúa.

## Ejemplos

| Original | Reemplazo | `Dear CUSTOMER_NAME,` se convierte en |
|---|---|---|
| `CUSTOMER_NAME` | `Acme Ltd` | `Dear Acme Ltd,` |
