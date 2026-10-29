---
title: Document - Remote Delete File
description: Elimine archivos en sistemas remotos mediante un agente de PlaidLink en los flujos de trabajo de PlaidCloud para administrar archivos de forma segura detrás de cortafuegos.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-delete-file.md
---

## Descripción



Elimina un archivo en un sistema de archivos que se encuentra detrás de un cortafuegos, al que se accede mediante un agente de PlaidLink. El agente realiza la eliminación localmente en el sistema de archivos local.

Úselo para la limpieza después de operaciones de exportación locales, o como parte de integraciones basadas en archivos que necesitan eliminar los archivos de origen ya procesados.


## Ejemplos


Primero, haga una selección en la lista desplegable “Agente que se usará”. A continuación, introduzca la ruta del archivo o de la carpeta en “Ruta del archivo o de la carpeta que se eliminará”. Por último, seleccione “Guardar y ejecutar el paso”.

## Ruta inexistente

Con un agente de PlaidLink actualizado, una ruta que no existe en el sistema remoto hace que el paso termine con la advertencia `Nothing to delete at <path>` en lugar de un error, y el flujo de trabajo continúa. Los agentes que no se han actualizado siguen haciendo fallar el paso.

Una ruta vacía hace que el paso termine con la advertencia `No path to delete; nothing deleted.` y no elimina nada. Esto incluye una ruta cuya carpeta es una variable que no se resolvió en esta ejecución, como `{folder}/archive`.

Una ruta que es la raíz de un sistema de archivos o una carpeta superior del directorio de trabajo del agente de PlaidLink (`/`, `C:\`, la raíz de un recurso compartido como `\\server\share`, o `..`) hace fallar el paso antes de eliminar nada, con `Refusing to delete the filesystem root <path>.` o `Refusing to delete <path>, which contains the agent's working directory.` Las raíces y `..` se rechazan con los agentes de PlaidLink que ya tiene implementados; un agente actualizado también rechaza cualquier otra carpeta que contenga su directorio de trabajo, según su propio sistema de archivos.
