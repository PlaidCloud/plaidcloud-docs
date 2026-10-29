---
title: Paso Table Restore to Timestamp
description: Restaure una tabla de PlaidCloud, en su lugar, a su instantánea más reciente tomada en un momento dado o antes, como paso de flujo de trabajo.
sidebar:
  order: 45
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-restore-timestamp.md
---

## Descripción

**Tabla: restaurar a una marca de tiempo** reemplaza una tabla, en su lugar, por su instantánea más reciente tomada en un momento dado o antes. Úselo para devolver una tabla a su estado al cierre de un período, o antes de una carga que salió mal. La restauración cambia la propia tabla, por lo que todos los pasos y paneles de control que la leen ven las filas restauradas.

## Restaurar a un momento dado

| Configuración | Obligatorio | Qué hace |
| --- | --- | --- |
| Tabla | Sí | La tabla que se restaurará. |
| Marca de tiempo | Sí | El momento, como una hora ISO-8601 como `2026-09-30T23:59:59Z` o como segundos desde 1970. Una hora sin zona se interpreta como UTC. También sirve una variable de flujo de trabajo como `{restore_time}`. |
| Se cuenta una instantánea tomada exactamente en la marca de tiempo | No | Activada de forma predeterminada. Desactívela para restaurar solo a una instantánea tomada antes de la marca de tiempo. |

Si no se tomó ninguna instantánea en la marca de tiempo o antes, el paso termina con una advertencia, deja la tabla como está y el flujo de trabajo continúa. Una tabla que no se encuentra también termina con una advertencia. En un motor de almacenamiento que solo conserva instantáneas con nombre, la tabla solo puede restaurarse a una instantánea tomada exactamente en la marca de tiempo; tome una instantánea con nombre en el momento al que querrá volver.

## Relacionado

- [Restaurar tablas](/es/reference/workflow-steps/import/restore-tables/)
- [Pasos de tabla](/es/reference/workflow-steps/tables/)
