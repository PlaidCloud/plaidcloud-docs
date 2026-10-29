---
title: Alertas de texto
description: Active la recepción de alertas de flujos de trabajo de PlaidCloud como mensajes de texto en su número de móvil de EE. UU. y desactívelas de nuevo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/text-alerts.md
---

Los flujos de trabajo pueden enviarle un mensaje de texto cuando necesitan atención, con el paso [Notify Via SMS](/es/reference/workflow-steps/notifications/notify-via-sms/). Un flujo de trabajo solo puede enviarle mensajes de texto después de que usted mismo se haya suscrito.

## Activar las alertas de texto

1. Abra el menú de usuario en la esquina superior derecha y elija **Alertas de texto**.
2. Introduzca su **Número de móvil de EE. UU.**.
3. Marque **Acepto recibir alertas de texto de flujos de trabajo de PlaidCloud en este número.** Lea las divulgaciones que aparecen encima y los enlaces **SMS Terms** y **SMS Privacy Policy**.
4. Haga clic en **Enviar código**. PlaidCloud envía por mensaje de texto un código de 6 dígitos a su número. Los mensajes pueden tardar uno o dos minutos en llegar.
5. Introduzca el **Código de confirmación** en un plazo de 10 minutos y haga clic en **Confirmar**.

Después de enviar un código, el botón realiza una cuenta atrás de 60 segundos y luego muestra **Reenviar código**. Si reenvía mientras su código sigue siendo válido, se envía el mismo código, así que sirve cualquiera de los mensajes que llegue. Puede solicitar 3 códigos por número de teléfono al día y 3 por persona por hora.

La ventana mostrará entonces **Las alertas de texto están activadas para** su número enmascarado. Solo se admiten números de móvil de EE. UU. Pueden aplicarse tarifas de mensajes y de datos, y la frecuencia de los mensajes varía.

## Desactivar las alertas de texto

Abra **Alertas de texto** y haga clic en **Detener alertas de texto**, o responda **STOP** a cualquier mensaje. Responda **HELP** para obtener ayuda.

## Volver a activarlas después de STOP

Responder STOP bloquea todos los mensajes a su número. Envíe **START** por mensaje de texto al número de alertas que se muestra en la ventana, luego envíe un código nuevo y confírmelo.

## Si algo sale mal

| Mensaje | Qué hacer |
|---|---|
| Ese código no es correcto | Revise el mensaje y vuelva a introducir el código. |
| Ese código ha caducado | Haga clic en **Enviar código** para obtener uno nuevo. |
| Demasiados códigos incorrectos | Tras 5 códigos incorrectos, haga clic en **Enviar código** para obtener uno nuevo. |
| Introduzca un número de móvil de EE. UU. válido | Use un número de móvil de EE. UU. de 10 dígitos. |
| Demasiadas solicitudes | Alcanzó un límite de códigos. Espere unos minutos e inténtelo de nuevo. |
| Las alertas de texto no están disponibles para su espacio de trabajo en este momento | Inténtelo de nuevo más tarde. |

No use las alertas de texto para datos personales de salud o financieros. Preguntas: support@plaidcloud.com.
