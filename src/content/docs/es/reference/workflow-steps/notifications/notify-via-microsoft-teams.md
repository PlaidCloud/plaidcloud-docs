---
title: Notify via Microsoft Teams
description: Envíe notificaciones de Microsoft Teams desde un paso de flujo de trabajo de PlaidCloud para alertar a canales o usuarios sobre eventos y el estado del flujo de trabajo.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

Agregar notificaciones de Microsoft Teams desde un flujo de trabajo es un proceso de dos partes. Las dos partes son:


1. Crear una conexión externa de Microsoft Teams
2. Agregar pasos de notificación de Microsoft Teams a sus flujos de trabajo

## Agregar el paso de notificación de Microsoft Teams al flujo de trabajo


Agregar pasos de notificación de Microsoft Teams al flujo de trabajo es igual que agregar otros pasos. Después de agregar el paso, abra la configuración del paso, complete el formulario y guárdelo. Ya puede probar su notificación de Microsoft Teams.



## Formato del mensaje de Microsoft Teams


Teams ofrece muchas opciones de formato, como agregar imágenes y mencionar usuarios. Consulte la documentación de [Formato de texto de los mensajes de Teams](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772) para obtener más información.



## Crear la conexión externa de Microsoft Teams


Es una configuración única que permite a PlaidCloud enviar notificaciones de Microsoft Teams en su nombre. Microsoft Teams permite crear una aplicación de webhook (una forma genérica de enviar una notificación por internet). Después de crear la aplicación de webhook en Microsoft Teams, agregue las credenciales proporcionadas a PlaidCloud para permitir su uso.



### Creación de la aplicación de webhook de Microsoft Teams


Un administrador de Microsoft Teams debe realizar estos pasos. Siga los pasos descritos aquí para [crear un webhook entrante (documentación de Microsoft Teams)](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1).



### Configuración de la conexión externa de PlaidCloud


Un administrador del espacio de trabajo de PlaidCloud con permisos para crear conexiones de datos externas debe realizar estos pasos. Siga estos pasos para crear la conexión:


1. Vaya a `Analyze > Tools > External Data Connections`
2. En la selección `+ New Connection`, elija Webhook de Microsoft Teams
3. Complete el nombre y la descripción, y pegue la URL del webhook generada durante la creación del webhook anterior. El nombre que indique aquí se mostrará como la opción en el paso del flujo de trabajo, por lo que conviene que sea lo más descriptivo posible. Cualquiera que tenga la URL puede publicar en su canal, por lo que el campo **URL del webhook** la enmascara al pegarla y aparece en blanco al volver a abrir la conexión; déjelo en blanco para conservar la URL guardada.
4. Seleccione el botón `+ Create`


## Ejemplos

Todavía no hay ejemplos...
