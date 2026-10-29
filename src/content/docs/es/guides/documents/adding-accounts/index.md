---
title: Agregar nuevas cuentas de documentos
description: "Conecte almacenamiento de documentos en la nube y local a PlaidCloud: S3, GCS, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV y más."
sidebar:
  label: Agregar nuevas cuentas de documentos
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

Conecte almacenamiento de documentos en la nube y local a PlaidCloud: S3, Google Cloud Storage, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV y más. Cada proveedor tiene sus propias credenciales y su propio flujo de conexión.

La opción más rápida es un **Bucket administrado de PlaidCloud**, en el que PlaidCloud configura y administra el almacenamiento por usted: solo elige un nombre, sin nada más que configurar. Para conectar almacenamiento que ya posee, elija el proveedor correspondiente a continuación.

## Los secretos guardados son de solo escritura

El secreto de una cuenta, el campo llamado **Clave privada / Contraseña** o, según el tipo de cuenta, **Clave de acceso secreta**, **Clave de la cuenta**, **Secreto de cliente**, **Token de acceso**, **Contraseña**, **Clave JSON del usuario del sistema** o **JSON de credenciales de OAuth2**, es de solo escritura, al igual que la **RSA Private Key** de una cuenta de SFTP. Una vez guardados, nunca se vuelven a mostrar, ni en el formulario, ni en la API, ni a un asistente de IA. Cuando edita una cuenta, el campo aparece vacío con la sugerencia *Paste the value; leave blank on edit to keep the saved one.* Déjelo en blanco para conservar el secreto guardado, o pegue uno nuevo para reemplazarlo.

Cambiar el lugar al que se conecta una cuenta requiere volver a introducir su secreto. Si cambia la primera parte de la **Ruta de inicio** (en el almacenamiento en la nube, el bucket o el contenedor), el **Host o dirección IP** o el **Puerto de conexión SSH** de una cuenta de SFTP, o el **ID de inquilino de OneDrive** de una cuenta de OneDrive, pegue también el secreto, o se rechazará el guardado con el mensaje *Changing where the account connects needs its secret entered again*. Esto impide que alguien que puede editar una cuenta pero nunca vio su secreto lo envíe a un servidor que él elija.

Un asistente de IA conectado mediante el conector MCP de PlaidCloud también puede crear y actualizar cuentas, con un tipo de almacenamiento, credenciales y una ruta de inicio. Las credenciales son de solo escritura y se ocultan cuando se vuelve a leer la cuenta. Para ver un ejemplo detallado, consulte [Agregar una cuenta de OneDrive / SharePoint](/es/guides/documents/adding-accounts/add-onedrive-account/#crear-la-cuenta-con-un-asistente-de-ia).
