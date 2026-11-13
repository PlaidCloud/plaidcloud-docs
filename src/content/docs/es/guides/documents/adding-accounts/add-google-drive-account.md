---
title: Agregar una cuenta de Google Drive
description: Agregue una cuenta de almacenamiento de Google Drive a PlaidCloud para importar y exportar archivos de datos mediante el almacenamiento en la nube de Google Drive.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Configuración de Google Drive

Estos pasos deben completarse en Google Cloud Console para crear una cuenta de servicio que PlaidCloud pueda usar para acceder a Google Drive.

### Crear un proyecto de Google Cloud

1. Inicie sesión en [Google Cloud Console](https://console.cloud.google.com)
2. Cree un proyecto nuevo o seleccione uno existente

### Habilitar la API de Google Drive

1. Vaya a **APIs & Services > Library**
2. Busque **Google Drive API**
3. Selecciónela y haga clic en **Habilitar**

### Crear una cuenta de servicio

1. Vaya a **APIs & Services > Credentials**
2. Seleccione **+ Create Credentials > Service account**
3. Escriba un nombre para la cuenta de servicio (por ejemplo, `plaidcloud-drive`)
4. Seleccione **Create and Continue**
5. Si lo desea, conceda roles (por ejemplo, **Visualizador** para solo lectura o **Editor** para lectura y escritura). Seleccione **Continuar**.
6. Seleccione **Hecho**

### Generar una clave de cuenta de servicio

1. En la lista **Service Accounts**, seleccione la cuenta de servicio que acaba de crear
2. Vaya a la pestaña **Keys**
3. Seleccione **Add Key > Create new key**
4. Elija el formato **JSON** y seleccione **Crear**
5. Se descargará un archivo de clave JSON. Guarde este archivo de forma segura: contiene las credenciales que usará PlaidCloud.

### Compartir el contenido de Drive con la cuenta de servicio

1. Copie la dirección de correo electrónico de la cuenta de servicio (por ejemplo, `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. En Google Drive, comparta con esta dirección de correo electrónico las carpetas a las que desea que PlaidCloud tenga acceso, otorgando acceso de **Editor**. Para usar una unidad compartida, agregue la cuenta de servicio como miembro de ella.

Ahora debería tener todo lo necesario para agregar su cuenta de Google Drive a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage`
4. Seleccione el botón **Nueva cuenta**
5. Seleccione `Google Drive` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba la ruta de la carpeta compartida en el campo **Ruta de inicio**, o déjelo en blanco para acceder a todo el contenido compartido
8. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
9. Pegue todo el contenido del archivo de clave JSON en el campo JSON de credenciales de OAuth2, en Credenciales de autenticación
10. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa

## Uso de la cuenta en flujos de trabajo

Una cuenta de Google Drive funciona en flujos de trabajo además de en el explorador de Document. Los pasos pueden listar, importar, exportar, copiar, mover, cambiar el nombre y eliminar archivos, y crear carpetas.

- **Ubicaciones.** Las ubicaciones de nivel superior de la cuenta son las carpetas compartidas con la cuenta de servicio y las unidades compartidas de las que es miembro. Las rutas son nombres de carpeta, como `Finance/Reports/2026`. Si dos carpetas compartidas o unidades compartidas tienen el mismo nombre, la cuenta se niega a abrir ese nombre. Cambie el nombre de todas menos una, o deje de compartirlas.
- **Google Sheets.** Una hoja de cálculo de Google Sheets se lee como una exportación `.xlsx` y aparece como `Name.xlsx`. Otros archivos de Google Workspace, como Docs y Slides, no se pueden leer.
- **Archivos nuevos en Mi unidad.** Una cuenta de servicio no tiene almacenamiento propio, por lo que en una carpeta que está en la unidad personal Mi unidad de otra persona puede sobrescribir un archivo existente, pero no puede crear uno nuevo. Cree primero el archivo allí, o use una carpeta de una unidad compartida, que acepta archivos y carpetas nuevos.
- **Carpetas inexistentes.** Una carpeta que no existe se lista como vacía en lugar de causar un error.
- **Limitación de solicitudes.** PlaidCloud reintenta automáticamente cuando Google limita una solicitud o devuelve un error temporal.
