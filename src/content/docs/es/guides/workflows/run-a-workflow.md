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
| Simulate | Cada paso de contabilización en ERP genera y valida exactamente lo que contabilizaría, pero no confirma nada y nunca se comunica con el ERP. Los asientos que se contabilizarían se registran para que pueda revisarlos antes de ejecutar en modo Live: los de un paso **Contabilizar documentos**, en el [Registro de asientos](/es/guides/connections/posting-register/) como **Se contabilizaría** (consulte [Contabilizar documentos en sistemas ERP](/es/guides/connections/post-documents/)), y los del propio paso de contabilización de un sistema, en el [historial de contabilización en ERP](/es/guides/connections/erp-post-history/), marcados como simulados. |
| Off | Los pasos de contabilización se omiten por completo. |

Un proyecto también tiene su propio límite de modo de contabilización, que cualquier miembro con acceso de escritura a un proyecto desbloqueado establece mediante la API del proyecto o el asistente. El límite solo hace que una ejecución sea más segura, nunca más permisiva: el modo efectivo de una ejecución es el más restrictivo entre el modo que usted eligió y el límite del proyecto, de modo que un proyecto limitado a Simulate sigue simulado aunque inicie la ejecución en modo Live.

Un [evento programado](/es/administration/scheduled-events/event-scheduler/#modo-de-contabilización-en-erp) conserva su propio modo de contabilización, por lo que una programación establecida en Simulate se ejecuta simulada cada vez que se activa.

El modo se propaga a todo lo que toca la ejecución. Un subflujo de trabajo, una macro y un paso **Run Model**, **Conditional Run Model** o **Loop Model** heredan el modo de la ejecución principal, igual que una ejecución que [reanude](#pausar-detener-y-reanudar) después de una detención: una ejecución simulada no puede contabilizar de verdad en ningún punto de su interior.

:::caution
Los pasos de contabilización de SAP, de adjuntos de SAP y de RFC genéricos de SAP no admiten simulación. En los modos Simulate y Off se omiten por completo, porque las propias marcas de prueba de SAP siguen abriendo una conexión real con SAP; omitir el paso es la única forma de que una ejecución simulada nunca llegue a SAP.
:::

:::note
Cada paso individual de contabilización en ERP también tiene su propia opción Validate Only (con la etiqueta Vista previa o Test Only Mode en algunos pasos), independiente del modo de contabilización de la ejecución descrito arriba. El editor de pasos siempre la guarda de forma explícita. Una configuración de paso escrita de otra manera (la API REST, MCP o una importación de paquete de flujo de trabajo) que omita por completo esta opción ahora también adopta de forma predeterminada una vista previa en lugar de una contabilización real. El paso **Contabilizar documentos** no tiene esa opción: el modo de la ejecución y el modo propio de su sistema deciden si contabiliza; consulte [Contabilizar documentos en sistemas ERP](/es/guides/connections/post-documents/).
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

Si se pierde el servidor que ejecuta un paso a mitad de la ejecución, PlaidCloud vuelve a ejecutar el paso automáticamente cuando es seguro repetirlo: un paso que reemplaza su resultado termina con el mismo resultado que una sola ejecución limpia, por lo que no tiene nada que comprobar. El registro del paso muestra una advertencia donde comienza el segundo intento: "Restarted: the server running this step stopped before it finished (e.g. out of memory or a restart); running it again from the start."

Un paso que no se puede repetir de forma segura no se vuelve a ejecutar. Falla una sola vez con un mensaje de **interrumpido**, porque ejecutarlo por segunda vez podría duplicar lo que el primer intento ya escribió. Los pasos que escriben resultados con `{date}` o `{date_iso}` en el nombre o la ruta se consideran no seguros de repetir, ya que una nueva ejecución podría caer en una fecha distinta. Para recuperarse, revise en el destino del paso lo que escribió el primer intento, límpielo si es necesario y luego [vuelva a ejecutar el paso](/es/guides/workflows/running-one-step-in-a-workflow/) o **Reanude** la ejecución.

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

### Ejecuciones que dejan de responder

Una ejecución nunca permanece **En ejecución** después de que el trabajo que la respalda haya desaparecido. Si se pierde el servidor que ejecuta el flujo de trabajo, la ejecución termina como fallida. Una ejecución puede durar como máximo 12 horas: si sigue en ejecución en ese momento, falla con "Run failed: still running at the 12-hour limit. Re-run the workflow."

## Run Insight

Run Insight muestra en qué empleó su tiempo una ejecución de un flujo de trabajo y qué pasos tardaron más o menos de lo habitual. Juzga cada paso frente a sus propias ejecuciones recientes, de modo que un paso que siempre es lento no se señala.

### Abrir Run Insight

- En el lienzo, haga clic en **Historial** en la barra de herramientas. Consulte [Diseñador visual de flujos de trabajo](/es/guides/workflows/advanced-workflows/).
- En la pestaña **Flujos de trabajo**, seleccione un flujo de trabajo y elija **Run Insight** en el menú **Acciones** o en el menú contextual.
- En Inicio, elija **Abrir la última ejecución** en una tarjeta de flujo de trabajo.
- En el cuadro de diálogo del historial de ejecuciones, elija una ejecución en la tabla **Ejecuciones** con **Abrir en Insight**, o abra su fila.
- En un mensaje de Weave dentro de la aplicación sobre una ejecución lenta, haga clic en **Abrir la ejecución**. Consulte [Aviso al terminar una ejecución](/es/guides/ai-assistant/weave-findings/#aviso-al-terminar-una-ejecución).

El cuadro de diálogo se titula **Historial de ejecuciones** — nombre del flujo de trabajo. Su selector **Insight** | **Ejecuciones** alterna entre esta vista y la tabla de ejecuciones anteriores. El historial de ejecuciones de un paso, que se abre desde el Inspector, muestra solo la tabla.

### Leer el titular y la lista de atención

El titular indica el resultado de la ejecución en una línea: **Tardó** *tiempo*, **En ejecución desde hace** *tiempo* mientras se ejecuta, **Detenido tras** *tiempo* en una última ejecución que se detuvo, o **Falló en** *flujo de trabajo*, el flujo de trabajo en el que falló. Una frase debajo indica qué destaca, como los pasos que fueron más lentos de lo habitual, el tiempo de espera, o que todos los pasos con historial se ejecutaron dentro de su intervalo habitual. Después aparecen la hora de inicio, el número de flujos de trabajo y pasos y, cuando algunos pasos tienen muy poco historial para juzgarse, cuántos. Cuando algo merece una revisión, aparece junto al titular *N* **por revisar**.

Junto al titular hay una franja de ejecuciones recientes, con un rótulo encima. Cada barra es una ejecución, tan alta como lo que tardó, y el día se indica solo donde cambia. Haga clic en una ejecución de la franja para abrirla. Una tapa roja y una ✕ marcan una ejecución fallida, y un contorno discontinuo marca una ejecución que ejecutó menos pasos que la mayoría de las ejecuciones recientes, porque no puede compararse con una ejecución completa.

**Qué requiere atención** lista, en este orden, primero los errores, después el tiempo más allá de lo habitual y por último las esperas. Cada elemento es una tarjeta con su nombre, el tiempo que perdió o **Error**, dónde se encuentra y una barra de su tiempo en la que el gris es lo habitual y el ámbar lo que lo supera, y la barra de un error es roja. Un paso guardado desde su última ejecución lleva una etiqueta **Guardado el** *fecha*. Haga clic en una tarjeta para seleccionarla en la vista; la tarjeta seleccionada aparece resaltada.

### Flujo, cronología y tabla

El encabezado situado sobre la vista contiene el nombre del flujo de trabajo, después **Comparar con**, después **Vista**, cuyos botones **Flujo**, **Cronología** y **Tabla** eligen la vista, y el botón Actualizar a la derecha.

| Vista | Qué muestra |
|---|---|
| **Flujo** | Bloques cuya altura es el tiempo. El ámbar es el tiempo más allá de lo habitual de un paso. Un bloque que no está abierto pero contiene un error muestra ✕ y un contorno rojo. Un bloque fallido o seleccionado demasiado corto para mostrar su nombre se dibuja más alto, y la leyenda indica que entonces no está a escala. Cuando un paso llamó a otros flujos de trabajo, un segmento **Sobrecarga de llamada** es el tiempo propio del paso fuera de esos flujos de trabajo. Cuando no se estaba ejecutando ningún paso, un segmento **En espera** muestra el hueco; un flujo de trabajo que se ejecutó en paralelo no lo dibuja. |
| **Cronología** | Hora de reloj desde el inicio de la ejecución. Un contorno discontinuo indica cuánto tardó el bloque en la ejecución comparada. |
| **Tabla** | Todo en orden de llamada, con las columnas **Nombre**, **Esta ejecución**, **Normalmente**, **Extra**, **Ejecución comparada** y **Estado**. |

Un flujo de trabajo que llamó a otros flujos de trabajo los muestra en su interior. Haga doble clic en un bloque de flujo de trabajo, o elija **Acercar**, para trabajar dentro de él, y use la ruta situada sobre la vista para volver. Cuando varios pasos al ritmo habitual están juntos, **Flujo** los pliega en un bloque *N* **al ritmo habitual**; haga clic en él, o haga clic en **Mostrar los** *número* **bloques** a la derecha de la ruta, para abrirlos; el número es la cantidad de bloques de la vista. **Plegar bloques al ritmo habitual** los vuelve a plegar, y el botón aparece solo cuando algo puede plegarse.

Seleccione un bloque para ver su panel de detalle. Muestra el nombre y el lugar del bloque, una etiqueta de estado con una de las marcas siguientes, y filas con lo que corresponda de **Esta ejecución**, **Normalmente**, **Historial**, **Más allá de lo habitual** y **Ejecución comparada**. Sigue una línea de tendencia: para el flujo de trabajo de la propia ejecución, sus ejecuciones completas recientes, con esta ejecución como un punto cuando se completó; para un paso con un intervalo habitual, ese intervalo como una banda con esta ejecución como un punto. Unas notas explican la marca, y los botones son **Mostrar en su flujo de trabajo**, **Mostrar sus pasos** o **Acercar**, **Abrir flujo de trabajo** y **Ver registro de ejecución**. **Abrir flujo de trabajo** abre el flujo de trabajo en el lienzo y **Ver registro de ejecución** abre su [registro](/es/guides/workflows/viewing-workflow-log/).

### Qué significan las marcas

| Marca | Significado |
|---|---|
| **Error** | Un paso terminó con un error. El panel muestra su mensaje, a menos que su rol no pueda ver el nombre del paso. |
| **Más lento de lo habitual** | El paso tardó más que su intervalo habitual. |
| **Más lento en todo momento** | Todos los pasos del flujo de trabajo fueron aproximadamente igual de lentos, lo que apunta a algo que comparte todo el flujo de trabajo y no a un solo paso. Sus pasos muestran **Parte de una lentitud compartida**. |
| **Tiene pasos lentos** | Un flujo de trabajo con **Pasos lentos internos**. |
| **Al ritmo habitual** | El paso se ejecutó dentro de su intervalo habitual. |
| **Más rápido** | El paso se ejecutó más rápido que su intervalo habitual. |
| **Historial insuficiente** | El paso no se ha ejecutado las veces suficientes para tener un intervalo habitual, por lo que no se juzga. |
| **Error, continuó** | El paso falló, pero está configurado para [continuar en caso de error](/es/guides/workflows/continue-on-error/). |
| **Omitido** | El paso se omitió. |
| **En ejecución** | El paso no ha terminado. |

Un paso cuyas ejecuciones recientes ya eran lentas o varían mucho puede no marcarse. Una ejecución de fin de periodo, comparada con días ordinarios, puede mostrarse más lenta en todo momento. Una ejecución detenida más antigua se muestra como una ejecución corta, no como detenida.

El panel también puede explicar una marca. **En espera** es el tiempo en que no se estaba ejecutando ningún paso, por lo que ningún paso tiene la culpa. En un paso que fue más lento de lo habitual, **Filas escritas** compara su salida con su recuento habitual, y se omite cuando la seguridad a nivel de fila filtra lo que usted puede leer, y **Guardado desde su última ejecución** indica que el paso se guardó después de su ejecución anterior y antes de que esta comenzara; el registro muestra un guardado, no lo que cambió. **Trabajo distinto** cuenta los pasos que no se ejecutaron y los pasos que se ejecutaron sin historial, medidos frente al historial de cada paso o, cuando compara con otra ejecución, frente a esa ejecución. **Ejecutado en paralelo** significa que las partes del flujo de trabajo se ejecutaron al mismo tiempo, por lo que sus tiempos suman más que el reloj. **Llamador no seguro** significa que el historial no puede mostrar qué paso llamó a un flujo de trabajo. **Nombre oculto** marca un paso o flujo de trabajo cuyo nombre su rol no puede ver, y se muestra como **Paso oculto** o **Flujo de trabajo oculto**.

### Comparar con

**Comparar con** establece frente a qué se mide una ejecución. Su botón de menú muestra la elección: **Habitual**, **Habitual + ejecución anterior** o **Habitual + ejecución del** seguido de la hora de inicio de la ejecución elegida. **Habitual** usa las ejecuciones recientes de cada paso. **Habitual + ejecución anterior** y **Habitual + una ejecución elegida** añaden además el tiempo de esa ejecución para cada paso, que la **Cronología** contornea y la **Tabla** muestra en **Ejecución comparada**. **Habitual + una ejecución elegida** abre una lista de las ejecuciones recientes para elegir una.

### Un flujo de trabajo dentro de una ejecución mayor

Cuando abre un flujo de trabajo al que llamó otro flujo de trabajo, Insight muestra solo la parte de la ejecución que corresponde a ese flujo de trabajo. **Abrir la ejecución completa** cambia el mismo cuadro de diálogo al flujo de trabajo que inició la ejecución.

### Ejecuciones en curso

Una ejecución que sigue en curso se vuelve a leer cada 30 segundos mientras el cuadro de diálogo esté visible. El zoom, la selección y la vista se mantienen. Al salir de Insight hacia **Ejecuciones**, las actualizaciones se detienen, y al volver a Insight se vuelve a leer la ejecución y se reanudan. El botón Actualizar, las flechas circulares a la derecha del encabezado, recarga la ejecución desde cero, restablece el zoom y la selección, y vuelve a plegar los bloques al ritmo habitual.

### Para asistentes de IA y la API REST

El mismo perfil está disponible fuera del cuadro de diálogo:

- REST: `GET /rest/v1/analyze/workflow/run-insight` con `project_id` y `workflow_id`. `run_id` elige la ejecución (la última si se omite), y `baseline` es `typical`, `previous` o `run:<id>`.
- MCP: `workflow_describe` con `include=['run_insight']`, y `run_id` y `baseline` opcionales.

Cada flujo de trabajo y cada paso se devuelve con su tiempo, su lugar en la ejecución, un veredicto frente a su propio historial y los motivos. Una ejecución que no existe, o que no tiene filas de pasos, no devuelve ningún perfil y sí una advertencia en lugar de un error.

## Pausar, detener y reanudar

Mientras un flujo de trabajo se está ejecutando, puede **Pausar**lo, de modo que los pasos en curso terminen y los nuevos esperen, o **Detener**lo, lo que cancela los pasos que estaban en cola y cualquier trabajo de importación o exportación que siga en ejecución, junto con la consulta del almacén de datos que estaba leyendo una exportación. Los pasos de importación y de dimensión que seguían en cola se cancelan limpiamente, para que no retengan las importaciones y cargas de dimensiones posteriores del espacio de trabajo. Detener también detiene las sincronizaciones de conector (Singer) en cola o en ejecución del flujo de trabajo, para que una sincronización no siga ejecutándose después de que el flujo de trabajo se haya detenido.

Una macro puede estar ejecutándose en varios lugares a la vez, llamada por otros flujos de trabajo o por un paso **Macro: ejecución simultánea**. Detener la macro detiene todas sus copias en ejecución. Detener una sola copia detiene solo esa copia y lo que esta inició, y deja en ejecución el flujo de trabajo que la llamó, al igual que un paso **Macro Concurrent** que abandona una copia que dejó de responder. Una macro que solo se está ejecutando dentro de otros flujos de trabajo aparece como **En ejecución** en la lista de flujos de trabajo, con **Detener** disponible, y al abrirla se muestra el estado, la hora de inicio y la hora de fin de cada paso según su última ejecución.

**Reanudar** retoma una ejecución pausada, detenida o fallida desde donde se quedó, en lugar de empezar de nuevo. Está disponible siempre que la última ejecución de un flujo de trabajo haya terminado en estado pausado, detenido o de error.

Lo que significa "desde donde se quedó" depende de cómo se ejecuta el flujo de trabajo:

| Ejecución | Al reanudar |
|---|---|
| Serie | Se reinicia en el paso que se estaba ejecutando cuando terminó la ejecución y continúa desde allí. Si ese paso está dentro de un grupo, Reanudar retoma todo el grupo de nivel superior que lo contiene: los pasos del grupo que ya terminaron correctamente se dejan como están, los demás se ejecutan y la ejecución continúa después del grupo. |
| Paralela | Vuelve a ejecutar cada paso que no había terminado correctamente y deja intactos los pasos completados. |
| Avanzada (grafo) | Vuelve a ejecutar el nodo que falló y todo lo que sigue esperándolo, y deja intactos los nodos completados. |

Los pasos que llaman a otro flujo de trabajo (**Run Model**, **Conditional Run Model** y **Loop Model**) reanudan el flujo de trabajo al que llaman en lugar de reiniciarlo, sin importar cuántos niveles de anidamiento tenga. Un paso de bucle reanuda la iteración que se interrumpió y omite las iteraciones que ya se completaron.

Cuando usted reanuda un flujo de trabajo que se ejecutó como **hijo anidado** de otro (uno invocado por un paso **Run Model** de un flujo principal), PlaidCloud ofrece **Reanudar desde el inicio de la cadena**. Reanudar el hijo por sí solo no puede continuar la orquestación del principal, así que esta opción reanuda el flujo principal de nivel superior (la raíz de la cadena) y continúa toda la cadena desde donde se detuvo. Reanudar un flujo de trabajo de nivel superior no cambia. El inicio de la cadena se resuelve dentro del mismo proyecto: una cadena que cruza a otro proyecto se reanuda desde el inicio de la parte que está dentro del proyecto.

Reanudar siempre continúa la ejecución **original**. Vuelve a ejecutar cada paso de esa ejecución que no terminó correctamente (un paso que falló o fue abandonado se vuelve a ejecutar, no se trata como completado), y volver a ejecutar un paso individual por separado mientras tanto no cambia lo que Reanudar retomará a continuación. Esto también se aplica a un flujo de trabajo hijo: si volvió a ejecutar uno de sus pasos por separado, reanudar el flujo principal sigue ejecutando todo lo que le quedaba al hijo, no solo ese paso.

Una ejecución reanudada se registra como una **ejecución nueva** en el historial de ejecuciones del flujo de trabajo, que contiene solo los pasos que volvió a ejecutar. La ejecución original conserva su propia entrada en el historial. Cuando una ejecución llama al mismo flujo de trabajo hijo más de una vez, cada llamada tiene su propia entrada en el historial de ejecuciones del hijo. Las iteraciones de un paso de bucle cuentan como una sola llamada.

:::note
Un paso de bucle hace coincidir sus iteraciones completadas por los valores de sus variables. Si los datos sobre los que itera el bucle cambiaron entre la ejecución original y la reanudación, las iteraciones que ya no puede hacer coincidir se vuelven a ejecutar en lugar de omitirse.
:::
