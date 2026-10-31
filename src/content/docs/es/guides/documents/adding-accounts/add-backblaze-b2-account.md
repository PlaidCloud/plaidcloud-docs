---
title: Agregar una cuenta de Backblaze B2
description: Agregue una cuenta de almacenamiento de Backblaze B2 a PlaidCloud para importar y exportar archivos de datos mediante almacenamiento de objetos en la nube a bajo costo.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Configuración de Backblaze B2

Estos pasos deben completarse en la consola de Backblaze B2.

1. Inicie sesión en la [consola de Backblaze B2](https://secure.backblaze.com/b2_buckets.htm)
2. Vaya a **Buckets** y cree un bucket si todavía no existe uno. Anote el nombre del bucket.
3. Vaya a **App Keys**
4. Seleccione **Add a New Application Key**
5. Asigne un nombre a la clave, seleccione el bucket al que debe tener acceso y elija los permisos adecuados (lectura y escritura)
6. Seleccione **Create New Key**
7. Copie el **keyID** (es su Access Key) y la **applicationKey** (es su Secret Key). Guarde ambos para la configuración de PlaidCloud Document que aparece más abajo. La clave de aplicación solo se muestra una vez.
8. Anote el **S3 Endpoint** de la región de su bucket. Sigue el patrón `https://s3.{region}.backblazeb2.com` (por ejemplo, `https://s3.us-west-004.backblazeb2.com`). Puede encontrarlo en la página de detalles del bucket.

Ahora debería tener todo lo necesario para agregar su cuenta de Backblaze B2 a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `Backblaze B2` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba la **Ruta de inicio** como su punto de conexión compatible con S3 seguido del nombre del bucket: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Escriba la **Región** de su bucket (por ejemplo, `us-west-004`)
9. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
10. Pegue el **keyID** en el campo ID de clave de acceso, en Credenciales de autenticación
11. Pegue la **applicationKey** en el campo Clave de acceso secreta, en Credenciales de autenticación
12. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
