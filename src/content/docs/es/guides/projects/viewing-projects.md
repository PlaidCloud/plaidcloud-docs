---
title: Visualización de proyectos
description: Vea y explore los proyectos de PlaidCloud a los que tiene acceso, incluidos los detalles del proyecto, el estado, los miembros y los recursos de datos asociados.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/viewing-projects.md
---

## Descripción


Dentro de **Analyze**, la función Proyectos ofrece un nivel de compartimentación que facilita mucho el control del acceso y la modificación de los privilegios. Los proyectos son los que proporcionan la segregación principal de los datos dentro de una pestaña del espacio de trabajo.



Aunque los proyectos están dentro de Analyze, los flujos de trabajo están dentro de los proyectos, es decir, los proyectos contienen flujos de trabajo. Los flujos de trabajo, en pocas palabras, realizan una amplia gama de tareas, entre ellas canalizaciones de transformación de datos, análisis de datos e incluso procesos ETL. Encontrará más información sobre los flujos de trabajo en la sección “Flujos de trabajo”.



## Acceso a los proyectos


**Para acceder a los proyectos:**


1. Abra Analyze
2. Seleccione “Proyectos” en la barra de menús superior

Esto muestra la jerarquía de proyectos. Desde aquí verá una jerarquía de los proyectos a los que tiene acceso. Puede haber proyectos adicionales dentro del espacio de trabajo pero, si no es propietario ni está asignado al proyecto, no serán visibles para usted.


## El panel Actividad

El panel **Actividad** situado a la derecha de la ventana Proyectos muestra qué se ejecutó en sus proyectos, si funcionó y quién cambió qué. Enumera la actividad de todos los proyectos a los que tiene acceso, de la más reciente a la más antigua, bajo un encabezado por cada día. Busca actividad nueva cada 15 segundos aproximadamente mientras la ventana Proyectos es la ventana activa y la pestaña del navegador está visible.

El encabezado de cada día indica **Hoy**, **Ayer** o la fecha, con un resumen de las filas de ese día, como “12 ejecuciones · 1 con error · 3 cambios”. El encabezado del día por el que se desplaza permanece en la parte superior de la lista.

### Ejecuciones

Una ejecución de un flujo de trabajo ocupa una fila. Un icono muestra cómo fue, y al pasar el cursor sobre el icono se indica el estado: Correctos, Error, Advertencia, Detenido o Iniciado. Las filas con un error o una advertencia tienen además una barra de color en el borde izquierdo.

- **La primera línea** indica el flujo de trabajo y la hora: “ahora”, hace minutos u horas si es de hoy, o la hora del reloj si es de un día anterior. Pase el cursor sobre la hora para ver la fecha completa.
- **La segunda línea** indica quién la ejecutó y en qué proyecto, como “mike ejecutó · CFO Services”, “Ejecución programada · CFO Services” o “Ejecución de sensor · CFO Services”. A la derecha figura lo que duró la ejecución, o **Error** o **Detenido** con su duración. Una ejecución detenida indica quién la detuvo.
- **Una tercera línea**, cuando la hay, muestra qué salió mal. Cuando un paso falló o generó una advertencia durante la ejecución, muestra el nombre del paso y su mensaje, con “+2 más” cuando otros pasos también tuvieron problemas. Haga clic en esa línea para abrir el flujo de trabajo en ese paso.

Mientras una ejecución está en curso, aparece en [En ejecución ahora](#en-ejecución-ahora). Cuando termina, su fila muestra el resultado. Una ejecución de un flujo de trabajo lanzada por otro flujo de trabajo, mediante un paso Flujo de trabajo: ejecutar o como macro, no tiene una fila propia, y un problema de paso dentro de ella aparece en la fila de la ejecución que la llamó. Un problema de paso cuya ejecución no está en la lista tiene una fila propia, como “Error en el paso · CRM Pipeline · CFO Services”.

Los cambios, por ejemplo en flujos de trabajo, pasos, tablas, dimensiones y proyectos, tienen una fila cada uno, como “mike modificó el paso · CFO Services” bajo el nombre del paso.

La mayoría de las filas abren lo que nombran al hacer clic en ellas o al pulsar Intro sobre ellas. Una ejecución, o un flujo de trabajo que se creó, modificó, importó o exportó, abre su proyecto en la pestaña **Flujos de trabajo** con el flujo de trabajo seleccionado. Un problema de paso, o un paso que se creó, modificó, eliminó, copió o movió, abre el flujo de trabajo en ese paso. Una tabla que se creó, cambió de nombre, publicó o dejó de publicar se abre en el Explorador de tablas, una dimensión que se creó o modificó se abre para editarla, y un proyecto que se creó, modificó, importó, exportó o del que se hizo una copia de seguridad, o cuya seguridad cambió, abre el proyecto.

### Filas repetidas

Las ediciones consecutivas del mismo tipo hechas por la misma persona en el mismo objeto se agrupan en una sola fila, y lo mismo ocurre con las ejecuciones correctas consecutivas del mismo flujo de trabajo, iniciadas de la misma manera por la misma persona o programación. Haga clic en **3 ediciones** o **4 ejecuciones** en la fila para ver cada una de ellas, y vuelva a hacer clic para plegarlas.

### En ejecución ahora

Los flujos de trabajo que se están ejecutando ahora aparecen en **En ejecución ahora**, encima de la lista, con quién los inició y cuánto tiempo llevan ejecutándose. Una ejecución en pausa indica **En pausa**. Haga clic en el nombre de un flujo de trabajo para seleccionarlo en la lista **Flujos de trabajo** de su proyecto, o haga clic en **Detener** para detener esa ejecución.

### Acciones al pasar el cursor

Pase el cursor sobre la fila de una ejecución, o vaya a ella con el teclado, para mostrar dos botones con icono, cuyas descripciones emergentes dicen **Abrir registro** y **Ejecutar flujo de trabajo**:

- **Abrir registro** abre el registro del proyecto, filtrado por ese flujo de trabajo. La fila de un problema de paso también tiene este botón.
- **Ejecutar flujo de trabajo** vuelve a ejecutar el flujo de trabajo.

**Detener** y **Ejecutar flujo de trabajo** están permitidos para los mismos miembros que pueden detener y ejecutar el flujo de trabajo desde sus propias pantallas. **Ejecutar flujo de trabajo** ejecuta todo el flujo de trabajo con su configuración predeterminada, aunque la ejecución de la fila fuera de un solo paso, de un intervalo de pasos o una simulación.

### Problemas y filtros

Cuando la actividad cargada incluye ejecuciones o pasos que fallaron o generaron advertencias, el encabezado del panel muestra un recuento como **2 problemas**, marcado como error si alguno falló. Haga clic en él para mostrar solo esas filas.

La franja de la parte inferior del panel elige lo que muestra la lista:

| Opción | Muestra |
|---|---|
| **Todos** | Todo |
| **Ejecuciones** | Ejecuciones de flujos de trabajo |
| **Cambios** | Cambios en flujos de trabajo, pasos, tablas, dimensiones, proyectos y más |
| **Problemas** | Ejecuciones y pasos que fallaron o generaron advertencias |
| **Mías** | Sus propias ejecuciones y cambios |

Escriba en **Filtro** para mostrar solo las filas cuyo nombre de flujo de trabajo, proyecto, paso, tabla, dimensión o miembro contenga su texto. La franja termina con el número de eventos que coinciden, como **12 eventos**. El panel recuerda la opción que eligió, en este navegador.

### Novedades desde su última visita

Una línea **Novedades desde su última visita** separa lo que llegó desde su visita anterior de lo que ya había visto. Se muestra cuando está elegido **Todos** y no hay nada escrito en **Filtro**. Una visita termina cuando cambia a otra ventana o cierra la ventana Proyectos, y la línea se mueve la próxima vez que abra la ventana Proyectos o vuelva a cargar la página.

### Mostrar anteriores

La lista empieza con los últimos 7 días. Haga clic en **Mostrar anteriores** al final de la lista para cargar hasta 500 eventos más de los 30 días anteriores al más antiguo cargado, y vuelva a hacer clic para retroceder más. Desaparece cuando un período de 30 días no tiene actividad.

### Teclado

Pulse Tab para moverse a una fila y use las teclas de flecha arriba y abajo para moverse entre filas e Intro para abrir la que está seleccionada. Tab también pasa a las acciones de esa fila al pasar el cursor.

### Límites

- **La última visita se recuerda por navegador.** En otro navegador o dispositivo, la línea **Novedades desde su última visita** refleja su última visita allí.
- **Los recuentos describen la actividad cargada en el panel.** El recuento de problemas, **Problemas** y los resúmenes por día abarcan al principio los 500 eventos más recientes de los últimos 7 días, y más a medida que usa **Mostrar anteriores**. No son totales de sus proyectos.
- **Una ejecución en cola aparece como Iniciado**, y pasa a **En ejecución ahora** cuando realmente comienza. Su duración se cuenta desde que se puso en cola.
- **Los problemas de paso de una macro dentro de otra macro** no aparecen en la fila de la ejecución de nivel superior.
- **Un flujo de trabajo que se ejecuta con frecuencia** tiene muchas filas. Las ejecuciones correctas consecutivas se agrupan, pero las de dos flujos de trabajo que se ejecutan por turnos no.
- **Las ejecuciones anteriores a la publicación de este panel** aparecen como Iniciado, sin resultado, y las detenciones anteriores no aparecen.
- **Un evento registrado con retraso**, cuando ya han aparecido otros más recientes, aparece al volver a cargar la página.
- **Una ventana Proyectos que se deja abierta y sin usar durante más de 30 días** continúa desde 30 días atrás.
- **Sin actividad en los últimos 7 días**, el panel dice «Sin actividad en los últimos 7 días.» y **Mostrar anteriores** no aparece, por lo que no se puede cargar la actividad anterior.
