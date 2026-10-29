---
title: Administrar errores de pasos
description: Administre los errores de pasos en los flujos de trabajo de PlaidCloud, incluidas las notificaciones de error, la lógica de reintento y las opciones de recuperación ante fallos.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/managing-step-errors.md
---

Si un flujo de trabajo experimenta un error durante el procesamiento, se muestra un indicador de error tanto en el flujo de trabajo como en el paso que tuvo el error. PlaidCloud puede reintentar un paso fallido varias veces. Esto suele ser útil si el paso accede a sistemas remotos o a datos que pueden no estar siempre disponibles o que fallan de forma intermitente por motivos desconocidos. El reintento puede configurarse para repetirse muchas veces, además de agregar una espera entre reintentos que va de segundos a horas.



Un paso cuyo servidor se pierde a mitad de la ejecución se trata de forma independiente de los reintentos: un paso que es seguro repetir se vuelve a ejecutar automáticamente, y uno que no lo es falla una sola vez con un mensaje de **interrumpido**. Consulte [Pasos interrumpidos](/es/guides/workflows/run-a-workflow/#pasos-interrumpidos).

Cuando PlaidCloud rechaza un paso por un motivo que usted puede corregir, como un permiso faltante o una configuración no válida, el registro del paso muestra ese mensaje en palabras sencillas en lugar de un error del servidor con un seguimiento de pila. Un paso Model Loop, Model Run o Macro Run cuyo flujo de trabajo secundario falla muestra el mensaje de error propio del flujo secundario, como “Child workflow run failed:” seguido del mensaje.

Si no se selecciona ningún reintento o se supera el número máximo de reintentos, el paso se marca como error. En ese caso, PlaidCloud ofrece tres niveles de manejo de errores:


* Detener el flujo de trabajo cuando ocurre un error
* Marcar el paso como error pero seguir procesando el flujo de trabajo
* Marcar el paso como error y activar un proceso de flujo de trabajo de corrección en lugar de continuar con el flujo de trabajo actual

## Detener el flujo de trabajo


Detener el flujo de trabajo cuando un paso falla es el enfoque más común, ya que los flujos de trabajo generalmente deben ejecutarse sin errores. Esto detiene el flujo de trabajo y muestra el indicador de error tanto en el paso como en el flujo de trabajo. El error también se muestra en el monitor de actividad, pero no se realiza ninguna otra acción.



## Seguir procesando


Cada paso puede configurarse para continuar en caso de error en el formulario del paso. Si esta casilla está habilitada, cualquier paso se marcará con un error si este ocurre, pero el flujo de trabajo tratará el error como la finalización del paso y continuará. Esto suele ser útil si hay pasos que realizan tareas que pueden fallar cuando faltan datos pero que son inofensivas para el proceso en general.



Dado que en este caso el flujo de trabajo continúa a pesar del error, no mostrará un indicador de error y seguirá mostrando un indicador de ejecución.



## Activar flujo de trabajo de corrección


Con la posibilidad de establecer un flujo de trabajo de corrección como parte de la configuración del flujo de trabajo, un error del flujo de trabajo detiene de inmediato el procesamiento del flujo de trabajo actual e inicia el procesamiento del flujo de trabajo de corrección. Tenga en cuenta que, si un paso está marcado para continuar en caso de error, un fallo no activará el flujo de trabajo de corrección. Solo activan el proceso de corrección los pasos que fallan y que además harían que se detuviera todo el flujo de trabajo.



Un flujo de trabajo de corrección puede ser útil simplemente para avisar a las personas de que ocurrió un fallo, o puede realizar otros procesamientos complejos para intentar corregir automáticamente las causas subyacentes por las que falló el flujo de trabajo original.
