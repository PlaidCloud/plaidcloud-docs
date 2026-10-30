---
title: Agregar una cuenta de AWS S3
description: Agregue una cuenta de almacenamiento de AWS S3 a PlaidCloud para importar y exportar archivos de datos mediante el almacenamiento de objetos en la nube de Amazon.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## Configuración de AWS S3

Estos pasos deben completarse en la consola de AWS.

1. Inicie sesión en una cuenta de Amazon Web Services (AWS) o cree una
2. Vaya a `All services > Storage > S3` en la consola
3. Cree un bucket predeterminado o de prueba. Anote el nombre del bucket y la región (por ejemplo, `us-east-1`).
4. Vaya a `All Services > Security Identity & Compliance > IAM > Users` en la consola
5. Seleccione el botón `Create User`
6. Cuando se le solicite, escriba un nombre de usuario y seleccione únicamente `Access Key - Programmatic access`. Seleccione el botón `Next: Permissions`.
7. Seleccione la casilla de opción llamada `Attach existing policies directly`
8. En el cuadro de búsqueda del filtro, escriba `s3`. Cuando la lista se reduzca a los elementos relacionados con S3, seleccione `AmazonS3FullAccess` marcando la casilla de la izquierda. Seleccione el botón `Next: Tags`.
9. Omita este paso seleccionando el botón `Next: Review`
10. Revise la configuración del usuario y seleccione `Create user`
11. Capture las claves generadas para el usuario descargando el CSV o copiándolas y pegándolas en algún lugar para usarlas más adelante. No podrá recuperar esta clave de nuevo, así que téngala bien resguardada. Si necesita regenerar una clave, simplemente vuelva al paso 5 anterior.

Ahora debería tener todo lo necesario para agregar su cuenta de S3 a PlaidCloud Document.


## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `Amazon S3` como Tipo de servicio
6. Complete un nombre y una descripción
7. Escriba el nombre del bucket y el prefijo de ruta opcional en el campo **Ruta de inicio** (por ejemplo, `my-bucket` o `my-bucket/data`). El primer segmento de la ruta es el nombre del bucket.
8. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
9. Pegue la **Access Key** creada en el paso 11 anterior en el campo ID de clave de acceso, en Credenciales de autenticación
10. Pegue la **Secret Key** creada en el paso 11 anterior en el campo Clave de acceso secreta, en Credenciales de autenticación
11. Escriba la **Región** de su bucket (por ejemplo, `us-east-1`, `eu-west-1`). Si se deja en blanco, el valor predeterminado es `us-east-2`.
12. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
