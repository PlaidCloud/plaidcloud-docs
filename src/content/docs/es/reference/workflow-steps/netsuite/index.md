---
title: Pasos de NetSuite
description: "Pasos de flujo de trabajo de NetSuite: importe saldos, detalle del libro mayor, datos maestros o su propia consulta SuiteQL, y contabilice asientos de diario a través de su conexión de NetSuite."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

Pasos de flujo de trabajo que leen de NetSuite y escriben en él a través de su [conexión de NetSuite](/es/guides/connections/netsuite/). Los pasos de importación predefinidos son la forma más sencilla de extraer los datos financieros y de referencia más habituales: elija una conexión, una tabla de destino y un intervalo de fechas o un tipo de registro, sin SuiteQL que escribir.

## Pasos de importación

- [NetSuite: importar saldos](/es/reference/workflow-steps/netsuite/import-balances/): saldos de cuentas (un balance de comprobación) para un intervalo de fechas y una subsidiaria.
- [NetSuite: importar detalle del libro mayor](/es/reference/workflow-steps/netsuite/import-gl-detail/): detalle de las líneas de transacciones del libro mayor para un intervalo de fechas y una subsidiaria.
- [NetSuite: importar datos maestros](/es/reference/workflow-steps/netsuite/import-master-data/): listas maestras: cuentas, subsidiarias, departamentos, clases, ubicaciones, proveedores o clientes.
- [NetSuite: importar consulta SuiteQL](/es/reference/workflow-steps/netsuite/import-suiteql-query/): ejecute su propia consulta SuiteQL y cargue el resultado en una tabla con tipos definidos, con las ventanas de fechas y la paginación resueltas por usted.

## Pasos de contabilización

- [Post NetSuite Journal Entry](/es/reference/workflow-steps/netsuite/post-netsuite-journal-entry/): contabilice en NetSuite asientos de diario con encabezado y líneas.

## Extracciones personalizadas

Para los datos que no cubren los pasos de importación predefinidos (una consulta a medida, o un registro de NetSuite sin paso predefinido), use [NetSuite: importar consulta SuiteQL](/es/reference/workflow-steps/netsuite/import-suiteql-query/) con su propio SuiteQL. Consulte [Ejemplos de consultas SuiteQL de NetSuite](/es/guides/connections/netsuite-financial-queries/) para ver puntos de partida.

## Relacionado

- [Conector REST de NetSuite](/es/reference/connectors/rest/netsuite/)
- [Conectarse a NetSuite](/es/guides/connections/netsuite/)
- [Importar datos financieros de NetSuite](/es/guides/connections/import-netsuite-financials/)
