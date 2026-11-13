---
title: Administrar variables de flujo de trabajo
description: Administre variables de flujo de trabajo en PlaidCloud para almacenar y pasar valores dinámicos entre pasos y lograr una lógica de procesamiento de datos flexible.
sidebar:
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/manage-workflow-variables.md
---

PlaidCloud permite variables tanto en el ámbito del proyecto como en el del flujo de trabajo. Esto permite definir variables para todo el proyecto o pasar información fácilmente entre flujos de trabajo. Las variables y sus valores se ven al hacer clic en el ícono de variables en la jerarquía de **Flujos de trabajo**.



Desde la tabla de variables puede ver las variables y sus valores actuales, y editar los valores. También puede agregar variables nuevas o eliminar las existentes.

## Variables integradas

La configuración y las expresiones de los pasos pueden usar estas variables integradas sin definirlas:

| Variable | Valor |
|---|---|
| `{project}`, `{model}`, `{cloud}` | Los nombres del proyecto, el modelo y el espacio de trabajo. |
| `{date}` | La hora UTC actual de la ejecución en formato largo, como `Wednesday, 11 November 2026 10:30PM UTC +0`. |
| `{date_iso}` | El mismo instante en ISO 8601, como `2026-11-12T22:49:56+00:00`. |

Use `{date_iso}` cuando una expresión necesite leer una parte de la fecha. Si toma sus primeros 7 caracteres obtiene el mes (`2026-11`), y con los primeros 10 obtiene el día (`2026-11-12`). `{date_iso}` funciona en todos los lugares donde funciona `{date}`, incluidas las plantillas de correo electrónico de notificación y los pasos Forecast, Parity y Solver.
