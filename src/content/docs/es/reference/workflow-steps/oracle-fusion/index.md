---
title: Pasos de Oracle Fusion
description: "Pasos de flujo de trabajo que leen de Oracle Fusion Cloud y escriben en él a través de su conexión de Oracle Fusion: importan saldos del libro mayor y lotes de asientos mediante OData/BIP o extracción masiva FBDI, y contabilizan asientos de diario."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

Pasos de flujo de trabajo que leen de Oracle Fusion Cloud y escriben en él a través de su [conexión de Oracle Fusion](/es/guides/connections/oracle-fusion/). Dos pasos de importación cubren distintos volúmenes de extracción: una llamada directa OData/BIP para las extracciones habituales y una extracción masiva asíncrona FBDI/BIP para las grandes; el paso de contabilización registra lotes de asientos a través de la canalización de escritura de ERP compartida de PlaidCloud.

## Pasos

- [Import Fusion Entity](/es/reference/workflow-steps/oracle-fusion/import-fusion-entity/): saldos del libro mayor y lotes de asientos, con filtros de fecha, período y rango numérico en el servidor.
- [Import Fusion Bulk Extract](/es/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/): las mismas entidades, mediante un trabajo de exportación asíncrono FBDI/BIP para extracciones grandes.
- [Oracle Fusion: Post Journal Entry](/es/reference/workflow-steps/oracle-fusion/oracle-fusion-post/): contabiliza lotes de asientos del libro mayor a través de la interfaz GL de FBDI, con un asiento de reversión contabilizado para las correcciones.

## Temas relacionados

- [Oracle Fusion Connector](/es/reference/connectors/erp/oracle-fusion/)
- [Connect to Oracle Fusion](/es/guides/connections/oracle-fusion/)
- [Review ERP Post History](/es/guides/connections/erp-post-history/)
