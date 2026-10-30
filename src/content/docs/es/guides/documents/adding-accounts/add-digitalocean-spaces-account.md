---
title: Agregar una cuenta de DigitalOcean Spaces
description: Agregue una cuenta de almacenamiento de DigitalOcean Spaces a PlaidCloud para importar y exportar archivos de datos mediante el almacenamiento de objetos compatible con S3 de DigitalOcean.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-digitalocean-spaces-account.md
---

## Configuración de Digitalocean Spaces

Estos pasos deben completarse en el panel de control de DigitalOcean.

1. Inicie sesión en el [panel de control de DigitalOcean](https://cloud.digitalocean.com)
2. Vaya a **Spaces Object Storage** en la barra lateral izquierda
3. Cree un Space si todavía no existe uno. Anote el nombre del Space y la región (por ejemplo, `nyc3`).
4. Vaya a **API > Spaces Keys** (en la sección Tokens)
5. Seleccione **Generate New Key**
6. Asigne un nombre a la clave
7. Copie la **Key** (Access Key) y el **Secret**. Guarde ambos para la configuración de PlaidCloud Document que aparece más abajo. El secreto solo se muestra una vez.
8. Anote la URL del punto de conexión de la región de su Space. Sigue el patrón `https://{region}.digitaloceanspaces.com` (por ejemplo, `https://nyc3.digitaloceanspaces.com`)

Ahora debería tener todo lo necesario para agregar su cuenta de DigitalOcean Spaces a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `DigitalOcean Spaces` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba la **Ruta de inicio** como la URL del punto de conexión seguida del nombre del Space: `https://nyc3.digitaloceanspaces.com/my-space`
8. Escriba la **Región** (por ejemplo, `nyc3`, `sfo3`, `ams3`)
9. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
10. Pegue la **Key** en el campo ID de clave de acceso, en Credenciales de autenticación
11. Pegue el **Secret** en el campo Clave de acceso secreta, en Credenciales de autenticación
12. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
