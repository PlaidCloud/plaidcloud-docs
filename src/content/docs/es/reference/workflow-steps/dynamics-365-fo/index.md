---
title: Pasos de Dynamics 365 F&O
description: "Pasos de flujo de trabajo que leen y escriben en Dynamics 365 Finance & Operations a través de su conexión de D365 F&O: importan entidades OData/DMF y contabilizan asientos de diario."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

Pasos de flujo de trabajo que leen y escriben en Dynamics 365 Finance & Operations (D365 F&O) a través de su [conexión de D365 F&O](/es/guides/connections/dynamics-365-fo/). El paso de importación trae entidades OData o extracciones masivas de DMF sin necesidad de escribir OData; el paso de contabilización contabiliza asientos de diario del libro mayor mediante el flujo de escritura de ERP compartido de PlaidCloud.

## Pasos

- [Import D365 F&O Entity](/es/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/): datos maestros y encabezados de diarios, en modo OData o masivo de DMF, con filtros en el servidor.
- [D365 F&O: Post Journal Entry](/es/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/): contabiliza asientos de diario del libro mayor, con un asiento de reversión contabilizado para las correcciones.

## Relacionado

- [Conector REST de Dynamics 365 F&O](/es/reference/connectors/rest/dynamics-365-fo/)
- [Conexión con Dynamics 365 Finance & Operations](/es/guides/connections/dynamics-365-fo/)
- [Revisar el historial de contabilización de ERP](/es/guides/connections/erp-post-history/)
