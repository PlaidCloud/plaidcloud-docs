---
title: Alertas y resúmenes
description: Notifique a las personas cuando un número de una aplicación Panel supere un límite, o envíe un resumen programado de números clave mediante notificación push, correo electrónico, Slack o Microsoft Teams.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/alerts-and-digests.md
---

Una **alerta** vigila un número de los datos de una aplicación Panel y le avisa en el momento en que supera un límite. Un **resumen** envía un breve compendio de hasta 10 números cada día o cada semana. Ambos se configuran desde la aplicación en [Panel Studio](/es/guides/panel-apps/studio/), y ambos son suyos: solo usted ve y modifica los propios.

## Abrir alertas y resúmenes

1. En **Mis aplicaciones Panel** o en el tablero **Inicio** de un proyecto, elija **Open in Studio** en la aplicación.
2. Elija **Alerts & Digests**.

La ventana tiene una pestaña **Alerts** y una pestaña **Digests**. La aplicación debe estar asignada a un proyecto, y sus tablas son las de ese proyecto.

## Definir un número para vigilar

Las alertas y los resúmenes miden un **KPI** que usted crea a partir de una tabla del proyecto de la aplicación:

| Campo | Qué establece |
|---|---|
| **Tabla** | La tabla que se lee. Debe estar creada. |
| **Measure column** | La columna que se suma o se cuenta. |
| **Función** | `sum`, `avg`, `min`, `max`, `count` o `count_distinct`. |
| **Añadir filtro** | Condiciones opcionales que restringen las filas, cada una con una columna, una comparación y un valor. Para *is in*, separe los valores con comas. **Remove filter** quita una. |

El número siempre se calcula con su propio acceso a la tabla, incluida la [seguridad a nivel de fila](/es/guides/panel-apps/accessing-data/). Nunca ve ni envía una cifra de filas que no puede leer.

## Crear una alerta

1. En la pestaña **Alerts**, elija **Nuevo**.
2. Escriba un **Nombre**.
3. Cree el KPI.
4. En **Alert when the KPI is**, elija `>`, `>=`, `<` o `<=` e ingrese un **Umbral**.
5. Elija cómo recibir el aviso en **Send by** (consulte [Canales](#canales)).
6. Deje marcado **Habilitado** y elija **Guardar**.

PlaidCloud comprueba cada alerta habilitada una vez por hora. Una alerta se dispara una vez cada vez que el número supera el umbral y luego permanece en silencio hasta que el número vuelve al lado seguro y lo supera de nuevo. La lista muestra cuándo se disparó por última vez cada alerta, y **(off)** después del nombre de una que está desactivada.

Puede tener hasta 20 alertas propias en una aplicación.

## Crear un resumen

1. En la pestaña **Digests**, elija **Nuevo**.
2. Escriba un **Nombre**.
3. Elija **Add KPI**, asígnele una **KPI label** y cree el número. Repita hasta con 10 KPI. **Remove KPI** quita uno.
4. Junto a **Enviar**, elija **Cada día** o **Cada semana**.
5. Elija cómo enviarlo en **Send by** y elija **Guardar**.

Un resumen se envía una vez al día o a la semana, en la primera comprobación horaria posterior al inicio del período, con el período en UTC. La lista muestra cuándo se envió por última vez cada resumen. Un KPI cuyo resultado queda sin filas por su acceso a la tabla se muestra como sin datos, nunca como una cifra sin filtrar.

Puede tener hasta 10 resúmenes propios en una aplicación y 20 en total entre todas las aplicaciones.

## Canales

| Send by | Adónde va |
|---|---|
| **Push notification** | La aplicación móvil de PlaidCloud en sus dispositivos. Solo para alertas. |
| **Correo electrónico** | La dirección de correo electrónico de su cuenta. |
| **Slack** | Un canal de Slack, mediante una conexión de Slack. |
| **Microsoft Teams** | Un canal de Teams, mediante una conexión de Microsoft Teams. |

Para **Slack** y **Microsoft Teams**, elija la **Conexión** por la que se publicará. Un administrador del espacio de trabajo crea la conexión, y a usted se le debe haber concedido acceso a ella. La dirección de la conexión debe comenzar con `https`.

### Qué muestra una tarjeta de Slack o Teams

Una tarjeta muestra las cifras solo cuando su propio acceso a la tabla no tiene restricciones, es decir, ninguna seguridad a nivel de fila limita las filas que puede leer. Si su acceso se limita a algunas filas, la tarjeta indica que hay nuevos valores disponibles y enlaza a la aplicación, donde cada lector ve solo las filas que su propio acceso permite. Cada tarjeta incluye un vínculo a la aplicación. Los miembros de un canal se administran fuera de PlaidCloud, por lo que los números de un propietario con restricciones no se envían a uno.

## Cuando falla la entrega

Una alerta o un resumen que no se puede entregar durante 24 horas seguidas, por ejemplo porque se eliminó su conexión de Slack, se desactiva. La lista lo muestra como **(off)** y el formulario indica cuántas entregas fallaron. Corrija el canal, marque **Habilitado** y elija **Guardar** para volver a activarlo.

## Editar o eliminar

Elija un elemento de la lista para modificarlo y **Guardar**. Elija **Eliminar** para quitarlo. Si cambia de elemento con cambios sin guardar, PlaidCloud le pregunta antes de descartarlos.

## Siguientes pasos

- [Panel Studio](/es/guides/panel-apps/studio/): desde donde accede a **Alerts & Digests**.
- [El kit de aplicaciones Panel](/es/guides/panel-apps/app-kit/): cree la aplicación que vigilan las alertas.
