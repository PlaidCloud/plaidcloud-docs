---
title: Document - Remote Export File
description: Exporte archivos a sistemas remotos mediante un agente de PlaidLink en los flujos de trabajo de PlaidCloud para transferir archivos de forma segura detrás de cortafuegos.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/document-remote-export-file.md
---

## Descripción



Escribe un archivo de una cuenta de documentos de PlaidCloud en un sistema de archivos remoto mediante un agente de PlaidLink. Es útil para entregar informes, extracciones o archivos procesados a sistemas a los que PlaidCloud no puede acceder directamente, como unidades compartidas internas, servidores SFTP locales o directorios de aplicaciones especializadas.

El agente recibe el archivo de PlaidCloud y lo escribe en el destino local configurado.


## Ejemplos


Primero, haga una selección en la lista desplegable “Agente que se usará”. A continuación, busque la ruta del archivo o de la carpeta en “Archivo o carpeta que se exportará”. Después, introduzca la ubicación en “Destino de la ruta de exportación”. Por último, seleccione “Guardar y ejecutar el paso”.

## Seguridad de la ruta

Una ruta de exportación vacía hace fallar el paso con `No destination path for the export; it would write into the agent's working directory.` Esto incluye una ruta que no se resolvió porque una variable de ella estaba vacía. La exportación a la raíz de una unidad o de un recurso compartido, como `E:\` o `\\nas\drop`, funciona.

Con **Descomprimir el archivo comprimido al llegar** seleccionado, el paso descomprime todos los archivos comprimidos de la carpeta de destino y los elimina. Por ello rechaza un destino que sea la raíz de un sistema de archivos o un archivo situado directamente en ella (`Refusing to unpack an export into the filesystem root <path>.`), o la propia carpeta del agente de PlaidLink (`Refusing to unpack an export into <path>, which contains the agent's working directory.`). Elija en su lugar una subcarpeta dedicada.

Las comprobaciones de ruta vacía y de raíz funcionan con los agentes de PlaidLink que ya tiene implementados. Para rechazar la propia carpeta del agente se necesita un agente de PlaidLink actualizado.
