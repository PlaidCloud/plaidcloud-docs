---
title: Agregar una cuenta de Azure Data Lake Gen2
description: Agregue una cuenta de Azure Data Lake Storage Gen2 a PlaidCloud para importar y exportar archivos de datos mediante el almacenamiento con espacio de nombres jerárquico en Azure.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-data-lake-gen2-account.md
---

## Configuración de Azure Data Lake Gen2

Azure Data Lake Storage Gen2 se construye sobre Azure Blob Storage con un espacio de nombres jerárquico habilitado. Estos pasos deben completarse en el portal de Azure.

1. Inicie sesión en el [portal de Azure](https://portal.azure.com)
2. Vaya a **Storage accounts** y seleccione o cree una cuenta de almacenamiento que tenga habilitado **Hierarchical namespace**
3. En la barra lateral izquierda, en **Security + networking**, seleccione **Access keys**
4. Copie el **Storage account name** y uno de los valores de **Key**. Guarde ambos para la configuración de PlaidCloud Document que aparece más abajo.
5. Vaya a **Containers**, en **Data storage**, y cree un sistema de archivos (contenedor) si todavía no existe uno. Anote el nombre del sistema de archivos.

Ahora debería tener todo lo necesario para agregar su cuenta de Azure Data Lake Gen2 a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `Azure Data Lake Gen2` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba el nombre del sistema de archivos y el prefijo de ruta opcional en el campo **Ruta de inicio** (por ejemplo, `my-filesystem/data`). El primer segmento de la ruta es el nombre del sistema de archivos.
8. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
9. Pegue el **Storage account name** en el campo Nombre de la cuenta, en Credenciales de autenticación
10. Pegue la **Key** en el campo Clave de la cuenta, en Credenciales de autenticación
11. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
