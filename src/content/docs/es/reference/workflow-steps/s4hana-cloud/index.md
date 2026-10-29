---
title: Pasos de SAP S/4HANA Cloud
description: "Pasos de flujo de trabajo que leen de SAP S/4HANA Cloud Public Edition y escriben en él a través de su conexión de S/4HANA Cloud: importan el balance de comprobación y las partidas de asientos, y contabilizan asientos de diario."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

Pasos de flujo de trabajo que leen de SAP S/4HANA Cloud Public Edition y escriben en él a través de su [conexión de S/4HANA Cloud](/es/guides/connections/s4hana-cloud/). El paso de importación extrae datos del balance de comprobación o de las partidas de asientos sin que tenga que escribir OData; el paso de contabilización registra asientos de diario a través de la canalización de escritura de ERP compartida de PlaidCloud.

## Pasos

- [Import S/4HANA Entity](/es/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/): datos del balance de comprobación y de las partidas de asientos, con filtros en el servidor.
- [S/4HANA: Post Journal Entry](/es/reference/workflow-steps/s4hana-cloud/s4hana-post/): contabiliza asientos de diario mediante SOAP, con un asiento de reversión contabilizado para las correcciones.

## Temas relacionados

- [SAP S/4HANA Cloud REST Connector](/es/reference/connectors/rest/s4hana-cloud/)
- [Connect to SAP S/4HANA Cloud](/es/guides/connections/s4hana-cloud/)
- [Review ERP Post History](/es/guides/connections/erp-post-history/)
