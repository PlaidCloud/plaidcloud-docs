---
title: Run SAP PCM Console Job
description: Ejecute un trabajo de la consola de SAP PCM desde un paso de flujo de trabajo de PlaidCloud para realizar de forma remota tareas de procesamiento por lotes y operaciones administrativas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-console-job.md
---

## Descripción



Inicia un trabajo en la consola de SAP PCM del servidor de PCM remoto; se usa normalmente para tareas administrativas o por lotes que PCM expone mediante su interfaz de consola en lugar de la API de cálculo de modelos.

Entre los casos de uso se incluyen operaciones de archivado, ejecuciones de Hyper Loader o rutinas de mantenimiento específicas del proveedor. El trabajo y los parámetros exactos dependen de su implementación de PCM.


## Nuestras credenciales


PlaidCloud es socio oficial de SAP y proveedor preferido de servicios relacionados con el diseño y la implementación de modelos de SAP PCM.








## Ejemplos


Seleccione “Agente que usar” en la lista desplegable, escriba la ruta del archivo de consola en el campo “Console File Path”, marque la casilla “Wait for Console Job to Complete” (si lo desea) y haga clic en “Save and Run Step”.
