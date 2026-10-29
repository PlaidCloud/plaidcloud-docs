---
title: Agregar una cuenta de Linode Object Storage
description: Agregue una cuenta de Linode (Akamai) Object Storage a PlaidCloud para importar y exportar archivos de datos mediante el almacenamiento en la nube compatible con S3 de Linode.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Configuración de Linode Object Storage

Estos pasos deben completarse en Linode Cloud Manager.

1. Inicie sesión en [Linode Cloud Manager](https://cloud.linode.com)
2. Vaya a **Object Storage** en la barra lateral izquierda
3. Cree un bucket si todavía no existe uno. Anote el nombre del bucket (llamado **label**) y la región (por ejemplo, `us-east-1`).
4. Vaya a **Object Storage > Access Keys**
5. Seleccione **Create Access Key**
6. Asigne una etiqueta a la clave y seleccione los buckets a los que debe tener acceso con permisos de lectura y escritura
7. Seleccione **Create Access Key**
8. Copie la **Access Key** y la **Secret Key**. Guarde ambas para la configuración de PlaidCloud Document que aparece más abajo. El secreto solo se muestra una vez.
9. Anote la URL del punto de conexión de la región de su bucket. Sigue el patrón `https://{region}.linodeobjects.com` (por ejemplo, `https://us-east-1.linodeobjects.com`)

Ahora debería tener todo lo necesario para agregar su cuenta de Linode Object Storage a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `Linode Object Storage` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba la **Ruta de inicio** como la URL del punto de conexión seguida del nombre del bucket: `https://us-east-1.linodeobjects.com/my-bucket`
8. Escriba la **Región** (por ejemplo, `us-east-1`)
9. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
10. Pegue la **Access Key** en el campo ID de clave de acceso, en Credenciales de autenticación
11. Pegue la **Secret Key** en el campo Clave de acceso secreta, en Credenciales de autenticación
12. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
