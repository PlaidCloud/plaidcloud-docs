---
title: Convert Document Encoding
description: Convierte la codificación de un archivo de documento entre juegos de caracteres en un paso de flujo de trabajo de PlaidCloud para resolver problemas de compatibilidad de codificación.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## Descripción



Recodifica un archivo de texto de una codificación de caracteres a otra. Resulta útil cuando los archivos de origen llegan en codificaciones heredadas (Windows-1252, ISO-8859-1) pero las herramientas posteriores necesitan UTF-8, o viceversa.

Cuando el archivo de origen no es UTF-8, su codificación se deduce del contenido del archivo. Un archivo muy corto o muy repetitivo ofrece muy poca información y puede leerse de forma errónea, así que revise la salida convertida de un archivo así.

Un carácter que la codificación de destino no puede contener hace que el paso falle de forma predeterminada. Seleccione **Reemplazar por ? los caracteres que la codificación de destino no admite** para escribir en su lugar un `?`, como hace un escritor de Java, y el paso termina.

Un archivo comprimido se expande primero, y cada archivo que contiene se convierte. En el caso de una carpeta, cada archivo se escribe en el destino con su propio nombre. Marque **Conservar subcarpetas** para escribir en su lugar un archivo de una subcarpeta en la subcarpeta equivalente del destino; el contenido de un archivo comprimido va entonces a la subcarpeta en la que estaba el archivo comprimido. Si dos archivos se escribieran en el mismo lugar, el paso falla antes de escribir el segundo, en lugar de dejar que reemplace al primero, e indica si marcar **Conservar subcarpetas** los mantendría separados.

Elija la codificación de destino en la configuración del paso. Para acceder a atajos de codificaciones específicas, consulte las variantes [UTF-8](/es/reference/workflow-steps/document/convert-document-encoding-to-utf-8/), [UTF-16](/es/reference/workflow-steps/document/convert-document-encoding-to-utf-16/) y [ASCII](/es/reference/workflow-steps/document/convert-document-encoding-to-ascii/).


## Ejemplos


Cree una entrada de origen, seleccione el archivo de entrada y examine el archivo dentro de esa ubicación. Seleccione la ubicación de salida que desee y examine para seleccionar la ubicación que desee para el archivo. Guarde y ejecute.
