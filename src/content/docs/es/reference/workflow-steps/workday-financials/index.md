---
title: Pasos de Workday Financials
description: "Pasos de flujo de trabajo que leen y escriben en Workday Financials a través de su conexión de Workday Financials: importar datos mediante un informe RaaS y contabilizar asientos de diario."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

Pasos de flujo de trabajo que leen y escriben en Workday Financials a través de su [conexión de Workday Financials](/es/guides/connections/workday-financials/). El paso de importación extrae un informe Report-as-a-Service (RaaS) proporcionado por el cliente; el paso de contabilización contabiliza asientos de diario mediante la canalización de escritura de ERP compartida de PlaidCloud.

## Pasos

- [Import Workday Entity](/es/reference/workflow-steps/workday-financials/import-workday-entity/): extrae un informe RaaS, con filtros de parámetros del informe.
- [Workday Financials: Post Journal Entry](/es/reference/workflow-steps/workday-financials/workday-post/): contabiliza asientos de diario mediante `Submit_Accounting_Journal`, con un asiento de reversión contabilizado para las correcciones.

## Relacionado

- [Conector de Workday Financials](/es/reference/connectors/rest/workday-financials/)
- [Conectarse a Workday Financials](/es/guides/connections/workday-financials/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
