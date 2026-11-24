---
title: Ruta de aprendizaje de Ingeniería de datos
description: Qué leer antes de los laboratorios Profesional y Experto de Ingeniería de datos de PlaidCloud, y qué le pide cada laboratorio.
sidebar:
  label: Ingeniería de datos
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

La ruta de Ingeniería de datos trata de construir flujos de trabajo correctos, controlados por variables y rápidos. Empiece por la ruta de [Fundamentos](/es/guides/certification/foundations/). Para saber cómo funcionan los laboratorios, consulte [Certificación de PlaidCloud](/es/guides/certification/).

## Profesional

### Lea en este orden

1. [Crear flujo de trabajo](/es/guides/workflows/create-workflow/)
2. [Pasos del flujo de trabajo](/es/reference/workflow-steps/), en particular [Table Inner Join](/es/reference/workflow-steps/tables/table-inner-join/) y [Table Extract](/es/reference/workflow-steps/tables/table-extract/)
3. [Administrar variables de flujo de trabajo](/es/guides/workflows/manage-workflow-variables/)
4. [Reutilice su trabajo: variables, macros y UDF](/es/get-started/tutorials/reuse-variables-macros-udfs/)
5. [Ejecutar un flujo de trabajo](/es/guides/workflows/run-a-workflow/)
6. [Ver el registro del flujo de trabajo](/es/guides/workflows/viewing-workflow-log/)

### Qué le pide el laboratorio

El laboratorio se llama *Ingeniería de datos: construcción mensual de ventas*.

Se cargan tres tablas sin procesar: líneas de ventas, tiendas y productos. En el flujo de trabajo del laboratorio, usted construye un resumen mensual con una fila por región y categoría de producto, con unidades e ingresos, para las líneas vendidas de un mes. El mes proviene de una variable del proyecto, no de un valor escrito en un paso: el laboratorio cambia la variable y vuelve a ejecutar el flujo de trabajo. Use solo pasos estándar, sin pasos de SQL ni de código.

El laboratorio comprueba que el flujo de trabajo se ejecuta, que usa solo pasos estándar y que el resumen es correcto para el mes y de nuevo para otro mes.

## Experto

El laboratorio Experto tiene tiempo límite: dispone de 4 horas desde el momento en que lo inicia.

### Lea en este orden

1. [Depurar un flujo de trabajo](/es/get-started/tutorials/debug-a-workflow/)
2. [Ver el registro del flujo de trabajo](/es/guides/workflows/viewing-workflow-log/)
3. [Administrar errores de pasos](/es/guides/workflows/managing-step-errors/)
4. [Vista previa de los datos de un paso](/es/guides/workflows/preview-step-data/)
5. [Optimizar un flujo de trabajo](/es/guides/workflows/optimize-a-workflow/)
6. [Pasos del flujo de trabajo](/es/reference/workflow-steps/), en particular [Table Inner Join](/es/reference/workflow-steps/tables/table-inner-join/)

### Qué le pide el laboratorio

El laboratorio se llama *Ingeniería de datos Experto: reparar y acelerar la compilación nocturna*.

Un flujo de trabajo nocturno ha dejado de ejecutarse y, antes de eso, era demasiado lento. Usted lee el registro de ejecución, encuentra todas las causas y corrige el flujo de trabajo para que se complete correctamente, genere el resumen correcto y termine en una pequeña fracción de su tiempo anterior. Las filas sin cuenta se excluyen, y las cuentas listadas dos veces no deben inflar los recuentos. Use solo pasos estándar y deje las tablas de entrada como están.

El laboratorio comprueba que el flujo de trabajo se ejecuta, que usa solo pasos estándar, que el resumen es correcto, que las tablas de entrada no han cambiado y que el flujo de trabajo es lo bastante rápido.
