---
title: Agregar una cuenta de Azure Blob Storage
description: Agregue una cuenta de Azure Blob Storage a PlaidCloud para importar y exportar archivos de datos mediante el almacenamiento de objetos en la nube de Microsoft Azure.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-blob-storage-account.md
---

## Configuración de Azure Blob Storage

Estos pasos deben completarse en el portal de Azure.

1. Inicie sesión en el [portal de Azure](https://portal.azure.com)
2. Vaya a **Storage accounts** y seleccione o cree una cuenta de almacenamiento
3. En la barra lateral izquierda, en **Security + networking**, seleccione **Access keys**
4. Copie el **Storage account name** y uno de los valores de **Key**. Guarde ambos para la configuración de PlaidCloud Document que aparece más abajo.
5. Vaya a **Containers**, en **Data storage**, y cree un contenedor si todavía no existe uno. Anote el nombre del contenedor.

Ahora debería tener todo lo necesario para agregar su cuenta de Azure Blob Storage a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `Azure Blob Storage` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba el nombre del contenedor y el prefijo de ruta opcional en el campo **Ruta de inicio** (por ejemplo, `my-container/data`). El primer segmento de la ruta es el nombre del contenedor.
8. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
9. Pegue el **Storage account name** en el campo Nombre de la cuenta, en Credenciales de autenticación
10. Pegue la **Key** en el campo Clave de la cuenta, en Credenciales de autenticación
11. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
