---
title: Ejecutar un rango de pasos en un flujo de trabajo
description: Ejecute un rango específico de pasos dentro de un flujo de trabajo de PlaidCloud para ejecutar de forma selectiva partes de su canalización de procesamiento de datos.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

Aunque ejecutar pasos individuales resulta útil, también puede serlo ejecutar subconjuntos de un flujo de trabajo completo para desarrollo, pruebas o resolución de problemas. Para ejecutar un subconjunto de pasos, seleccione todos los pasos que desea ejecutar y elija **Ejecutar pasos seleccionados** en el menú **Acciones** situado en la parte superior de la jerarquía de pasos del flujo de trabajo. Esto activa un procesamiento normal del flujo de trabajo, pero lo inicia al comienzo de los pasos seleccionados y lo detiene cuando se completa el último paso seleccionado.

Si el último paso seleccionado está dentro de un grupo configurado en [**Execute in Parallel**](/es/guides/workflows/controlling-parallel-execution/), la ejecución también espera a que terminen todos los demás pasos seleccionados de ese grupo antes de detenerse.
