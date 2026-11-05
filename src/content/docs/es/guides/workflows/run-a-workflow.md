---
title: Ejecutar un flujo de trabajo
description: Ejecute un flujo de trabajo de PlaidCloud de forma manual o a demanda, siga el estado de cada paso y pause, detenga o reanude una ejecución desde donde se quedó.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/run-a-workflow.md
---

Puede iniciar una ejecución completa de un flujo de trabajo haciendo clic en el icono de ejecución de la jerarquía **Flujos de trabajo** o seleccionando **Run All** en el menú **Acciones** de un flujo de trabajo específico.



También puede hacer clic en el botón **Toggle Start/Stop** en la parte superior de la tabla de flujos de trabajo. Este botón de alternancia detiene un flujo de trabajo en ejecución o inicia un flujo de trabajo.

Si hace clic en **Ejecutar** en un flujo de trabajo que ya se está ejecutando, PlaidCloud se lo indica en lugar de iniciar una segunda ejecución.

## Elegir un modo de contabilización

Cada ejecución lleva un modo de contabilización en ERP. Para elegir uno en PlaidCloud, use **Ejecutar con modo de contabilización** en el menú contextual de un flujo de trabajo, o el botón de modo de ejecución del lienzo del flujo de trabajo; **Iniciar flujo de trabajo** o **Ejecutar flujo de trabajo** a secas solicitan el modo Live, sujeto aun así al límite del proyecto que se describe más adelante. También puede elegir el modo al iniciar una ejecución mediante la API de ejecución o el asistente.

| Modo | Qué sucede |
|---|---|
| Live | Los pasos de contabilización contabilizan exactamente como siempre. Es el modo predeterminado. |
| Simulate | Cada paso de contabilización en ERP genera y valida exactamente lo que contabilizaría, pero no confirma nada y nunca se comunica con el ERP. Los asientos que se contabilizarían se registran en el [historial de contabilización en ERP](/es/guides/connections/erp-post-history/), marcados como simulados, para que pueda revisarlos antes de ejecutar en modo Live. |
| Off | Los pasos de contabilización se omiten por completo. |

Un proyecto también tiene su propio límite de modo de contabilización, que cualquier miembro con acceso de escritura a un proyecto desbloqueado establece mediante la API del proyecto o el asistente. El límite solo hace que una ejecución sea más segura, nunca más permisiva: el modo efectivo de una ejecución es el más restrictivo entre el modo que usted eligió y el límite del proyecto, de modo que un proyecto limitado a Simulate sigue simulado aunque inicie la ejecución en modo Live.

Un [evento programado](/es/administration/scheduled-events/event-scheduler/#modo-de-contabilización-en-erp) conserva su propio modo de contabilización, por lo que una programación establecida en Simulate se ejecuta simulada cada vez que se activa.

El modo se propaga a todo lo que toca la ejecución. Un subflujo de trabajo, una macro y un paso **Run Model**, **Conditional Run Model** o **Loop Model** heredan el modo de la ejecución principal, igual que una ejecución que [reanude](#pausar-detener-y-reanudar) después de una detención: una ejecución simulada no puede contabilizar de verdad en ningún punto de su interior.

:::caution
Los pasos de contabilización de SAP, de adjuntos de SAP y de RFC genéricos de SAP no admiten simulación. En los modos Simulate y Off se omiten por completo, porque las propias marcas de prueba de SAP siguen abriendo una conexión real con SAP; omitir el paso es la única forma de que una ejecución simulada nunca llegue a SAP.
:::

:::note
Cada paso individual de contabilización en ERP también tiene su propia opción Validate Only (con la etiqueta Vista previa o Test Only Mode en algunos pasos), independiente del modo de contabilización de la ejecución descrito arriba. El editor de pasos siempre la guarda de forma explícita. Una configuración de paso escrita de otra manera (la API REST, MCP o una importación de paquete de flujo de trabajo) que omita por completo esta opción ahora también adopta de forma predeterminada una vista previa en lugar de una contabilización real.
:::

## Autorizar al proyecto para contabilizar

Una ejecución de flujo de trabajo contabiliza en un ERP como el proyecto, no como la persona que la inició. Antes de que una ejecución pueda contabilizar, el proyecto necesita una autorización para cada conexión y entorno de ERP que usen sus pasos de contabilización. Sin ella, el paso falla con el mensaje "This project isn't authorized to post to connection …", que indica la conexión y el entorno. Los pasos **Call SAP Financial Document Attachment**, **Call SAP Master Data Table RFC** y **Call SAP RFC** no la necesitan.

Para autorizar un proyecto, abra su página de inicio y seleccione **Autorizaciones de escritura en ERP** en **Contabilización en ERP**. Cada fila es una conexión en un entorno. Marque **Autorizado** para permitir que el proyecto contabilice allí, o desmárquelo para impedirlo. **Autorizado por** y **Autorizado el** muestran quién autorizó por última vez y cuándo.

- El botón se muestra a los Arquitectos del proyecto y a los administradores del espacio de trabajo, pero solo un Arquitecto puede cambiar una autorización, y solo mientras el proyecto esté desbloqueado. Un administrador del espacio de trabajo que no sea Arquitecto puede agregarse primero como Arquitecto.
- Al seleccionar una fila para autorizar o desautorizar, la lista no se vuelve a cargar: la posición de desplazamiento y el orden de columnas que haya elegido se mantienen. La ventana se puede cambiar de tamaño, y la nota sobre los proyectos públicos se ajusta para mostrarse completa.
- Para autorizar una conexión, también necesita acceso de escritura a ella: es de su propiedad, o se comparte con usted por nombre o mediante uno de sus grupos de seguridad. Una conexión establecida en **Todos los miembros del espacio de trabajo** no cuenta.
- Un proyecto establecido en **Todos los miembros del espacio de trabajo** se autoriza como cualquier otro. Todos los miembros son Arquitectos de él, por lo que cualquier miembro con acceso de escritura a una conexión puede autorizar el proyecto para ella. Una vez autorizado, cualquier miembro puede contabilizar en esa conexión desde los flujos de trabajo del proyecto, y la ventana lo indica sobre la cuadrícula.
- Una copia nueva privada para usted, creada con datos de tablas o miembros de dimensión, conserva las autorizaciones del origen que usted mismo podría conceder, y llega en modo Simulate si el origen estaba en Live; consulte [Autorizaciones de escritura en ERP en la copia](/es/guides/projects/managing-projects/#autorizaciones-de-escritura-en-erp-en-la-copia). Cualquier otra copia, o un proyecto creado a partir de un archivo de proyecto, empieza sin autorizaciones. Autorícelo antes de que contabilice.

## Seguir el estado de un paso

Mientras se ejecuta un flujo de trabajo, cada paso muestra un icono de estado que indica en qué punto se encuentra, junto con el tiempo que lleva en ejecución. Pase el cursor sobre el icono para ver el mensaje correspondiente.

| Estado | Qué significa |
|---|---|
| Waiting | El paso está en cola y aún no ha comenzado. |
| Running | El paso está trabajando y su duración aumenta mientras tanto. |
| Completed | El paso terminó correctamente. |
| Warning | El paso terminó, pero señaló algo que vale la pena leer en el [registro del flujo de trabajo](/es/guides/workflows/viewing-workflow-log/). |
| Error | El paso falló. Consulte [Gestión de errores de pasos](/es/guides/workflows/managing-step-errors/). |
| Skipped | Se omitió el paso: está deshabilitado o no se cumplieron sus condiciones de ejecución. Consulte [Omitir pasos en un flujo de trabajo](/es/guides/workflows/skip-steps-in-a-workflow/). |
| Continued | El paso falló, pero está configurado para continuar en caso de error, así que el flujo de trabajo siguió adelante. Consulte [Continuar en caso de error](/es/guides/workflows/continue-on-error/). |
| Stopped | La ejecución se detuvo antes de que el paso pudiera terminar. |
| Abandoned | La ejecución del paso se interrumpió, por lo que nunca terminará. Reanude la ejecución o vuelva a ejecutar el flujo de trabajo. |

Una vista de flujo de trabajo abierta se actualiza sola a medida que avanza una ejecución, de modo que los estados que ve se mantienen al día sin recargar la página.

### Pasos abandonados

Un paso se marca como **abandonado** cuando lo que lo estaba ejecutando desapareció a mitad de la ejecución, con mayor frecuencia porque alguien presionó **Detener** o porque el mantenimiento de la plataforma interrumpió la ejecución. La duración del paso deja de aumentar y la información sobre herramientas del estado explica lo que sucedió.

Un paso abandonado no se completó y no produjo ningún resultado. No es un paso lento, ni un problema con sus datos o su configuración.

Para retomar el trabajo, [**Reanude**](#pausar-detener-y-reanudar) la ejecución, con lo que el paso abandonado se ejecuta de nuevo, o vuelva a ejecutar todo el flujo de trabajo. Ambas opciones son seguras.

### Pasos interrumpidos

Si se pierde el servidor que ejecuta un paso a mitad de la ejecución, PlaidCloud vuelve a ejecutar el paso automáticamente cuando es seguro repetirlo: un paso que reemplaza su resultado termina con el mismo resultado que una sola ejecución limpia, por lo que no tiene nada que comprobar.

Un paso que no se puede repetir de forma segura no se vuelve a ejecutar. Falla una sola vez con un mensaje de **interrumpido**, porque ejecutarlo por segunda vez podría duplicar lo que el primer intento ya escribió. Los pasos que escriben resultados con `{date}` en el nombre o la ruta se consideran no seguros de repetir, ya que una nueva ejecución podría caer en una fecha distinta. Para recuperarse, revise en el destino del paso lo que escribió el primer intento, límpielo si es necesario y luego [vuelva a ejecutar el paso](/es/guides/workflows/running-one-step-in-a-workflow/) o **Reanude** la ejecución.

### Pasos que nunca se inician

Mientras un paso espera a un trabajador, su mensaje de estado dice "Waiting for a worker… N min. No import worker has picked this step up yet." (el tipo de trabajador corresponde al paso, como importación o exportación). El mensaje desaparece cuando comienza el trabajo.

Si el trabajo de un paso no puede iniciarse nunca, el paso falla con el motivo en lugar de esperar indefinidamente:

| Causa | Falla después de aproximadamente |
|---|---|
| Ningún trabajador recoge el trabajo de un paso de importación o de dimensión | 40 minutos |
| El pod del paso se queda atascado en Pending | 20 minutos |
| No se puede descargar la imagen del paso | 5 minutos |
| No se crea ningún pod para el paso | 20 minutos |
| Ningún ejecutor recoge una sincronización de conector (Singer) | 30 minutos |

El mensaje de la sincronización del conector nombra la sincronización. Si un trabajador inició el trabajo y luego desapareció, el paso también falla, con un mensaje que indica que el trabajador se detuvo. Los mensajes de importación y de dimensión dicen "Use Run from here to retry."

## Pausar, detener y reanudar

Mientras un flujo de trabajo se está ejecutando, puede **Pausar**lo, de modo que los pasos en curso terminen y los nuevos esperen, o **Detener**lo, lo que cancela los pasos que estaban en cola y cualquier trabajo de importación o exportación que siga en ejecución. Los pasos de importación y de dimensión que seguían en cola se cancelan limpiamente, para que no retengan las importaciones y cargas de dimensiones posteriores del espacio de trabajo. Detener también detiene las sincronizaciones de conector (Singer) en cola o en ejecución del flujo de trabajo, para que una sincronización no siga ejecutándose después de que el flujo de trabajo se haya detenido.

**Reanudar** retoma una ejecución pausada, detenida o fallida desde donde se quedó, en lugar de empezar de nuevo. Está disponible siempre que la última ejecución de un flujo de trabajo haya terminado en estado pausado, detenido o de error.

Lo que significa "desde donde se quedó" depende de cómo se ejecuta el flujo de trabajo:

| Ejecución | Al reanudar |
|---|---|
| Serie | Se reinicia en el paso que se estaba ejecutando cuando terminó la ejecución y continúa desde allí. Si ese paso está dentro de un grupo, Reanudar retoma todo el grupo de nivel superior que lo contiene: los pasos del grupo que ya terminaron correctamente se dejan como están, los demás se ejecutan y la ejecución continúa después del grupo. |
| Paralela | Vuelve a ejecutar cada paso que no había terminado correctamente y deja intactos los pasos completados. |
| Avanzada (grafo) | Vuelve a ejecutar el nodo que falló y todo lo que sigue esperándolo, y deja intactos los nodos completados. |

Los pasos que llaman a otro flujo de trabajo (**Run Model**, **Conditional Run Model** y **Loop Model**) reanudan el flujo de trabajo al que llaman en lugar de reiniciarlo, sin importar cuántos niveles de anidamiento tenga. Un paso de bucle reanuda la iteración que se interrumpió y omite las iteraciones que ya se completaron.

Cuando usted reanuda un flujo de trabajo que se ejecutó como **hijo anidado** de otro (uno invocado por un paso **Run Model** de un flujo principal), PlaidCloud ofrece **Reanudar desde el inicio de la cadena**. Reanudar el hijo por sí solo no puede continuar la orquestación del principal, así que esta opción reanuda el flujo principal de nivel superior (la raíz de la cadena) y continúa toda la cadena desde donde se detuvo. Reanudar un flujo de trabajo de nivel superior no cambia. El inicio de la cadena se resuelve dentro del mismo proyecto: una cadena que cruza a otro proyecto se reanuda desde el inicio de la parte que está dentro del proyecto.

Reanudar siempre continúa la ejecución **original**. Vuelve a ejecutar cada paso de esa ejecución que no terminó correctamente (un paso que falló o fue abandonado se vuelve a ejecutar, no se trata como completado), y volver a ejecutar un paso individual por separado mientras tanto no cambia lo que Reanudar retomará a continuación.

Una ejecución reanudada se registra como una **ejecución nueva** en el historial de ejecuciones del flujo de trabajo, que contiene solo los pasos que volvió a ejecutar. La ejecución original conserva su propia entrada en el historial.

:::note
Un paso de bucle hace coincidir sus iteraciones completadas por los valores de sus variables. Si los datos sobre los que itera el bucle cambiaron entre la ejecución original y la reanudación, las iteraciones que ya no puede hacer coincidir se vuelven a ejecutar en lugar de omitirse.
:::
