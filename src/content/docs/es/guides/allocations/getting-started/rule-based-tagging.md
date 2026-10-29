---
title: Etiquetado basado en reglas
description: Configure el etiquetado basado en reglas en las asignaciones de PlaidCloud para clasificar y etiquetar automáticamente los registros de datos con criterios definidos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

El etiquetado basado en reglas le permite marcar las filas de origen con metadatos que el motor de asignación usa para decidir *adónde* va cada fila. Úselo cuando necesite que el comportamiento de la asignación varíe según la fila; por ejemplo, cuando los costos de un centro de costo deban distribuirse según el número de empleados, pero los de otro deban distribuirse según los ingresos.

## Cuándo usarlo

- Una regla de asignación única no refleja cómo debe distribuirse realmente el costo (reglas distintas para distintos tipos de costo).
- Desea dirigir ciertas filas de origen a destinos concretos y dejar que las demás se distribuyan normalmente.
- Está modelando una asignación de varios grupos en la que cada grupo usa un inductor distinto.

## Cómo funciona el etiquetado

1. **Etiquete el origen.** La tabla de valores recibe una o más columnas de etiquetas que clasifican cada fila.
2. **Haga referencia a las etiquetas en la regla de asignación.** Al configurar el paso de asignación, expresa las reglas con la forma *“si la etiqueta de origen X = valor Y, asignar con el inductor D y la dimensión de destino T”*.
3. **El motor enruta las filas.** Cada fila de origen se compara con las reglas en orden; la primera regla que coincide decide el comportamiento de la asignación.

## Patrones de origen adecuados para etiquetas

- Una columna llamada `cost_category` con valores como `payroll`, `facilities`, `it`, `marketing`
- Una columna llamada `pool` que nombra el grupo de asignación al que pertenece la fila
- Una columna booleana como `is_overhead` que activa un tratamiento distinto

## Ejemplo

Una tabla de costos con `cost_center` y `cost_category`:

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

Puede configurar dos reglas de asignación:

- **Las filas de nómina** se distribuyen según el inductor de número de empleados
- **Las filas de TI** se distribuyen según el inductor de número de usuarios

Ambas reglas se ejecutan sobre la misma tabla de origen; las etiquetas deciden cuál se aplica a cada fila.

## Temas relacionados

- [Inicio rápido de asignaciones](/es/guides/allocations/getting-started/allocations-quick-start/): el flujo básico antes de agregar el etiquetado
- [Configurar una asignación](/es/guides/allocations/setup/configure-an-allocation/): referencia completa del paso
- [Paso de reglas de asignación](/es/reference/workflow-steps/allocation/allocation-rules/): el paso de flujo de trabajo que consume datos etiquetados
