---
title: Set Project Variable Values from Table (paso)
description: Lea valores de una tabla del proyecto y asígnelos a variables del proyecto que persisten entre ejecuciones del flujo de trabajo.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## Descripción

Lee valores de una tabla del proyecto y los asigna a variables del *proyecto*. A diferencia de [Set Workflow Variable Values from Table (paso)](/es/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/), los valores persisten más allá de la ejecución: todos los flujos de trabajo del proyecto los ven hasta que algo los cambie de nuevo.

Úselo para el estado que sobrevive a una sola ejecución: el último período cargado correctamente, una marca de tiempo de referencia o el nombre del escenario actual.

## Configuración

### Columnas de origen

Asigne cada columna de origen a la variable del proyecto que rellena. El paso lee una sola fila, así que reduzca la tabla a una fila antes de que se ejecute.

### Seleccionar subconjunto de datos

Una expresión de filtro que reduce las filas de origen.

### Aplicar filtro secundario a los datos de resultado

Un filtro de tipo `HAVING` que se aplica después de la agregación.

### Final Data Table Slicing (Limit)

Desactivado de forma predeterminada y limitado a una fila cuando está activado. Actívelo con una ordenación explícita cuando el origen pueda devolver varias filas candidatas.

## Elementos relacionados

- [Pasos de control de flujos de trabajo](/es/reference/workflow-steps/workflow-control/)
- [Set Project Variable (paso)](/es/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table (paso)](/es/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
