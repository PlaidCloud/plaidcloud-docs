---
title: Get Workspace Usage
description: Escriba en una tabla de proyecto los totales de uso del espacio de trabajo de los Informes de uso, por día o por mes, para graficar la adopción o alimentar un paso posterior.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/get-workspace-usage.md
---

## Descripción

Escribe en una tabla de proyecto un resumen de cómo se usa su espacio de trabajo. Úselo para seguir la adopción a lo largo del tiempo, crear sus propios paneles de control sobre el uso o detectar una caída de actividad en un flujo de trabajo programado. Las cifras son las mismas que muestran los [Informes de uso](/es/administration/access/usage-reports/).

La salida contiene solo totales. Ninguna fila nombra a un miembro y las rutas de los notebooks se sustituyen por `*`. Se omiten los miembros cuyo uso se borró.

## Configuración

### Datos de uso

**Conjunto de datos** elige qué contiene cada fila:

| Conjunto de datos | Una fila por | Columnas |
|---|---|---|
| **Diario por elemento** | Día, área, evento y asunto | `day`, `source`, `event`, `subject`, `events` |
| **Mensual por elemento** | Mes, área, evento y asunto | `month`, `source`, `event`, `subject`, `users`, `events`, `unattributed_events`, `coverage_start`, `partial` |
| **Totales mensuales** (predeterminado) | Mes y área | `month`, `source`, `active_users`, `coverage_start`, `partial` |

`partial` es verdadero para un mes que el historial no cubre por completo, y `coverage_start` es la fecha en que comenzó la recopilación.

**Área** limita las filas a un área: **Aplicación PlaidCloud**, **Paneles de control**, **Aplicaciones**, **Visitas a aplicaciones** o **Notebooks**. Déjela en **Todas las áreas** para incluirlas todas.

### Intervalo de fechas

**Intervalo** elige los días que se leen:

- **Últimos días** (predeterminado 30) lee los días más recientes, incluido hoy.
- **Mes anterior** lee el último mes natural completo.
- **Mes en curso** lee desde el primer día de este mes hasta hoy.
- **Entre fechas** lee desde **Fecha de inicio** hasta **Fecha de fin**. Deje **Fecha de fin** vacía para leer hasta hoy.

Los días y las fechas son UTC. **Días**, **Fecha de inicio** y **Fecha de fin** aceptan una [variable](/es/guides/workflows/manage-workflow-variables/) como `{report_start}`, además de un número o una fecha `YYYY-MM-DD`. El inicio no puede ser posterior al fin.

### Destino del uso

**Tabla de destino** recibe el resultado. El paso reemplaza todo lo que contenía la tabla y siempre escribe las columnas del conjunto de datos, incluso cuando no hay filas.

## Advertencias

Estas no hacen fallar el paso. Termina con una advertencia que indica lo ocurrido y aun así escribe la tabla:

- La recopilación de uso aún no está configurada para el espacio de trabajo.
- No hubo uso en el intervalo.
- El intervalo comienza antes de lo que se conserva, por lo que se recortó para empezar donde comienza el historial. Los datos diarios se conservan 180 días y los mensuales, 25 meses.

## Registro de seguridad

Cada ejecución escribe una entrada en el Registro de seguridad con el conjunto de datos, el intervalo, la tabla de destino, el flujo de trabajo, el paso y la ejecución, y el número de filas escritas.

## Relacionado

- [Pasos generales](/es/reference/workflow-steps/general/)
- [Informes de uso](/es/administration/access/usage-reports/)
- [Get Workspace Members](/es/reference/workflow-steps/general/get-workspace-members/)
