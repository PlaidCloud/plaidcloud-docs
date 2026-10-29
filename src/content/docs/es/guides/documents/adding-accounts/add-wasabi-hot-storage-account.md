---
title: Agregar una cuenta de Wasabi Hot Storage
description: Agregue una cuenta de Wasabi Hot Storage a PlaidCloud para importar y exportar archivos de datos mediante almacenamiento en la nube rentable.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Configuración de Wasabi Hot Storage


Estos pasos deben completarse en la consola de Wasabi Hot Storage


1. Inicie sesión en una cuenta de Wasabi Hot Storage o cree una
2. Vaya a `Buckets` en la consola
3. Cree un bucket predeterminado o de prueba
4. Vaya a Users en la consola
5. Seleccione el botón `Create User`
6. Cuando se le solicite, escriba un nombre de usuario y seleccione el usuario `Programmatic (create API key)`
7. Omita la asignación de grupo. Seleccione el botón `Next`
8. Seleccione el ícono de más junto a la política `WasabiFullAccess` para adjuntar la política al usuario. Seleccione el botón `Next`.
9. Revise la configuración del usuario y seleccione `Create User`
10. Guarde las claves generadas para el usuario descargando el CSV o copiándolas y pegándolas en algún lugar para usarlas más adelante. No podrá recuperar esta clave de nuevo, así que téngala a buen resguardo. Si necesita regenerar una clave, simplemente vuelva al paso 5 anterior.

Ahora debería tener todo lo necesario para agregar su cuenta de Wasabi a PlaidCloud Document.



## Configuración de PlaidCloud Document

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `Wasabi Hot Storage` como Tipo de servicio
6. Escriba un nombre y una descripción
7. Escriba el nombre del bucket y un prefijo de ruta opcional en el campo **Ruta de inicio** (por ejemplo, `my-bucket` o `my-bucket/data`). El primer segmento de la ruta es el nombre del bucket.
8. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro.
9. Pegue la **Access Key** creada en el paso 10 anterior en el campo ID de clave de acceso, en Credenciales de autenticación
10. Pegue la **Secret Key** creada en el paso 10 anterior en el campo Clave de acceso secreta, en Credenciales de autenticación
11. Escriba la **Región** si su cuenta de Wasabi usa una región específica; de lo contrario, déjela en blanco
12. Seleccione el botón Guardar y su nueva cuenta de documentos estará activa
