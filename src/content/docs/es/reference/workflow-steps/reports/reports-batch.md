---
title: Reports Batch
description: Genere informes PDF por lotes desde un paso de flujo de trabajo de PlaidCloud para producir varios informes a partir de plantillas con distintas entradas de datos.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/reports/reports-batch.md
---

## Descripción



Genera muchos informes PDF a partir de una única plantilla RML, controlados por una tabla de control. Se produce un informe por cada fila de la tabla de control, y los valores de las columnas de cada fila se usan como parámetros al generar ese informe.

Uso habitual: estados de cuenta de clientes (un PDF por cliente), estados financieros por unidad (un PDF por unidad de negocio), facturas (un PDF por pedido). Compárelo con [Report Single](/es/reference/workflow-steps/reports/report-single/) para la generación de informes puntuales.


## Nombres que lee la plantilla

La plantilla lee cada origen de la pestaña **Datos del informe**, y cada columna de destino de la asignación de **Origen de datos de valores de registro por lotes**, por su nombre. No hay sección de constantes: cada fila del lote aporta a la plantilla los valores de su informe. Los orígenes nuevos se llaman `new_source`, `new_source_2` y así sucesivamente, y la plantilla puede leerlos tal cual.


## Qué se comprueba al guardar

Cada nombre de origen y de columna del lote debe estar indicado, ser propio y ser legible por la plantilla, con las mismas reglas que [Report Single](/es/reference/workflow-steps/reports/report-single/), con columnas de lote en lugar de constantes: *Batch column name 'unit id' can't be read by the template: use letters, digits and underscores, starting with a letter or underscore.*

Si guarda con una tabla de origen del lote elegida pero con la asignación del lote vacía, la asignación se rellena a partir de esa tabla, igual que lo haría Populate.


## Tabla de lote vacía

Cuando la tabla de origen del lote no tiene filas, el paso finaliza correctamente con una advertencia que nombra la tabla del lote, y no se produce ningún informe.


## Ejemplos

Aún no hay ejemplos...
