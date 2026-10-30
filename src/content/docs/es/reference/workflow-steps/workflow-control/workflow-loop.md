---
title: Workflow Loop (paso)
description: Cree un bucle en un paso de flujo de trabajo de PlaidCloud para iterar sobre un conjunto de valores y repetir pasos para cada elemento de la colección.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/workflow-loop.md
---

## Descripción

Ejecuta un flujo de trabajo de destino una vez por cada fila de un conjunto de datos, estableciendo los valores de las columnas de cada fila como variables del proyecto antes de cada iteración. Úselo cuando tenga un proceso parametrizado que deba ejecutarse varias veces con entradas distintas; por ejemplo, “ejecutar el cierre mensual para cada unidad de negocio de esta tabla” o “cargar este informe para cada trimestre de la lista”.

Cada iteración del bucle ve las variables como si se hubieran establecido manualmente, por lo que el flujo de trabajo invocado puede referenciarlas en expresiones, filtros, rutas de archivo y nombres de tabla con la sintaxis estándar `\{variable_name}`. De forma predeterminada, el bucle es secuencial; las iteraciones no se ejecutan en paralelo.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="Un Workflow Loop sobre un conjunto de datos con las filas Q1, Q2 y Q3. Los valores de las columnas de cada fila se convierten en variables del proyecto y después se ejecuta el flujo de trabajo de destino: una pasada por fila, en secuencia, no en paralelo." style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">conjunto de datos</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">pasada 1</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">pasada 2</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">pasada 3</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">secuencial: una pasada a la vez, no en paralelo</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Las columnas de cada fila se convierten en variables del proyecto y después se ejecuta el flujo de trabajo de destino: una pasada por fila, en secuencia. Para una distribución en paralelo aislada, use en su lugar una <a href="/es/guides/workflows/create-a-macro/">macro</a>.</figcaption>
</figure>



## Flujo de trabajo que se va a detener


Primero, seleccione el proyecto que contiene el flujo de trabajo que se ejecutará en cada iteración del bucle en el menú desplegable **Proyecto**.



A continuación, seleccione el flujo de trabajo concreto que se ejecutará en el menú desplegable **Flujo de trabajo**.

## Si falla una iteración

De forma predeterminada, el bucle se detiene en la primera iteración cuyo flujo de trabajo falla, y el paso falla. En **Gestión de errores**, seleccione **Continuar tras una iteración fallida** para ejecutar todas las iteraciones aunque una falle. Cada error se conserva en **Estado de ejecución del bucle**, junto con el resultado de cada iteración, y el paso termina con una advertencia que indica cuántas iteraciones fallaron. Si la opción está desactivada, el bucle se detiene en el primer error.

## Ejemplos

Próximamente habrá ejemplos
