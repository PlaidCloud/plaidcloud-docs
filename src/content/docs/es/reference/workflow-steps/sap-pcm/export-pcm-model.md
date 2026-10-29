---
title: Calculate and Export PCM Model
description: Ejecute el cálculo de un modelo de PCM y exporte el resultado a una base de datos o a un archivo delimitado, mediante un agente de PlaidLink.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## Descripción

Calcula un modelo de SAP PCM y exporta el resultado en un solo paso, mediante un [agente de PlaidLink](/es/reference/workflow-steps/agent/) con acceso a la instalación de PCM. Mientras que [Calculate PCM Model](/es/reference/workflow-steps/sap-pcm/calculate-pcm-model/) solo ejecuta el cálculo, este paso también traslada la salida.

## Configuración

### Agente que usar

El agente de PlaidLink que accede a la instalación de PCM.

### Información del modelo

- **Nombre del modelo**: el modelo de PCM que se calcula.
- **Export specification path**: la especificación de exportación de PCM que describe qué se exporta.

### Destino de salida de la exportación

Elija un destino de base de datos, un destino de archivo o ambos.

**A una base de datos**: activada de forma predeterminada; la exportación escribe a través del destino de base de datos configurado en la especificación.

**A un archivo**: desactivada de forma predeterminada. Cuando está activada:

- **Ruta del archivo**: dónde escribe el archivo el agente.
- **Alias**: el alias registrado en la exportación. El valor predeterminado es `DEFAULT ALIAS`.
- **Precision**: posiciones decimales de los valores exportados. El valor predeterminado es 0.
- **Delimitador**: coma, tabulación, barra vertical, punto y coma, espacio, `@`, `~` o `:`. El valor predeterminado es la tabulación.
- **Anexar**: desactivada de forma predeterminada, por lo que cada ejecución reemplaza el archivo. Actívela para acumular ejecuciones.
- **Include rules**: desactivada de forma predeterminada. Actívela para exportar las reglas del modelo junto con los valores.
- **Unicode**: desactivada de forma predeterminada. Actívela cuando los datos exportados contengan caracteres fuera de la codificación predeterminada.

## Temas relacionados

- [Pasos de SAP-PCM](/es/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model](/es/reference/workflow-steps/sap-pcm/calculate-pcm-model/)
- [Run SAP PCM Hyper Loader](/es/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/)
