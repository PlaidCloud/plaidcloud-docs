---
title: Document - Remote Import File
description: Importe archivos desde sistemas remotos mediante un agente de PlaidLink en los flujos de trabajo de PlaidCloud para recuperar archivos de forma segura detrás de cortafuegos.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-import-file.md
---

## Descripción



Obtiene un archivo de un sistema de archivos remoto mediante un agente de PlaidLink y lo almacena en una cuenta de documentos de PlaidCloud. Se utiliza cuando los archivos de origen proceden de recursos compartidos internos, servidores locales o están detrás de un cortafuegos.

El agente lee el archivo localmente y lo transmite a PlaidCloud, donde los pasos posteriores del flujo de trabajo pueden procesarlo.


## Ejemplos


Primero, haga una selección en la lista desplegable “Agente que se usará”. A continuación, introduzca la ruta del archivo o de la carpeta en “Ruta del archivo o de la carpeta que se importará”. Después, introduzca la carpeta de destino en “Carpeta de destino”. Opcionalmente, elija una **Compresión** para comprimir el archivo a medida que llega: Zip, GZip, BZip2, Zstandard, LZ4, Snappy, LZO o Deflate (zlib). Por último, seleccione “Guardar y ejecutar el paso”.

## Archivo o carpeta de origen inexistente

Cuando no existe nada en la ruta del recurso compartido remoto, el paso termina con la advertencia `No file or folder found at <path>; nothing imported.` en lugar de un error. El flujo de trabajo continúa con el paso siguiente, y la configuración de reintento y de error del paso (ir a un paso o continuar) no se aplica a un origen inexistente. Esto funciona con los agentes de PlaidLink que ya tiene implementados.

Una ruta vacía termina de la misma manera, con la advertencia `No path to import from; nothing imported.`. Esto incluye una ruta cuya carpeta es una variable que no se resolvió en esta ejecución, como `{folder}/archive`.

Una ruta que es la raíz de un sistema de archivos o una carpeta superior del directorio de trabajo del agente de PlaidLink (`/`, `C:\`, la raíz de un recurso compartido como `\\server\share`, o `..`) hace fallar el paso antes de cargar nada, con `Refusing to import from the filesystem root <path>.` o `Refusing to import from <path>, which contains the agent's working directory.` Las raíces y `..` se rechazan con los agentes de PlaidLink que ya tiene implementados; un agente actualizado también rechaza cualquier otra carpeta que contenga su directorio de trabajo, según su propio sistema de archivos.

Otros fallos siguen haciendo fallar el paso: permiso denegado, una carga fallida a PlaidCloud o, en un agente de PlaidLink actualizado, un servidor o recurso compartido al que no se puede acceder.

Como no se importa nada, un documento de una ejecución anterior permanece donde estaba. Para ejecutar un paso posterior solo cuando haya llegado el archivo de este período, puede hacer una de estas dos cosas:

- Agregue al paso posterior una [condición de paso](/es/guides/workflows/step-conditions/#condiciones-de-ruta-de-documento) **file exists in Document**, con la ruta de Document establecida en una ruta por período, como una que incluya el período en el nombre del archivo.
- Elimine el documento importado después de que el flujo de trabajo lo use, para que un origen inexistente no deje un archivo antiguo.
