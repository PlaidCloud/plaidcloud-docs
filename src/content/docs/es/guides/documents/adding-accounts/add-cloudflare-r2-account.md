---
title: Agregar una cuenta de Cloudflare R2
description: Agregue una cuenta de almacenamiento de Cloudflare R2 a PlaidCloud para importar y exportar archivos de datos mediante el almacenamiento de objetos de Cloudflare sin tarifas de salida de datos.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Configuración de Cloudflare R2

Estos pasos deben completarse en el panel de Cloudflare.

1. Inicie sesión en el [panel de Cloudflare](https://dash.cloudflare.com)
2. Seleccione su cuenta y luego vaya a **R2 Object Storage** en la barra lateral izquierda
3. Cree un bucket si todavía no existe uno. Anote el nombre del bucket.
4. Vaya a **R2 Object Storage > Manage R2 API Tokens**
5. Seleccione **Create API Token**
6. Asigne un nombre al token, seleccione los buckets a los que debe tener acceso y elija los permisos **Object Read & Write**
7. Seleccione **Create API Token**
8. Copie el **Access Key ID** y la **Secret Access Key**. Guarde ambos para la configuración de PlaidCloud Document que aparece más abajo. El secreto solo se muestra una vez.
9. Anote el **S3 API endpoint** de su cuenta. Sigue el patrón `https://{account_id}.r2.cloudflarestorage.com` y se muestra en la página de descripción general de R2.

Ahora debería tener todo lo necesario para agregar su cuenta de Cloudflare R2 a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `Cloudflare R2` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba la **Ruta de inicio** como su punto de conexión de R2 seguido del nombre del bucket: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. El campo **Región** se puede establecer en `auto` o dejarse en blanco: R2 selecciona automáticamente la región más cercana
9. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
10. Pegue el **Access Key ID** en el campo ID de clave de acceso, en Credenciales de autenticación
11. Pegue la **Secret Access Key** en el campo Clave de acceso secreta, en Credenciales de autenticación
12. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
