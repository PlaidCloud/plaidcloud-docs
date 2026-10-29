---
title: Tokens OAuth
description: Configure tokens OAuth para el acceso a la API de PlaidCloud y autenticar Cuadernos de Jupyter, herramientas de CLI y conexiones de aplicaciones personalizadas.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/oauth-setup.md
---

PlaidCloud usa solicitudes JSON-RPC estándar y se puede utilizar con cualquier aplicación capaz de realizar esas solicitudes.  Las solicitudes están protegidas mediante tokens OAuth.


## Obtención de un token OAuth

Los tokens OAuth se generan desde la aplicación PlaidCloud. Para ver la lista de tokens OAuth que tiene asignados y generar otros nuevos, vaya a `Analyze > Tools > Registered Systems`.

Una vez allí, puede ver los tokens existentes o crear uno nuevo.

## Descarga del archivo de configuración OAuth de PlaidCloud
Seleccione “Register a New System”.

Complete el formulario y anote el nombre que ingresó para poder encontrarlo en la lista.

Una vez creado, abra el registro del sistema registrado haciendo clic en el ícono de engranaje.  Se mostrará el texto del archivo de configuración.  

NOTA: Asegúrese de seleccionar el proyecto para el que desea usar esta conexión en la lista desplegable de la parte superior.  Esto agregará el identificador único del proyecto a la configuración.

Copie este texto en un archivo plaid.conf ubicado en su sistema.  Colóquelo en el directorio .plaid.

## Creación local de un archivo de configuración
Cree un directorio un nivel por encima del directorio de su cuaderno o de donde piense usar la interacción por línea de comandos.  Asigne al directorio el nombre `.plaid`.

Dentro del directorio `.plaid`, cree un archivo llamado `plaid.conf` y pegue en él el contenido que copió anteriormente.  Guarde el archivo y, con ello, podrá conectarse mediante las utilidades de PlaidCloud y los métodos rpc.


## Usos avanzados

Aunque es cómodo ubicar la carpeta `.plaid` cerca del punto de uso, en realidad puede colocarse en cualquier lugar del árbol de directorios superior.  El proceso de inicialización recorrerá el árbol de directorios hacia arriba hasta encontrar el directorio `.plaid`.

Ubicar el directorio `.plaid` en un nivel más alto puede ser útil si tiene varias operaciones que necesitan acceso pero no pueden coexistir en las mismas estructuras de directorios de nivel inferior.


## Especificación opcional de rutas
Si utiliza una instalación local de Jupyter Notebook o trabaja desde la línea de comandos, es posible exportar datos, archivos de Excel y otros datos, así como leer datos locales en dataframes mediante las herramientas auxiliares.  Para ello, es necesario un archivo paths.yaml.

Además del archivo `plaid.conf`, cree un archivo `paths.yaml`.  El archivo `paths.yaml` debe estar al mismo nivel que el archivo `plaid.conf`, dentro del directorio `.plaid`.  Debe contener la siguiente información de rutas:

```yaml
paths:
 PROJECT_ROOT: '{WORKING_USER}/Documents'
 LOCAL_STORAGE: '{PROJECT_ROOT}/local_storage'
 DEBUG: '{PROJECT_ROOT}/local_storage'
 REPORTS: '{PROJECT_ROOT}/reports'
 
 create: []
 local: {}
```
