---
title: Agregar una cuenta de Google Cloud Storage
description: Agregue una cuenta de Google Cloud Storage a PlaidCloud para importar y exportar archivos de datos mediante el almacenamiento de objetos en la nube de Google.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-cloud-storage-account.md
---

## Configuración de Google Cloud


Estos pasos deben completarse en Google Cloud Platform


1. Inicie sesión en una cuenta de Google Cloud Platform o cree una
2. Seleccione o cree un proyecto en el que residirá la cuenta de Google Cloud Storage
3. Vaya a `Cloud Storage > Browser` en la consola de Google Cloud Platform
4. Cree un bucket predeterminado o de prueba
5. Vaya a `IAM & Admin > Service Accounts` en la consola de Google Cloud Platform
6. Seleccione el botón `+ Create Service Account`
7. Complete la información de la cuenta de servicio y cree la cuenta
8. Busque la cuenta de servicio que acaba de crear en la lista de cuentas de servicio y seleccione `Manage Keys` en el menú contextual de la derecha
9. En el menú `Add Key`, seleccione `Create a Key`
10. Cuando se le solicite, seleccione el formato JSON para la clave. Esto generará la clave y la descargará automáticamente en su escritorio. No podrá recuperar esta clave de nuevo, así que téngala bien resguardada. Si necesita regenerar una clave, simplemente vuelva al paso 8 anterior.
11. Vaya a `IAM & Admin > IAM` en la consola de Google Cloud Platform
12. Busque la cuenta de servicio que acaba de crear y haga clic en el icono de edición de permisos
13. Agregue los derechos `Storage Admin` y `Storage Transfer Admin` para la cuenta de servicio y guarde. Tenga en cuenta que se pueden asignar derechos menos permisivos, pero esto afectará a la funcionalidad disponible a través de Document.

Ahora debería tener todo lo necesario para agregar su cuenta de GCS a PlaidCloud Document.



## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `Google Cloud Storage` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba el nombre del bucket y el prefijo de ruta opcional en el campo **Ruta de inicio** (por ejemplo, `my-bucket` o `my-bucket/data`). El primer segmento de la ruta es el nombre del bucket.
8. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
9. Abra el archivo de clave JSON de la cuenta de servicio que descargó en el paso 10 anterior y copie todo su contenido
10. Pegue el contenido en el campo **Clave JSON del usuario del sistema**, en Credenciales de autenticación
11. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa

Se requiere una clave válida de cuenta de servicio. Guardar la cuenta sin ella, o con algo que no sea una clave de cuenta de servicio de Google, se rechaza con el mensaje “GCS document accounts require a valid service-account key.” Una cuenta existente guardada sin una clave válida deja de funcionar hasta que pegue una en el campo **Clave JSON del usuario del sistema**.
