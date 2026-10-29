---
title: Set Workflow Variable Values from Table (paso)
description: Lea valores de una tabla del proyecto y asígnelos a variables del flujo de trabajo, de modo que los pasos posteriores se ramifiquen o filtren según los datos y no según valores fijos.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## Descripción

Lee valores de una tabla del proyecto y los asigna a variables del flujo de trabajo. Úselo para dirigir un flujo de trabajo con sus propios datos: lea de una tabla de control el último período cerrado, un recuento de filas o una ruta de archivo, y permita que los pasos posteriores lo referencien.

Las variables que se establecen aquí viven durante la ejecución del flujo de trabajo. Para establecer valores que persistan entre los flujos de trabajo del proyecto, use [Set Project Variable Values from Table (paso)](/es/reference/workflow-steps/workflow-control/set-project-variable-from-table/).

## Configuración

### Columnas de origen

Asigne cada columna de origen a la variable del flujo de trabajo que rellena. El paso lee una sola fila, así que reduzca la tabla a una fila antes de que se ejecute.

### Seleccionar subconjunto de datos

Una expresión de filtro que reduce las filas de origen, normalmente a la fila que contiene los valores que desea.

### Aplicar filtro secundario a los datos de resultado

Un filtro de tipo `HAVING` que se aplica después de la agregación, para cuando el valor proviene de un cálculo agrupado.

### Final Data Table Slicing (Limit)

Desactivado de forma predeterminada y limitado a una fila cuando está activado. Actívelo con una ordenación explícita cuando el origen pueda devolver varias filas candidatas y desee una concreta.

## Elementos relacionados

- [Pasos de control de flujos de trabajo](/es/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable (paso)](/es/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table (paso)](/es/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [Administrar variables del flujo de trabajo](/es/guides/workflows/manage-workflow-variables/)
