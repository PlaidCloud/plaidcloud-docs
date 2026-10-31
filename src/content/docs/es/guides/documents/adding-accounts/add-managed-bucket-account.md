---
title: Agregar una cuenta de bucket administrado de PlaidCloud
description: "Agregue almacenamiento de archivos totalmente administrado a PlaidCloud Document en un solo paso: elija un nombre y PlaidCloud lo configura todo por usted, sin nada que configurar."
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

Un **bucket administrado de PlaidCloud** es la forma más rápida de agregar almacenamiento de archivos a Document. PlaidCloud crea y administra el almacenamiento por usted: no hay nada que configurar de antemano ni credenciales que administrar. Solo tiene que darle un nombre.

Use un bucket administrado de PlaidCloud cuando quiera un lugar nuevo e independiente donde guardar los archivos de Document. Para conectar un almacenamiento que ya posee y administra usted mismo, elija en su lugar uno de los otros proveedores de la página [Agregar nuevas cuentas de documentos](/es/guides/documents/adding-accounts/).

## Configuración

1. Inicie sesión en PlaidCloud
2. Seleccione el espacio de trabajo en el que residirá la nueva cuenta de documentos
3. Vaya a `Document > Manage Accounts`
4. Seleccione el botón `+ New Account`
5. Seleccione `PlaidCloud Managed Bucket` como Tipo de servicio
6. Complete un nombre y una descripción opcional
7. Escriba un **Nombre del bucket**. Los nombres deben tener entre 3 y 63 caracteres, usar solo letras minúsculas, dígitos, puntos o guiones, y empezar y terminar con una letra o un dígito. El nombre debe ser **único a nivel global**: si ya está en uso, se le pedirá que elija otro
8. Seleccione un **Modelo de seguridad** adecuado para su caso de uso. Déjelo en `Private` si no está seguro
9. Seleccione el botón Guardar

PlaidCloud configura el almacenamiento y lo designa a usted como propietario. La cuenta está lista de inmediato para examinar y cargar archivos: no hay nada más que configurar.

:::note
Los buckets administrados de PlaidCloud están disponibles en los planes **Business** y **Enterprise**. Si su plan no los incluye, o ha alcanzado el límite de su plan, el formulario se lo indicará cuando intente crear uno.
:::

## Después de la creación

- El nombre del bucket queda fijo una vez creado: no se puede cambiar en una cuenta existente.
- Al eliminar la cuenta, **los archivos almacenados se conservan**, de modo que una eliminación nunca destruye sus datos. Comuníquese con el soporte técnico si necesita que se elimine el almacenamiento en sí.
- Un bucket administrado de PlaidCloud se comporta como cualquier otra cuenta de documentos en cuanto al [control de acceso](/es/guides/documents/account-management/control-document-account-access/), la [propiedad](/es/guides/documents/account-management/managing-document-account-owners/) y la exploración.
