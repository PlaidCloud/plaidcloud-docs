---
title: Generar error de flujo de trabajo
description: Genere un error personalizado en un paso de flujo de trabajo de PlaidCloud para activar la gestión de errores y detener la ejecución cuando no se cumplan las condiciones.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/raise-workflow-error.md
---

## Descripción

Fuerza el flujo de trabajo a un estado de error con un mensaje personalizado. Úselo cuando un paso deba hacer fallar el flujo de trabajo según una condición de los datos que detectaron pasos anteriores; por ejemplo, “fallar si el recuento de filas es cero”, “fallar si una tabla de validación de claves tiene valores sin asignar” o “fallar si una comprobación de saldos no concilia”.

Combínelo con [condiciones de paso](/es/guides/workflows/step-conditions/) para que el error solo se active cuando realmente algo esté mal. Cuando se ejecuta el paso, detiene el flujo de trabajo de inmediato y escribe el error en el registro del flujo de trabajo, lo que a su vez puede activar el flujo de trabajo de corrección si hay uno configurado.


## Generar error de flujo de trabajo


Pensado principalmente para usarse con condiciones de paso: el paso puede configurarse para ejecutarse si se cumplen las condiciones y generar un error dentro del flujo de trabajo.
