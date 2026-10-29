---
title: Calculate PCM Model
description: Active los cálculos de un modelo de SAP PCM desde un paso de flujo de trabajo de PlaidCloud para ejecutar trabajos de procesamiento de rentabilidad y asignación de costos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/calculate-pcm-model.md
---

## Descripción



Activa el motor de cálculo de un modelo de SAP Profitability and Cost Management (PCM). Úselo en un flujo de trabajo para ejecutar el cálculo de costos después de que las cargas de datos anteriores hayan rellenado las entradas del modelo (asignaciones, inductores, datos de origen).

El cálculo es asíncrono en el servidor de PCM; combínelo con [Stop PCM Model Calculation](/es/reference/workflow-steps/sap-pcm/stop-pcm-model-calculation/) si necesita cancelar un cálculo de larga duración.


## Nuestras credenciales


PlaidCloud es socio oficial de SAP y proveedor preferido de servicios relacionados con el diseño y la implementación de modelos de SAP PCM.







## Ejemplos


Seleccione “Agente que usar” en la lista desplegable, escriba el nombre del modelo en el campo “Nombre del modelo”, marque la casilla “Wait for Calculation to Complete” (si lo desea) y haga clic en “Save and Run Step”.
