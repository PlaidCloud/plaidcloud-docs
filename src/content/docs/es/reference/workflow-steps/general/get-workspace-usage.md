---
title: Get Workspace Usage
description: Escriba en una tabla del proyecto los totales de uso del espacio de trabajo de los Informes de uso, por día o por mes, para graficar la adopción o alimentar un paso posterior.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descripción

Escribe en una tabla del proyecto cómo se usa su espacio de trabajo. Úselo para seguir la adopción a lo largo del tiempo, informar del uso por departamento o equipo, crear sus propios paneles de control o detectar una caída de la actividad en un flujo de trabajo programado. Las cifras son las mismas que muestran los [Informes de uso](/es/administration/access/usage-reports/).

Tres conjuntos de datos contienen únicamente totales: ninguna fila nombra a un miembro y las rutas de los cuadernos se sustituyen por `*`. Los otros cuatro (**Miembros**, **Diario por miembro**, **Contenido** y **Contenido por miembro**) están pensados para la elaboración de informes. **Miembros**, **Diario por miembro** y **Contenido por miembro** contienen la identidad del miembro (ID de usuario, nombre de usuario, correo electrónico, nombre y apellidos y grupos de seguridad), así que trate la tabla de destino como trataría cualquier lista de miembros. Cada ejecución del paso se registra en el Registro de seguridad.

## Configuración

### Datos de uso

**Conjunto de datos** elige lo que contiene cada fila:

| Conjunto de datos | Una fila por cada | Contiene identidad |
|---|---|---|
| **Diario por elemento** | Día, área, evento y asunto | No |
| **Mensual por elemento** | Mes, área, evento y asunto | No |
| **Totales mensuales** (predeterminado) | Mes y área | No |
| **Miembros** | Persona en el espacio de trabajo | Sí |
| **Diario por miembro** | Persona, día y área | Sí |
| **Contenido** | Panel de control, aplicación o cuaderno | No |
| **Contenido por miembro** | Persona y elemento | Sí |

**Área** limita las filas a un área: **Aplicación PlaidCloud**, **Paneles de control**, **Aplicaciones**, **Visitas a aplicaciones** o **Cuadernos**. Déjela en **Todas las áreas** para incluirlas todas.

### Columnas

#### Diario por elemento

`day`, `source`, `event`, `subject`, `events`.

#### Mensual por elemento

`month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial`.

#### Totales mensuales

`month`, `source`, `active_users`, `coverage_start`, `partial`.

`partial` es verdadero para un mes que el historial no cubre por completo, y `coverage_start` es la fecha en que comenzó la recopilación. Un mes se incluye cuando ha cerrado y se ha estabilizado, lo que tarda 3 días.

#### Columnas de miembro

**Miembros**, **Diario por miembro** y **Contenido por miembro** empiezan con las mismas siete columnas:

| Columna | Contiene |
|---|---|
| `user_id` | El ID del miembro. |
| `user_name` | El nombre de usuario del miembro. |
| `email` | La dirección de correo electrónico del miembro, en minúsculas. |
| `first_name` | Nombre. |
| `last_name` | Apellidos. |
| `is_active` | Verdadero cuando el miembro está activo, falso cuando está desactivado. |
| `groups` | Los grupos de seguridad del miembro, separados por `; `. |

`groups` enumera solo los grupos de nivel superior. Los subgrupos no se expanden.

#### Miembros

Las columnas de miembro y, después:

| Columna | Contiene |
|---|---|
| `first_seen` | El primer día en que el miembro usó PlaidCloud, sea cual sea el intervalo de fechas. |
| `last_seen` | El último día de actividad del miembro dentro del intervalo. |
| `active_days` | Días con actividad en el intervalo. |
| `events` | Eventos de actividad en el intervalo. |
| `active_minutes` | Minutos de actividad. Los minutos superpuestos entre áreas se cuentan una sola vez. |
| `session_minutes` | Minutos en sesiones. |
| `app_open_minutes` | Minutos que el miembro tuvo abiertas aplicaciones de Panel. |

Cada persona del espacio de trabajo tiene una fila. Un miembro sin actividad en el intervalo tiene valores en blanco después de `groups`. Los totales coinciden con los [Informes de uso](/es/administration/access/usage-reports/), salvo en el caso de los miembros eliminados desde entonces.

#### Diario por miembro

Las columnas de miembro y, después, `day`, `source` (el área), `events`, `active_minutes`, `session_minutes`, `first_at` y `last_at` (las horas de la primera y la última actividad de ese día).

#### Contenido

| Columna | Contiene |
|---|---|
| `type` | `dashboard`, `panel_app`, `wasm_app` o `notebook`. |
| `subject` | El ID del elemento. Todos los cuadernos comparten una fila, con `*` aquí. |
| `name` | El nombre del elemento, o `*` para los cuadernos. |
| `deleted` | Verdadero cuando el elemento se ha eliminado desde entonces. |
| `users` | Miembros que lo abrieron. |
| `opens` | Veces que se abrió. |
| `last_used` | Cuándo se usó por última vez. |
| `app_open_minutes` | Minutos que estuvieron abiertas las aplicaciones de Panel. |

#### Contenido por miembro

Las columnas de miembro y, después, `type`, `subject`, `name` (como en **Contenido**), `opens` (veces que este miembro abrió el elemento) y `last_day` (el último día de uso del miembro).

### Notas sobre los conjuntos de datos de miembros

- La actividad de agentes, cuentas de servicio y miembros eliminados desde entonces tiene en blanco las columnas de identidad. Un miembro eliminado conserva el `user_id` y nada más.
- Las aperturas de **Contenido** pueden superar la suma de las aperturas de **Contenido por miembro**. La diferencia son aperturas que no se pueden atribuir a un miembro, como las vistas incrustadas o de invitados de un panel de control. **Contenido** las cuenta y **Contenido por miembro** no puede.

### Ejemplo: minutos activos por departamento

**Miembros** y **Contenido por miembro** incluyen el `email` del miembro, en minúsculas, de modo que puede combinarlos con una tabla propia, como una tabla maestra de RR. HH. u organización, e informar por departamento.

1. Agregue un paso **Get Workspace Usage** con **Conjunto de datos** definido en **Miembros** y una tabla de destino como `usage_members`.
2. Agregue un paso **Tabla: combinación interna** que combine `usage_members` con su tabla de organización donde coincidan las columnas `email` en minúsculas. Conserve el departamento de su tabla y las columnas `active_minutes` y `events` de `usage_members`.
3. En el mismo paso, agregue por departamento y sume `active_minutes`.

El resultado son los minutos activos por departamento. Los miembros que no están en su tabla de organización desaparecen en una combinación interna, así que use una combinación izquierda si desea verlos. Repita con un segundo paso sobre **Contenido por miembro** y sume `opens` por departamento para informar de quién usa qué paneles de control y aplicaciones.

### Intervalo de fechas

**Intervalo** elige los días que se leen:

- **Último número de días** (predeterminado 30) lee los días más recientes, incluido hoy.
- **Mes anterior** lee el último mes natural completo.
- **Mes en curso** lee desde el primer día de este mes hasta hoy.
- **Entre fechas** lee desde **Fecha de inicio** hasta **Fecha de fin**. Deje **Fecha de fin** vacía para leer hasta hoy.

Los días y las fechas están en UTC. **Días**, **Fecha de inicio** y **Fecha de fin** aceptan una [variable](/es/guides/workflows/manage-workflow-variables/) como `{report_start}`, además de un número o una fecha `YYYY-MM-DD`. El inicio no debe ser posterior al fin.

### Destino del uso

**Tabla de destino** recibe el resultado. El paso reemplaza lo que contuviera la tabla y siempre escribe las columnas del conjunto de datos, incluso cuando no hay filas.

## Advertencias

Estas no hacen fallar el paso. Termina con una advertencia que indica lo ocurrido y aun así escribe la tabla:

- La recopilación de uso aún no está configurada para el espacio de trabajo.
- No hubo uso en el intervalo.
- El intervalo comienza antes de lo que se conserva, por lo que se recortó para empezar donde comienza el historial. Los datos diarios se conservan durante 180 días y los datos mensuales durante 25 meses.

## Registro de seguridad

Cada ejecución escribe una entrada en el Registro de seguridad que registra el conjunto de datos, el intervalo, la tabla de destino, el flujo de trabajo, el paso y la ejecución, y el número de filas escritas.

## Relacionado

- [Pasos generales](/es/reference/workflow-steps/general/)
- [Informes de uso](/es/administration/access/usage-reports/)
- [Get Workspace Members](/es/reference/workflow-steps/general/get-workspace-members/)
