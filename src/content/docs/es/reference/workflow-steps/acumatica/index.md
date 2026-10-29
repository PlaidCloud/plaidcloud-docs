---
title: Pasos de Acumatica
description: "Pasos de flujo de trabajo que leen y escriben en Acumatica a través de su conexión de Acumatica: importan entidades REST basadas en contratos y contabilizan asientos de diario, facturas, facturas de proveedor y pagos."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

Pasos de flujo de trabajo que leen y escriben en Acumatica a través de su [conexión de Acumatica](/es/guides/connections/acumatica/). El paso de importación obtiene las entidades REST basadas en contratos de Acumatica sin necesidad de escribir OData; el paso de contabilización registra asientos de diario, facturas de venta, facturas de proveedor y pagos mediante la canalización de escritura de ERP compartida de PlaidCloud.

## Pasos

- [Import Acumatica Entity](/es/reference/workflow-steps/acumatica/import-acumatica-entity/): entidades de datos maestros y transaccionales, con filtros del lado del servidor.
- [Acumatica: Post Documents](/es/reference/workflow-steps/acumatica/acumatica-post/): contabiliza asientos de diario, facturas de venta, facturas de proveedor y pagos.

## Relacionado

- [Conector REST de Acumatica](/es/reference/connectors/rest/acumatica/)
- [Conectar con Acumatica](/es/guides/connections/acumatica/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
