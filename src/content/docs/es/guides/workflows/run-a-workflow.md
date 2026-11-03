---
title: Ejecutar un flujo de trabajo
description: Ejecute un flujo de trabajo de PlaidCloud manualmente o a demanda, siga el estado de cada paso, y pause, detenga o reanude una ejecución desde donde se quedó.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Puede iniciar una ejecución completa de un flujo de trabajo haciendo clic en el icono de ejecución de la jerarquía **Flujos de trabajo** o seleccionando **Run All** en el menú **Acciones** de un flujo de trabajo específico.



También puede hacer clic en el botón **Toggle Start/Stop** en la parte superior de la tabla de flujos de trabajo. Este botón de alternancia detiene un flujo de trabajo en ejecución o inicia un flujo de trabajo.

Si hace clic en **Ejecutar** en un flujo de trabajo que ya se está ejecutando, PlaidCloud se lo indica en lugar de iniciar una segunda ejecución.

## Elegir un modo de contabilización

Cada ejecución lleva un modo de contabilización en ERP. Para elegir uno en PlaidCloud, use **Ejecutar con modo de contabilización** en el menú contextual de un flujo de trabajo, o el botón de modo de ejecución del lienzo del flujo de trabajo; **Iniciar flujo de trabajo** o **Ejecutar flujo de trabajo** a secas solicita el modo En vivo, sujeto aun así al límite del proyecto que se describe más abajo. También puede elegir el modo al iniciar una ejecución mediante la API de ejecución o el asistente.

| Modo | Qué ocurre |
|---|---|
| En vivo | Los pasos de contabilización contabilizan exactamente como siempre. Es el valor predeterminado. |
| Simular | Cada paso de contabilización en ERP genera y valida exactamente lo que contabilizaría, y luego no confirma nada ni se comunica nunca con el ERP. Los asientos que se contabilizarían se registran en el [Historial de contabilización en ERP](/es/guides/connections/erp-post-history/), marcados como simulados, para que pueda revisarlos antes de ejecutar en vivo. |
| Desactivado | Los pasos de contabilización se omiten por completo. |

Un proyecto también tiene su propio límite de modo de contabilización, que establece mediante la API del proyecto o el asistente cualquier miembro con acceso de escritura a un proyecto desbloqueado. El límite solo hace que una ejecución sea más segura, nunca más permisiva: el modo efectivo de una ejecución es el más restrictivo entre el modo que usted eligió y el límite del proyecto, de modo que un proyecto limitado a Simular sigue simulado aunque inicie la ejecución en modo En vivo.

Un [evento programado](/es/administration/scheduled-events/event-scheduler/#modo-de-contabilización-en-erp) conserva su propio modo de contabilización, por lo que una programación configurada en Simular se ejecuta simulada cada vez que se activa.

El modo se transmite a todo lo que toca la ejecución. Un subflujo de trabajo, una macro y un paso **Run Model**, **Conditional Run Model** o **Loop Model** heredan el modo de la ejecución principal, y también lo hace una ejecución que [reanude](#pausar-detener-y-reanudar) tras una detención: una ejecución simulada no puede contabilizar de verdad en ningún punto de su interior.

:::caution
Los pasos de contabilización de SAP, de adjuntos de SAP y de RFC genéricas de SAP no admiten simulación. En Simular o Desactivado se omiten por completo, porque los indicadores de prueba propios de SAP siguen abriendo una conexión real con SAP: omitir el paso es la única forma de que una ejecución simulada nunca llegue a SAP.
:::

:::note
Un paso individual de contabilización en ERP también tiene su propia configuración Validate Only (con la etiqueta Preview o Test Only Mode en algunos pasos), independiente del modo de contabilización de la ejecución descrito arriba. El editor de pasos siempre la guarda de forma explícita. Una configuración de paso escrita de otro modo (la API REST, MCP o la importación de un paquete de flujo de trabajo) que omita por completo esa configuración ahora también se establece de forma predeterminada en una vista previa en lugar de una contabilización en vivo.
:::

## Autorizar al proyecto para contabilizar

Una ejecución de flujo de trabajo contabiliza en un ERP como el proyecto, no como la persona que la inició. Antes de que una ejecución pueda contabilizar, el proyecto necesita una autorización para cada conexión y entorno de ERP que usen sus pasos de contabilización. Sin ella, el paso falla con el mensaje "This project isn't authorized to post to connection …", que indica la conexión y el entorno. Los pasos **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** y **Call SAP RFC** no la necesitan.

Para autorizar un proyecto, abra su página de inicio y seleccione **Autorizaciones de escritura en ERP** en **Contabilización en ERP**. Cada fila es una conexión en un entorno. Marque **Autorizado** para permitir que el proyecto contabilice allí, o desmárquelo para impedirlo. **Autorizado por** y **Autorizado el** muestran quién lo autorizó por última vez y cuándo.

- El botón se muestra a los Arquitectos del proyecto y a los administradores del espacio de trabajo, pero solo un Arquitecto puede cambiar una autorización, y solo mientras el proyecto está desbloqueado. Un administrador del espacio de trabajo que no sea Arquitecto puede agregarse primero como Arquitecto.
- Al seleccionar una fila para autorizarla o borrar su autorización no se recarga la lista: la posición de desplazamiento y cualquier orden de columnas que haya elegido se conservan. La ventana se puede redimensionar, y la nota sobre los proyectos públicos se ajusta para mostrarse completa.
- Para autorizar una conexión, usted también necesita acceso de escritura a ella: es su propietario, o se compartió con usted por nombre o mediante uno de sus grupos de seguridad. Una conexión establecida en **Todos los miembros del espacio de trabajo** no cuenta.
- Un proyecto establecido en **Todos los miembros del espacio de trabajo** se autoriza como cualquier otro. Todos los miembros son Arquitectos del proyecto, por lo que cualquier miembro con acceso de escritura a una conexión puede autorizar el proyecto para ella. Una vez autorizado, cualquier miembro puede contabilizar en esa conexión desde los flujos de trabajo del proyecto, y la ventana lo indica encima de la cuadrícula.
- Un proyecto copiado, o uno creado a partir de un archivo de proyecto, comienza sin autorizaciones. Autorice la copia antes de que contabilice.

## Seguir el estado de un paso

Mientras se ejecuta un flujo de trabajo, cada paso muestra un icono de estado que indica en qué punto se encuentra, junto con el tiempo que lleva en ejecución. Pase el cursor sobre el icono para ver el mensaje que hay detrás.

| Estado | Qué significa |
|---|---|
| En espera | El paso está en cola y aún no ha comenzado. |
| En ejecución | El paso está trabajando y su duración aumenta mientras avanza. |
| Completado | El paso terminó correctamente. |
| Advertencia | El paso terminó, pero señaló algo que vale la pena leer en el [registro del flujo de trabajo](/es/guides/workflows/viewing-workflow-log/). |
| Error | El paso falló. Consulte [Gestionar errores de pasos](/es/guides/workflows/managing-step-errors/). |
| Omitido | El paso se pasó por alto: está deshabilitado o no se cumplieron sus condiciones de ejecución. Consulte [Omitir pasos en un flujo de trabajo](/es/guides/workflows/skip-steps-in-a-workflow/). |
| Continuado | El paso falló, pero está configurado para continuar en caso de error, por lo que el flujo de trabajo siguió adelante. Consulte [Continuar en caso de error](/es/guides/workflows/continue-on-error/). |
| Detenido | La ejecución se detuvo antes de que el paso pudiera terminar. |
| Abandonado | La ejecución del paso se interrumpió, por lo que nunca terminará. Reanude la ejecución o vuelva a ejecutar el flujo de trabajo. |

Una vista de flujo de trabajo abierta se actualiza sola a medida que avanza una ejecución, de modo que los estados que está viendo se mantienen al día sin recargar la página.

### Pasos abandonados

Un paso se marca como **abandonado** cuando lo que lo estaba ejecutando desapareció a mitad de la ejecución, con mayor frecuencia porque alguien presionó **Detener**, o porque el mantenimiento de la plataforma interrumpió la ejecución. La duración del paso deja de aumentar y la información sobre herramientas del estado explica lo ocurrido.

Un paso abandonado no se completó y no produjo ninguna salida. No es un paso lento, ni un problema con sus datos o su configuración.

Para retomar el trabajo, [**reanude**](#pausar-detener-y-reanudar) la ejecución (el paso abandonado se ejecuta de nuevo) o vuelva a ejecutar todo el flujo de trabajo. Ambas opciones son seguras.

### Pasos interrumpidos

Si se pierde el servidor que ejecuta un paso a mitad de la ejecución, PlaidCloud vuelve a ejecutar el paso automáticamente cuando es seguro repetirlo: un paso que reemplaza su salida termina con el mismo resultado que una sola ejecución limpia, por lo que no tiene nada que comprobar.

Un paso que no se puede repetir de forma segura no se vuelve a ejecutar. Falla una vez con un mensaje de **interrumpido**, porque ejecutarlo una segunda vez podría duplicar lo que el primer intento ya escribió. Los pasos que escriben salidas con `{date}` en el nombre o la ruta se consideran no seguros para repetir, ya que una nueva ejecución podría caer en una fecha distinta. Para recuperarse, revise en el destino del paso lo que escribió el primer intento, límpielo si es necesario y luego [vuelva a ejecutar el paso](/es/guides/workflows/running-one-step-in-a-workflow/) o **reanude** la ejecución.

### Pasos que nunca comienzan

Si ningún trabajador toma el trabajo de un paso de importación o de dimensión en unos 40 minutos, el paso falla en lugar de mostrar **En ejecución** hasta el tiempo de espera de 24 horas. Si un trabajador inició el trabajo y luego desapareció, el paso también falla, con un mensaje que indica que el trabajador se detuvo. Ambos mensajes dicen "Use Run from here to retry."

## Pausar, detener y reanudar

Mientras se ejecuta un flujo de trabajo, puede **pausarlo**, de modo que los pasos en curso terminen y los nuevos pasos esperen, o **detenerlo**, lo que cancela los pasos que estaban en cola y cualquier trabajo de importación o exportación que aún se esté ejecutando. Los pasos de importación y de dimensión que seguían en cola se cancelan limpiamente, de modo que no retrasan las importaciones ni las cargas de dimensiones posteriores en el espacio de trabajo.

**Reanudar** retoma una ejecución pausada, detenida o fallida desde donde se quedó en lugar de empezar de nuevo. Está disponible siempre que la última ejecución de un flujo de trabajo terminó en estado pausado, detenido o de error.

Lo que significa "desde donde se quedó" depende de cómo se ejecute el flujo de trabajo:

| Ejecución | Al reanudar |
|---|---|
| Serie | Reinicia en el paso que se estaba ejecutando cuando terminó la ejecución y continúa desde allí. Si ese paso está dentro de un grupo, Reanudar retoma todo el grupo de nivel superior que lo contiene: los pasos del grupo que ya terminaron correctamente se dejan como están, los demás se ejecutan, y la ejecución continúa después del grupo. |
| Paralela | Vuelve a ejecutar cada paso que no había terminado correctamente y deja los pasos completados como están. |
| Avanzada (grafo) | Vuelve a ejecutar el nodo que falló y todo lo que sigue esperándolo, y deja los nodos completados como están. |

Los pasos que llaman a otro flujo de trabajo (**Run Model**, **Conditional Run Model** y **Loop Model**) reanudan el flujo de trabajo al que llaman en lugar de reiniciarlo, a través de tantos niveles de anidamiento como tenga. Un paso de bucle reanuda la iteración que se interrumpió y omite las iteraciones que ya se completaron.

Cuando reanuda un flujo de trabajo que se ejecutó como **hijo anidado** de otro (uno que invocó un paso **Run Model** de un flujo principal), PlaidCloud ofrece **Reanudar desde el inicio de la cadena**. Reanudar el hijo por sí solo no puede continuar la orquestación del flujo principal, por lo que esta opción reanuda el flujo principal de nivel superior (la raíz de la cadena) y continúa toda la cadena desde donde se detuvo. Reanudar un flujo de trabajo de nivel superior no cambia. El inicio de la cadena se resuelve dentro del mismo proyecto: una cadena que cruza a otro proyecto se reanuda desde el inicio de la parte que está dentro del proyecto.

Reanudar siempre continúa la ejecución **original**. Vuelve a ejecutar cada paso de esa ejecución que no terminó correctamente (un paso que falló o que se abandonó se vuelve a ejecutar, no se trata como completado), y volver a ejecutar un paso individual por su cuenta mientras tanto no cambia lo que Reanudar retoma a continuación.

Una ejecución reanudada se registra como una **nueva ejecución** en el historial de ejecuciones del flujo de trabajo, que contiene solo los pasos que volvió a ejecutar. La ejecución original conserva su propia entrada en el historial.

:::note
Un paso de bucle hace coincidir sus iteraciones completadas por los valores de sus variables. Si los datos sobre los que itera el bucle cambiaron entre la ejecución original y la reanudación, las iteraciones con las que ya no puede hacer coincidirlos se vuelven a ejecutar en lugar de omitirse.
:::
