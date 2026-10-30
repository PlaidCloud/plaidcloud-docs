---
title: Notify via Slack
description: Envíe notificaciones de Slack desde un paso de flujo de trabajo de PlaidCloud para alertar a canales o usuarios sobre eventos, errores y el estado del flujo de trabajo.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-slack.md
---

Agregar notificaciones de Slack desde un flujo de trabajo es un proceso de dos partes. Las dos partes son:


1. Crear una conexión externa de webhook de Slack
2. Agregar pasos de notificación de Slack a sus flujos de trabajo

## Agregar el paso de notificación de Slack al flujo de trabajo


Agregar pasos de notificación de Slack al flujo de trabajo es igual que agregar otros pasos. Después de agregar el paso, abra la configuración del paso, complete el formulario y guárdelo. Ya puede probar su notificación de Slack.



## Adjuntar un archivo

Elija un documento en **Archivo para cargar** para enviarlo al canal con el mensaje como comentario. Un webhook no puede transportar un archivo, por lo que un archivo adjunto pasa por un token de bot en la conexión de Slack:

- Agregue un **Token de bot** a la conexión. Es el token `xoxb-` de una aplicación de Slack que tiene el alcance `files:write`, y la aplicación debe estar invitada al canal.
- Escriba el **ID del canal** en el paso, como `C0123ABCD`, no el nombre del canal. La carga de archivos de Slack solo acepta ID, y el paso falla si no se indica uno. Para encontrar un ID, abra los detalles del canal en Slack y desplácese hasta el final.
- Si no se encuentra el documento, el mensaje se envía por webhook sin él, y el paso advierte con la ruta del documento.

## Formato del mensaje de Slack


Slack ofrece muchas opciones de formato, como agregar imágenes y mencionar usuarios. Consulte la documentación de [Formato de texto de Slack](https://api.slack.com/reference/surfaces/formatting) para obtener más información.



## Crear la conexión externa de webhook de Slack


Es una configuración única que permite a PlaidCloud enviar notificaciones de Slack en su nombre. Slack permite crear una aplicación de webhook (una forma genérica de enviar una notificación por internet). Después de crear la aplicación de webhook en Slack, agregue las credenciales proporcionadas a PlaidCloud para permitir su uso.



### Creación de la aplicación de webhook de Slack


Un administrador de Slack debe realizar estos pasos. Siga estos pasos para crear una aplicación de webhook de Slack:


1. En Slack, abra el menú de control del espacio de trabajo y seleccione `Settings & administration > Manage Apps`
2. Seleccione `Custom Integrations` en la lista de categorías de aplicaciones
3. Seleccione `Incoming Webhooks` en la lista de aplicaciones
4. Seleccione el botón `Add to Slack`
5. En la pantalla siguiente, seleccione el canal de Slack en el que desea publicar los mensajes y continúe. Este es el canal predeterminado que se usará, pero se puede reemplazar en cada notificación, incluido el envío de mensajes directos a personas específicas.
6. Copie la URL del webhook que se muestra. Se usará más adelante, así que consérvela en un lugar seguro. Tendrá un aspecto similar a este: `https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. Puede personalizar el aspecto, el nombre y el emoji antes de guardar. Estas personalizaciones son solo los valores predeterminados y se pueden reemplazar en cada paso de notificación dentro de un flujo de trabajo de PlaidCloud.

### Configuración de la conexión externa de PlaidCloud


Un administrador del espacio de trabajo de PlaidCloud con permisos para crear conexiones de datos externas debe realizar estos pasos. Siga estos pasos para crear la conexión:


1. Vaya a `Analyze > Tools > External Data Connections`
2. En la selección `+ New Connection`, elija Webhook de Slack
3. Complete el nombre y la descripción, y pegue la URL del webhook proporcionada en el paso 6 anterior. El nombre que indique aquí se mostrará como la opción en el paso del flujo de trabajo, por lo que conviene que sea lo más descriptivo posible. Cualquiera que tenga la URL puede publicar en su canal, por lo que el campo **URL del webhook** la enmascara al pegarla y aparece en blanco al volver a abrir la conexión; déjelo en blanco para conservar la URL guardada.
4. Para enviar archivos adjuntos, pegue también el token de bot de la aplicación de Slack en el campo **Token de bot (para cargar archivos)**. Una conexión puede contener la URL del webhook, el token de bot o ambos. El token de bot se enmascara igual que la URL del webhook y aparece en blanco al volver a abrir la conexión.
5. Seleccione el botón `+ Create`


## Ejemplos

Todavía no hay ejemplos...
