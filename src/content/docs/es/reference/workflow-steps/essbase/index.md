---
title: Pasos de Oracle Essbase
description: Pasos de flujo de trabajo que leen de un cubo de Oracle Essbase a través de su conexión de Essbase (consultas MDX en vivo y esquemas de dimensión cargados en una dimensión de PlaidCloud) en nube directa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/index.md
---

Pasos de flujo de trabajo que leen de Oracle **Essbase** a través de su [conexión de Oracle Essbase](/es/guides/connections/essbase/): datos de cubo mediante una consulta MDX en vivo y un esquema de dimensión cargado en una dimensión de PlaidCloud. Se accede a Essbase en **nube directa** mediante su API REST: estos pasos no tienen ruta mediante un agente local.

## Pasos

- [Essbase: consultar cubo](/es/reference/workflow-steps/essbase/essbase-query/): ejecute una consulta MDX en vivo contra un cubo y deposite la cuadrícula de resultados como una tabla. Nube directa.
- [Essbase: leer dimensión](/es/reference/workflow-steps/essbase/essbase-dimension-read/): cargue el esquema de una dimensión de Essbase en una dimensión de PlaidCloud. Nube directa.

## Relacionado

- [Conexión con Oracle Essbase (guía)](/es/guides/connections/essbase/)
- [Conector de Oracle Essbase](/es/reference/connectors/erp/oracle-essbase/)
