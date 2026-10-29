---
title: Encrypt File and Decrypt File
description: Cifre o descifre un archivo de documento completo con AES o Blowfish, o agregue o quite la contraseña de un libro de Excel, en un paso de flujo de trabajo de PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/encrypt-decrypt-file.md
---

## Descripción

**Documento: cifrar archivo** cifra un archivo de una cuenta de documentos y escribe el resultado en otro archivo. **Documento: descifrar archivo** hace lo contrario. Ambos pasos tienen la misma configuración. Úselos para recibir archivos cifrados de un socio, descifrarlos antes de que una importación los lea y cifrar una exportación antes de que salga hacia otro sistema.

## Archivos

| Configuración | Obligatoria | Qué hace |
| --- | --- | --- |
| Archivo de origen | Sí | El archivo que se cifra o descifra. |
| Archivo de destino | Sí | El archivo que se escribe. Debe ser distinto del archivo de origen, para que una nueva ejecución nunca trabaje sobre su propia salida. |
| Eliminar el archivo de origen una vez escrito el archivo de destino | No | Quita el archivo de origen después de escribir correctamente el archivo de destino. |

Un archivo de origen que no existe no es un error: el paso termina con una advertencia que indica la ruta y no escribe nada, y el flujo de trabajo continúa. Un archivo de origen vacío escribe un archivo de destino vacío con una advertencia, salvo que cifrar un archivo vacío con AES o Blowfish escribe un archivo cifrado real. No se puede usar una cuenta de documentos de Smartsheet, porque los archivos no se pueden volver a leer desde ella.

## Parámetros

| Configuración | Qué hace |
| --- | --- |
| Algoritmo | En el grupo Cifrado: **AES-128 (clave de 16 bytes)**, **AES-192 (clave de 24 bytes)**, **AES-256 (clave de 32 bytes)**, **Blowfish (clave de 4 a 56 bytes)** o **Contraseña del libro de Excel**. |
| Modo | **CBC** (el valor predeterminado), **ECB** o **GCM**. Blowfish admite solo CBC o ECB. |
| Variable de clave | La variable de flujo de trabajo o de proyecto que contiene la clave de cifrado, como `{aes_key}`. Obligatoria para AES y Blowfish. |
| Codificación de la clave y el IV | Cómo se escriben la clave y el IV: **Texto (UTF-8)**, **Hexadecimal** o **Base64**. |
| IV fijo | El vector de inicialización. Si lo deja en blanco, el cifrado inicia el archivo con un IV aleatorio, que el descifrado lee desde el comienzo del archivo. El cifrado GCM siempre usa un IV aleatorio, así que déjelo en blanco para GCM. |
| Variable de contraseña del libro | La variable de flujo de trabajo o de proyecto que contiene la contraseña que se establece en un libro de Excel, o se quita de él, como `{xlsx_password}`. Obligatoria para **Contraseña del libro de Excel**. |

CBC y ECB rellenan con PKCS7, y GCM agrega una etiqueta de autenticación de 16 bytes después de los datos cifrados. Un archivo GCM puede ocupar hasta 256 MB. Una clave o un IV incorrectos detienen el paso con un error y no dejan ningún archivo parcial.

## Las claves residen en variables

**Variable de clave** y **Variable de contraseña del libro** aceptan únicamente una referencia a una variable, como `{aes_key}`, nunca la clave o la contraseña en sí: se rechaza guardar un paso con cualquier otra cosa en ellas. Coloque el secreto en una [variable de flujo de trabajo](/es/guides/workflows/manage-workflow-variables/) o en una variable de proyecto, de modo que se establezca en un solo lugar y nunca aparezca en el paso, en sus versiones, en sus copias ni en lo que lee de vuelta un asistente de IA. El paso lee el valor de la variable cuando se ejecuta. **IV fijo** es un campo de contraseña, por lo que su valor se oculta en el formulario.

Los pasos que tenían una clave o contraseña escrita antes de esta regla la vieron trasladada automáticamente a una nueva variable de proyecto, visible solo para los Arquitectos, y ahora hacen referencia a esa variable.

## Relacionado

- [Pasos de documento](/es/reference/workflow-steps/document/)
- [Administrar variables de flujo de trabajo](/es/guides/workflows/manage-workflow-variables/)
