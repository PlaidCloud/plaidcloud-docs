---
title: Pasos de Business Central
description: "Pasos de flujo de trabajo que leen y escriben en Microsoft Dynamics 365 Business Central a través de su conexión de Business Central: importan entidades OData y contabilizan líneas de diario general."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

Pasos de flujo de trabajo que leen y escriben en Business Central a través de su [conexión de Business Central](/es/guides/connections/business-central/). El paso de importación obtiene las entidades OData v2.0 estándar de Business Central sin necesidad de escribir una consulta; el paso de contabilización contabiliza líneas de diario general mediante la canalización de escritura de ERP compartida de PlaidCloud.

## Pasos

- [Paso Import Business Central Entity](/es/reference/workflow-steps/business-central/import-business-central-entity/): cuentas, movimientos contables, clientes, proveedores, artículos y diarios, con filtros en el servidor.
- [Paso Business Central: Post General Journal Lines](/es/reference/workflow-steps/business-central/business-central-post/): contabiliza líneas en un lote de diario existente y contabiliza el lote.

## Relacionado

- [Conector REST de Business Central](/es/reference/connectors/rest/business-central/)
- [Conectarse a Business Central](/es/guides/connections/business-central/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
