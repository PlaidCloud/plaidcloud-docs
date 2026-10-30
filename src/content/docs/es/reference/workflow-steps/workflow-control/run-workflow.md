---
title: Ejecutar flujo de trabajo
description: Ejecute un flujo de trabajo existente desde un paso de flujo de trabajo de PlaidCloud para encadenar ejecuciones y crear canalizaciones de procesamiento con varios flujos de trabajo.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/run-workflow.md
---

## Descripción

Activa otro flujo de trabajo como parte de la ejecución del flujo de trabajo actual. Úselo para encadenar flujos de trabajo cuando un proceso depende lógicamente de otro; por ejemplo, un flujo de trabajo de “cierre de mes” que llama a un flujo de trabajo de “cargar datos reales”, luego a uno de “ejecutar asignaciones” y después a uno de “publicar paneles de control”.

El flujo de trabajo invocado se ejecuta de forma independiente y puede estar en el mismo proyecto o en otro. De forma predeterminada, el flujo de trabajo que llama continúa sin esperar; active la opción **Wait until processing completes** si los pasos siguientes del flujo de trabajo que llama dependen de que el flujo invocado termine primero.



## Flujo de trabajo que se va a ejecutar


Primero, seleccione el proyecto que contiene el flujo de trabajo que se ejecutará en el menú desplegable **Proyecto**.



A continuación, seleccione el flujo de trabajo concreto que se ejecutará en el menú desplegable **Flujo de trabajo**.



Además, hay una opción **Wait until processing completes before continuing.** Si marca esta casilla, la ejecución del flujo de trabajo actual se aplaza hasta que el flujo de trabajo invocado termine su ejecución. De forma predeterminada, esta opción está desactivada, lo que significa que el flujo de trabajo actual, en el que se encuentra este paso, continúa su procesamiento en paralelo con el flujo de trabajo invocado.







## Ejemplos

Aún no hay ejemplos...
