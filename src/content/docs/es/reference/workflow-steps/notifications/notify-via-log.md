---
title: Notify Via Log
description: Escriba entradas de registro desde un paso de flujo de trabajo de PlaidCloud para dejar constancia de mensajes de estado, información de depuración y eventos de la pista de auditoría.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-log.md
---

## Descripción


Escribe un mensaje en el registro del flujo de trabajo de Analyze.



### Parámetros del mensaje


Escriba el mensaje que desea registrar. Luego seleccione uno de los tres niveles de gravedad siguientes:


* Información
* Advertencia
* Error

Tenga en cuenta que tanto las variables del proyecto como las variables del flujo de trabajo están disponibles para usarse con esta transformación.


## Ejemplos


En este ejemplo, al ejecutar esta transformación se agregará al registro un elemento de **Información** que dice *Write a message to the workflow log. I believe you have my stapler, Demo.*
