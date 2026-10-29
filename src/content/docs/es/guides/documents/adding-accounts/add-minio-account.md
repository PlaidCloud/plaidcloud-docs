---
title: Agregar una cuenta de MinIO
description: Agregue una cuenta de almacenamiento de MinIO a PlaidCloud para importar y exportar archivos de datos mediante almacenamiento de objetos autoalojado compatible con S3.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## Configuración de MinIO

Estos pasos deben completarse en la consola de MinIO o mediante la CLI `mc`.

1. Inicie sesión en la consola de MinIO (por ejemplo, `https://your-minio-host:9001`)
2. Vaya a **Buckets** y cree un bucket si aún no existe uno. Anote el nombre del bucket.
3. Vaya a **Identity > Users** (o **Access Keys**)
4. Cree un usuario o una cuenta de servicio con acceso de lectura y escritura al bucket de destino
5. Copie la **Access Key** y la **Secret Key** generadas para el usuario. Guarde ambas para la configuración de PlaidCloud Document que se describe más abajo.
6. Anote la URL del punto de conexión de MinIO (por ejemplo, `https://play.min.io` o `https://minio.yourcompany.com`)

Ahora debería tener todo lo necesario para agregar su cuenta de MinIO a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `MinIO` como Tipo de servicio
6. Escriba un nombre y una descripción
7. Escriba la **Ruta de inicio** como la URL del punto de conexión de MinIO seguida del nombre del bucket y un prefijo opcional: `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. Escriba la **Región** si su implementación de MinIO usa regiones; de lo contrario, déjela en blanco
9. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
10. Pegue la **Access Key** en el campo ID de clave de acceso, en Credenciales de autenticación
11. Pegue la **Secret Key** en el campo Clave de acceso secreta, en Credenciales de autenticación
12. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
