---
title: Notify Via SMS
description: Envíe un mensaje de texto desde un paso de flujo de trabajo a los miembros del espacio de trabajo que se suscribieron a las alertas de texto, con confirmación de entrega, respaldo por correo electrónico, agrupación de repeticiones y horas de silencio.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-sms.md
---

## Descripción

Envíe mensajes de texto a los miembros del espacio de trabajo cuando un flujo de trabajo requiera su atención. Un mensaje de texto solo llega a un miembro que se suscribió por su cuenta, desde **Alertas de texto** en el menú de usuario, con un número de móvil de EE. UU. que confirmó. Usted elige miembros o una lista de distribución; nunca escribe un número de teléfono en el paso. Para suscribirse, consulte [Alertas de texto](/es/guides/workflows/text-alerts/).

Los mensajes de texto son solo para números de EE. UU. No incluya datos personales de salud ni financieros en un mensaje de texto.

Los mensajes provienen de un único número de alertas de PlaidCloud y empiezan con `PlaidCloud [your workspace name]: ` seguido de su mensaje. Consulte los [Términos de SMS](https://plaidcloud.com/sms-terms/) y la [Política de privacidad de SMS](https://plaidcloud.com/sms-privacy/).

## Destinatarios

Elija **Miembros** o **Lista de distribución**.

- **Miembros** muestra los miembros de su espacio de trabajo. Cada uno aparece como **Suscrito**, **No suscrito** o **Baja de alertas - Envíe START por mensaje de texto al número de alertas**.
- **Lista de distribución** envía un mensaje de texto a todos los miembros de la lista que se hayan suscrito.

Un miembro que no se ha suscrito no recibe ningún mensaje de texto. Es un problema para el paso (consulte **Si no se puede entregar un mensaje de texto**) y, de forma predeterminada, recibe el mensaje por correo electrónico.

## Mensaje

Escriba el **Mensaje**. Las variables del proyecto y las variables del flujo de trabajo funcionan, y **Insertar variable** agrega cualquiera de estas:

| Variable | Valor |
|---|---|
| `{workflow_name}` | El nombre del flujo de trabajo en ejecución |
| `{project_name}` | El nombre del proyecto |
| `{run_url}` | Un enlace a la ejecución en PlaidCloud |
| `{project}`, `{model}`, `{cloud}`, `{date}` | Las variables existentes |

El contador situado bajo el mensaje muestra aproximadamente cuántos caracteres y segmentos ocupa el texto, incluidos el prefijo `PlaidCloud [workspace]:` y el enlace de la ejecución. Un mensaje de texto se recorta a partir de 3 segmentos. Se rechazan los enlaces de acortadores de enlaces públicos.

## Entrega

| Configuración | Qué hace |
|---|---|
| **Si no se puede entregar un mensaje de texto** | **Hacer que el paso falle** (valor predeterminado) o **Advertir y continuar**. Un mensaje de texto que no se entrega nunca pasa en silencio: siempre se informa en el paso. |
| **Enviar correo electrónico a los destinatarios cuyo mensaje de texto no se pueda entregar** | Activado de forma predeterminada. Un miembro cuyo mensaje de texto falla, que no se ha suscrito o que solicitó la baja recibe el mensaje por correo electrónico. |
| **Agrupar repeticiones durante (minutos)** | Valor predeterminado: 60. No se envía una repetición del mismo mensaje al mismo miembro dentro de este tiempo, y el siguiente mensaje de texto que salga termina con `(+N similar since HH:MM)`. |
| **Retener mensajes de texto durante las horas de silencio** | Elija las horas **Desde** y **a** y una zona horaria. Un mensaje de texto que saldría dentro de esa ventana se retiene hasta que termine. |

Cada miembro recibe como máximo 20 mensajes de texto al día, un espacio de trabajo envía como máximo 500 mensajes de texto y correos de respaldo al día, y un paso envía mensajes de texto a un máximo de 50 miembros a la vez.

## Enviarme una prueba

**Enviarme una prueba** envía un mensaje de texto de prueba a su propio número y muestra el resultado junto al botón. Si no se ha suscrito, se abre la ventana **Alertas de texto** para que pueda hacerlo.

## Qué ven los destinatarios

Todos los mensajes de texto provienen del número de alertas. Al responder **STOP** se detienen todos los mensajes de texto de PlaidCloud a ese número, y **HELP** devuelve la información de contacto. Después de STOP, un miembro debe enviar **START** por mensaje de texto al número de alertas para reanudarlos y luego volver a activar las alertas de texto en **Alertas de texto**. El formulario del paso muestra **Baja de alertas - Envíe START por mensaje de texto al número de alertas** junto a ese miembro hasta que lo haga.

Los administradores del espacio de trabajo pueden ver el estado de las alertas de texto de cada miembro, con el número enmascarado, en la pestaña **Información del miembro** de la ventana del miembro. Los miembros se suscriben y se dan de baja por su cuenta; un administrador no puede hacerlo por ellos.

## Pasos que usaban un número escrito

Una versión anterior de este paso aceptaba un proveedor de telefonía móvil y un número de teléfono escrito. Un paso que aún esté guardado de ese modo no hace fallar el flujo de trabajo y no envía ningún mensaje de texto al número escrito.

- **Sin destinatarios elegidos:** el paso termina con una advertencia, *No text was sent: this step still uses the retired mobile provider and number. Open the step, choose members who've opted in to text alerts, and save it.* No se envía nada.
- **Miembros o una lista de distribución elegidos:** el paso envía mensajes de texto a esos destinatarios e ignora el operador y el número sobrantes.

Para corregir un paso, ábralo, elija miembros o una lista de distribución y guárdelo.

## Ejemplos

Todavía no hay ejemplos...
