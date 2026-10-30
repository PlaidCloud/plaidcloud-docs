---
title: Conector de Oracle Fusion
description: Configure una conexión a Oracle Fusion Cloud en PlaidCloud con credenciales OAuth2 para importar saldos del libro mayor y lotes de diarios mediante OData/BIP, y contabilizar diarios mediante FBDI.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-fusion.md
---

## Documentación de la API

Las referencias de la [API REST (OData)](https://docs.oracle.com/en/cloud/saas/financials/) y de [BI Publisher (BIP) y File-Based Data Import (FBDI)](https://docs.oracle.com/en/cloud/saas/applications-common/) de Oracle Fusion Cloud documentan los puntos de conexión y la ruta de extracción y carga masivas que usa este conector.

## Cómo funciona la autenticación

La conexión se autentica con credenciales de cliente OAuth2 (o con las credenciales de API de autenticación básica que emite la configuración de seguridad de Fusion Cloud para los usuarios de integración) frente a un usuario de API dedicado. El rol del usuario de API controla tanto qué entidades del libro mayor puede leer como mediante qué funciones de FBDI y GL Interface puede contabilizar.

## Configuración

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| URL de la instancia | Texto | La URL de su instancia de Fusion Cloud, p. ej., `https://yourorg.fa.us2.oraclecloud.com`. |
| ID de cliente | Texto | El ID de cliente OAuth2 del usuario de API (o el nombre de usuario, en la autenticación básica). |
| Secreto de cliente | Texto | El secreto de cliente OAuth2 del usuario de API (o la contraseña, en la autenticación básica). Se almacena cifrado. |

## Entidades disponibles para importar

Dos pasos de importación cubren distintos tamaños de extracción, ambos sobre `gl_balances` y `journal_batches`:

- **Import Fusion Entity** (paso): una llamada directa de OData/BIP, para una extracción habitual y acotada.
- **Import Fusion Bulk Extract** (paso): un trabajo de exportación asíncrono de FBDI/BIP, para una extracción grande.

Ambos admiten filtros de rango (`ge`/`le`) sobre campos de fecha, de período contable y de saldo o importe numérico, además de filtros de igualdad sobre campos discretos como el libro mayor o la moneda. Consulte [Import Fusion Entity](/es/reference/workflow-steps/oracle-fusion/import-fusion-entity/) (paso) e [Import Fusion Bulk Extract](/es/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) (paso) para ver la referencia completa de los campos.

## Contabilizar asientos de diario

El paso **Oracle Fusion: Post Journal Entry** contabiliza lotes de diario del libro mayor mediante el flujo de escritura de ERP compartido de PlaidCloud: escribe el lote en la tabla de preparación GL_INTERFACE de Oracle como un archivo FBDI, envía el trabajo ESS Journal Import Launcher y lo consulta hasta que alcanza un estado terminal, y confirma antes de informar de que un lote se contabilizó. Una corrección contabiliza un nuevo asiento de reversión con el débito y el crédito intercambiados, en lugar de editar el original. Consulte [Oracle Fusion: Post Journal Entry](/es/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) (paso) para ver la referencia de los campos y [Conectarse a Oracle Fusion](/es/guides/connections/oracle-fusion/) para ver el tutorial completo de contabilización.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| Latencia del trabajo ESS | Journal Import Launcher se ejecuta como un trabajo programado, no como una llamada síncrona: una ejecución de contabilización tarda considerablemente más que una escritura directa mediante la API. |
| Latencia de la extracción masiva | `import_fusion_bulk_extract` espera a un trabajo de exportación de FBDI/BIP: resérvelo para extracciones demasiado grandes para la ruta directa de `import_fusion_entity`. |
## Temas relacionados

- [Conectarse a Oracle Fusion (guía)](/es/guides/connections/oracle-fusion/): paso a paso para crear la conexión, probarla, importar una entidad y contabilizar un diario.
- [Import Fusion Entity](/es/reference/workflow-steps/oracle-fusion/import-fusion-entity/) (paso)
- [Import Fusion Bulk Extract](/es/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) (paso)
- [Oracle Fusion: Post Journal Entry](/es/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) (paso)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
