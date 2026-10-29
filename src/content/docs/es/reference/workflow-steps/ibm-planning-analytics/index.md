---
title: Pasos de IBM TM1 / Planning Analytics
description: "Pasos de flujo de trabajo que leen de un servidor IBM TM1 / Planning Analytics a través de su conexión de TM1: datos de cubo mediante vista guardada o MDX, y jerarquías de dimensiones, de forma directa en la nube o mediante un agente de PlaidLink local."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/index.md
---

Pasos de flujo de trabajo que leen de IBM **TM1 / Planning Analytics** a través de su [conexión de TM1](/es/guides/connections/tm1/): datos de cubo mediante vista guardada o MDX con un segmento opcional de punto de vista, y jerarquías de dimensiones cargadas en una dimensión de PlaidCloud. Acceda a TM1 de forma directa en la nube o, para un servidor al que solo se puede llegar desde dentro de su propia red, mediante un agente de PlaidLink local.

## Pasos

- [TM1: consultar cubo](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query/): lee un cubo mediante vista guardada o MDX, con un segmento de punto de vista y una vista previa antes de guardar. Directo en la nube.
- [TM1: consultar cubo (agente)](/es/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/): el equivalente local de TM1: consultar cubo, enviado a través de un agente de PlaidLink instalado.
- [TM1: leer dimensión](/es/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/): carga una jerarquía de TM1 en una dimensión de PlaidCloud. Directo en la nube.

## Relacionado

- [Conectarse a TM1 (guía)](/es/guides/connections/tm1/)
- [Conector de TM1](/es/reference/connectors/rest/tm1/)
