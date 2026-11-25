---
title: Get Workspace Usage (paso)
description: Escriba el uso del espacio de trabajo en una tabla del proyecto como actividad, miembros, contenido o tendencias, para informar de la adopción o alimentar un paso posterior.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descripción

Escribe en una tabla del proyecto cómo se usa su espacio de trabajo. Utilícelo para seguir la adopción a lo largo del tiempo, para informar el uso por departamento o equipo, para crear sus propios paneles de control o para detectar una caída de la actividad en un flujo de trabajo programado. Las cifras proceden de los mismos datos de uso que [Informes de uso](/es/administration/access/usage-reports/), y todos los conjuntos de datos abarcan todas las áreas.

**Actividad** y **Miembros** contienen la identidad del miembro (ID de usuario, nombre de usuario, correo electrónico, nombre, apellido y grupos de seguridad). La tabla de destino es una tabla de proyecto normal, por lo que cualquier persona con acceso al proyecto puede leerla: trátela como trataría cualquier lista de miembros. Cada ejecución que escribe la tabla se registra en el Registro de seguridad.

## Configuración

### Datos de uso

**Conjunto de datos** elige lo que contiene cada fila. El texto que aparece debajo describe las filas y nombra las columnas principales del que elija.

| Conjunto de datos | Valor | Una fila por | Contiene identidad |
|---|---|---|---|
| **Actividad** (predeterminado) | `activity` | Día, miembro, acción y elemento | Sí |
| **Miembros** | `members` | Miembro, incluidos los miembros sin actividad | Sí |
| **Contenido** | `content` | Panel de control, aplicación y notebook, incluidos los paneles de control y las aplicaciones que nadie usó | No |
| **Tendencias** | `trends` | Día, semana y mes del intervalo | No |

Los valores son los que contiene un paso cuando lo crea o edita mediante la API o un asistente de IA. Un paso guardado con un conjunto de datos que no figura en esta lista falla al ejecutarse y nombra los cuatro conjuntos de datos: ábralo, elija un **Conjunto de datos** y guárdelo. Un paso guardado antes con **Miembros** o **Contenido** sigue ejecutándose y escribe las columnas siguientes, y un paso que estaba limitado a un área ahora abarca todas las áreas. En **Contenido**, `subject` es ahora `item_id` y `type` contiene `Dashboard`, `App` o `Notebook`.

### Columnas

Las fechas y los días se escriben como marcas de tiempo a medianoche UTC.

#### Columnas de miembros

**Actividad** y **Miembros** incluyen estas columnas:

| Columna | Contiene |
|---|---|
| `user_id` | El ID del miembro. |
| `user_name` | El nombre de usuario del miembro. |
| `email` | La dirección de correo electrónico del miembro, en minúsculas. |
| `first_name` | Nombre. |
| `last_name` | Apellido. |
| `is_active` | Verdadero cuando el miembro está activo, falso cuando está desactivado. |
| `groups` | Los grupos de seguridad del miembro, separados por `; `. |

`groups` enumera los grupos de nivel superior a los que el miembro pertenece directamente.

#### Actividad

| Columna | Contiene |
|---|---|
| `day` | El día. |
| Las columnas de miembros | Como arriba. |
| `member` | El nombre y el apellido del miembro, o su nombre de usuario cuando no tiene ninguno de los dos. |
| `area` | `PlaidCloud app`, `Dashboards`, `Apps` o `Notebooks`. |
| `action` | `Opened app`, `Opened screen`, `Opened step`, `Saved step`, `Used palette action`, `Viewed dashboard`, `Used chart`, `Opened notebook` o `Saved notebook`. |
| `item_type` | `App area`, `Screen`, `Step`, `Palette action`, `Dashboard`, `Chart`, `App` o `Notebook`. |
| `item_id` | El ID del elemento. Para un notebook, su ruta. |
| `item_name` | El nombre del elemento: una pantalla o área de la aplicación en palabras, como `Members List`; el tipo de paso; el nombre del panel de control, del gráfico o de la aplicación; o la ruta del notebook. Cuando no se encuentra un nombre, el ID del elemento. |
| `events` | Cuántas veces lo hizo el miembro ese día. |
| `source` | La clave del área, tal como la nombran las exportaciones de [Informes de uso](/es/administration/access/usage-reports/). |
| `event` | La clave de la acción, tal como la nombran las exportaciones. |

`member` y las columnas de miembros dependen de quién lo hizo:

- La actividad que no se puede vincular a ningún miembro tiene `Unattributed` en `member` y las columnas de miembros en blanco.
- Un miembro eliminado desde entonces conserva solo `user_id`, y `member` es `Deleted user`.
- Cualquier otra cuenta, como una cuenta de servicio o un agente, conserva solo `user_id`, y `member` es su nombre de usuario.

`Used chart` cuenta una vez por miembro y gráfico en cada ventana de 5 minutos, por lo que mide el uso, no las consultas.

#### Miembros

| Columna | Contiene |
|---|---|
| Las columnas de miembros | Como arriba. |
| `member` | El nombre y el apellido del miembro, o su nombre de usuario cuando no tiene ninguno de los dos. |
| `created` | El día en que el miembro se agregó al espacio de trabajo, cuando se conoce. |
| `status` | `Active` cuando el miembro estuvo activo en el intervalo, `Dormant` cuando usó PlaidCloud antes pero no en el intervalo, `Never active` cuando no hay ningún uso registrado hasta el final del intervalo. |
| `first_seen` | El primer día registrado en que el miembro usó PlaidCloud, sea cual sea el intervalo. |
| `last_seen` | El último día de actividad del miembro en el intervalo. |
| `active_days` | Días con actividad en el intervalo. |
| `events` | Eventos de actividad en el intervalo. |
| `active_minutes` | Minutos de actividad en el intervalo. |
| `session_minutes` | Minutos en sesiones en el intervalo. |
| `app_open_minutes` | Minutos que el miembro tuvo abiertas aplicaciones de Panel en el intervalo. Las vistas previas de Studio no se cuentan. |

Todos los miembros tienen una fila, incluidos los miembros desactivados, excepto aquellos cuyo uso se borró. Las cuentas de servicio y los agentes no aparecen en la lista. Un miembro sin actividad en el intervalo no tiene `last_seen`, y sus otras columnas de actividad están en blanco.

#### Contenido

| Columna | Contiene |
|---|---|
| `type` | `Dashboard`, `App` o `Notebook`. |
| `item_id` | El ID del panel de control o de la aplicación, o la ruta del notebook. |
| `name` | El nombre del panel de control o de la aplicación, o la ruta del notebook. En blanco cuando el elemento se ha eliminado o no se pueden leer los nombres. |
| `deleted` | Verdadero cuando el panel de control o la aplicación se ha eliminado desde entonces. |
| `unused` | Verdadero para un panel de control o una aplicación que nadie usó en el intervalo. |
| `users` | Miembros que lo usaron en el intervalo. |
| `opens` | Veces que se abrió en el intervalo, incluidas las aperturas que no se pueden vincular a ningún miembro. |
| `last_used` | El último día en que se usó en el intervalo. Para un elemento sin usar, el último día en que se abrió antes del final del intervalo, o en blanco. |
| `app_open_minutes` | Minutos que una aplicación de Panel estuvo abierta en el intervalo. En blanco para los paneles de control, los notebooks y las aplicaciones Dash y WASM. |

Cada ruta de notebook tiene su propia fila. Las filas enumeran primero lo que se usó, con más usuarios primero, y después los paneles de control y las aplicaciones que nadie usó. Son los paneles de control publicados y las aplicaciones que ya existían cuando comenzó el intervalo. Solo se enumeran cuando el intervalo comienza dentro de los datos diarios que se conservan, ya se estaba recopilando el uso de ese tipo de elemento y se pueden leer los nombres. Las vistas previas de Studio de las aplicaciones se omiten.

#### Tendencias

| Columna | Contiene |
|---|---|
| `period` | `Day`, `Week` o `Month`. |
| `period_start` | El primer día del período. Las semanas comienzan el lunes. |
| `active_members` | Miembros activos en el período, dentro del intervalo. |
| `events` | Eventos de actividad en el período. |
| `active_minutes` | Minutos de actividad en el período. |
| `session_minutes` | Minutos en sesiones en el período. |
| `active_members_7d` | En una fila `Day`, miembros activos en los 7 días que terminan ese día. |
| `active_members_28d` | En una fila `Day`, miembros activos en los 28 días que terminan ese día. |
| `stickiness` | En una fila `Day`, `active_members` dividido por `active_members_28d`. |
| `complete` | Falso para hoy, para una semana o un mes que contiene hoy y para una semana o un mes que el intervalo corta. |

Todos los días del intervalo, desde donde empiezan los datos diarios que se conservan, tienen una fila, incluso sin uso, y también todas las semanas y todos los meses en que caen esos días. `active_members_7d`, `active_members_28d` y `stickiness` están en blanco en las filas `Week` y `Month`, y en una fila `Day` cuyos 7 o 28 días llegan a antes de los datos diarios que se conservan. `stickiness` también está en blanco cuando `active_members_28d` es 0. Un mes que empieza antes de los datos diarios que se conservan y que queda totalmente dentro del intervalo procede de los resúmenes mensuales: tiene `active_members`, pero eventos y minutos en blanco, y `complete` indica si el resumen cubría todo el mes.

### Ejemplo: minutos activos por departamento

**Actividad** y **Miembros** incluyen el `email` del miembro, en minúsculas, de modo que puede combinarlos con una tabla propia, como una tabla maestra de RR. HH. o de la organización, e informar por departamento.

1. Agregue un paso **Get Workspace Usage** con **Conjunto de datos** establecido en **Miembros** y una tabla de destino como `usage_members`.
2. Agregue un paso **Tabla: combinación interna** que combine `usage_members` con su tabla de la organización donde coincidan las columnas `email` en minúsculas. Conserve el departamento de su tabla y las columnas `active_minutes` y `events` de `usage_members`.
3. En el mismo paso, agregue por departamento y sume `active_minutes`.

El resultado son los minutos activos por departamento. Los miembros que no están en su tabla de la organización se descartan en una combinación interna, así que use una combinación izquierda si desea verlos. Repita con un segundo paso sobre **Actividad** y sume `events` por departamento y `item_name` para informar quién usa qué paneles de control y aplicaciones.

### Intervalo de fechas

**Rango** elige los días que se leen:

| Rango | Valor | Lee |
|---|---|---|
| **Últimos N días** (predeterminado 30) | `last_days` | Los días más recientes, incluido hoy. |
| **Mes anterior** | `previous_month` | El último mes natural completo. |
| **Mes en curso** | `month_to_date` | Desde el primer día de este mes hasta hoy. |
| **Entre fechas** | `dates` | Desde **Fecha de inicio** hasta **Fecha de fin**. Deje **Fecha de fin** vacía para leer hasta hoy. |

Los días y las fechas son UTC. **Días** admite un número entero. **Fecha de inicio** y **Fecha de fin** admiten una fecha `YYYY-MM-DD` o una [variable](/es/guides/workflows/manage-workflow-variables/) como `{report_start}`. El inicio no debe ser posterior al fin.

Los datos diarios se conservan durante 180 días y los resúmenes mensuales durante 25 meses.

### Destino del uso

**Tabla de destino** recibe el resultado. El paso reemplaza lo que contuviera la tabla y siempre escribe las columnas del conjunto de datos, incluso cuando no hay filas.

## Advertencias

Estas no hacen que el paso falle. Este termina con la advertencia y aun así reemplaza la tabla, con las columnas del conjunto de datos:

| Advertencia | Significado |
|---|---|
| "Usage data is not available yet: the usage database has not been set up on this workspace." | La recopilación de uso aún no está configurada para el espacio de trabajo. |
| "Usage data is not available right now: the usage database could not be reached." | No se pudieron leer los datos de uso. Ejecute el paso de nuevo más tarde. |
| "No usage from *start* to *end*." | No hubo uso en el intervalo. |
| "Usage before *date* isn't kept, so the range was clipped to start there." | El intervalo comienza antes de los datos diarios que se conservan, por lo que la actividad se cuenta desde *date*. **Tendencias** sigue incluyendo los meses completos anteriores a partir de los resúmenes mensuales. |
| "This took too long to compute: narrow the date range." | La lectura agotó el tiempo, por lo que la tabla no tiene filas. Elija un intervalo más corto. |
| "Some names are unavailable right now, so those items are named by their id." | Solo **Actividad**. No se pudieron leer algunos nombres de paneles de control, gráficos o aplicaciones, por lo que `item_name` contiene el ID. |
| "Members could not be read right now, so they are named by their id." | Solo **Actividad**. No se pudo leer la lista de miembros, por lo que `member` contiene el ID del miembro y, de las columnas de miembros, solo se rellena `user_id`. |
| "Names are unavailable right now, so items nobody used are not listed." | Solo **Contenido**. No se pudieron leer los nombres de paneles de control o aplicaciones, por lo que solo se enumeran los elementos usados. |
| "Activity before *date* isn't kept, so items nobody used in this range can't be listed." | Solo **Contenido**. El intervalo comienza antes de los datos diarios que se conservan, por lo que solo se enumeran los elementos usados. |

Cuando no se puede leer la lista de miembros, **Miembros** falla en su lugar y deja la tabla de destino como estaba.

## Registro de seguridad

Cada ejecución que escribe la tabla añade una entrada al Registro de seguridad que registra el conjunto de datos, el intervalo, la tabla de destino y su proyecto, el flujo de trabajo, el paso y la ejecución, el número de filas escritas y, para **Actividad** y **Miembros**, que las filas contienen la identidad de los miembros.

## Relacionado

- [Pasos generales](/es/reference/workflow-steps/general/)
- [Informes de uso](/es/administration/access/usage-reports/)
- [Get Workspace Members](/es/reference/workflow-steps/general/get-workspace-members/)
