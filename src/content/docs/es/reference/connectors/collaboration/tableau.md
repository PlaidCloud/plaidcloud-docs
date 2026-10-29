---
title: Conexión de Tableau
description: Conecte PlaidCloud a Tableau Server o Tableau Cloud con un token de acceso personal para que los flujos de trabajo puedan publicar orígenes de datos.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/collaboration/tableau.md
---

Una conexión de Tableau contiene la dirección de un sitio de Tableau Server o Tableau Cloud y un token de acceso personal. El paso [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/) la usa para publicar extractos `.hyper` como orígenes de datos.

## Antes de empezar

En Tableau, cree un token de acceso personal para la cuenta que debe publicar: elija **My Account Settings** y luego **Personal Access Tokens**. Copie el secreto del token cuando Tableau lo muestre, porque Tableau no lo vuelve a mostrar. La cuenta necesita permiso para publicar orígenes de datos en el proyecto en el que va a publicar.

## Crear la conexión

1. Abra **Analyze**, elija **Tools → Conexiones de datos externas** y seleccione **+ Nueva conexión → Tableau**.
2. Escriba el nombre y la descripción de la conexión.
3. Escriba la configuración de la conexión:

| Campo | Qué escribir |
| --- | --- |
| **URL del servidor** | La dirección del servidor o del pod de Tableau Cloud, como `https://prod-useast-a.online.tableau.com`. Un host sin protocolo se interpreta como `https`, y una dirección `http` se rechaza. |
| **Sitio** | La URL de contenido del sitio, la parte de la dirección del navegador que sigue a `#/site/`. Déjelo en blanco para el sitio predeterminado (Default). |
| **Nombre del token de acceso personal** | El nombre que le dio al token en Tableau. |
| **Secreto del token de acceso personal** | El secreto del token. Se almacena cifrado y aparece en blanco cuando vuelve a abrir la conexión. Déjelo en blanco para conservar el secreto guardado. |

4. Seleccione **Crear**.

El servidor debe ser accesible desde internet. PlaidCloud no se conecta a un servidor de Tableau en una red privada.

## Temas relacionados

- [Publish to Tableau](/es/reference/workflow-steps/export/export-to-tableau/)
- [Tableau Hyper Export](/es/reference/workflow-steps/export/export-hyper/)
