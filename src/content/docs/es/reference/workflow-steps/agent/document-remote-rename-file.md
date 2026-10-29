---
title: Document - Remote Rename File
description: Cambie el nombre de archivos en sistemas remotos mediante un agente de PlaidLink en los flujos de trabajo de PlaidCloud para administrar archivos de forma segura detrás de cortafuegos.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-rename-file.md
---

## Descripción



Cambia el nombre de un archivo, o lo mueve, en un sistema de archivos remoto mediante un agente de PlaidLink. Opera por completo en el lado local; no se transfieren datos hacia PlaidCloud ni desde él.

Patrón habitual: cambiar el nombre de un archivo de origen para marcarlo como “procesado” después de que un paso de importación remota se complete correctamente, de modo que el mismo flujo de trabajo no vuelva a importarlo en la siguiente ejecución.


## Ejemplos


Primero, haga una selección en la lista desplegable “Agente que se usará”. 



A continuación, introduzca “Ruta de origen” y “Ruta de destino”. 



Por último, seleccione “Guardar y ejecutar el paso”.

## Origen inexistente

Con un agente de PlaidLink actualizado, un origen que no existe en el sistema remoto hace que el paso termine con la advertencia `No file or folder found at <path>; nothing renamed` en lugar de un error, y el flujo de trabajo continúa. Los agentes que no se han actualizado siguen haciendo fallar el paso.

Una ruta de origen vacía hace que el paso termine con la advertencia `No path to rename from; nothing renamed.`, incluso cuando una carpeta de la ruta es una variable que no se resolvió en esta ejecución.

Un origen que es la raíz de un sistema de archivos o una carpeta superior del directorio de trabajo del agente de PlaidLink (`/`, `C:\`, la raíz de un recurso compartido como `\\server\share`, o `..`) hace fallar el paso con `Refusing to rename from the filesystem root <path>.` o `Refusing to rename from <path>, which contains the agent's working directory.` Una ruta de destino vacía hace fallar el paso con `No destination path for the rename; it would write into the agent's working directory.` El cambio de nombre hacia la raíz de una unidad o de un recurso compartido, como `E:\` o `\\nas\drop`, funciona. Las raíces y `..` se rechazan con los agentes de PlaidLink que ya tiene implementados; un agente actualizado también rechaza cualquier otra carpeta que contenga su directorio de trabajo, según su propio sistema de archivos.
