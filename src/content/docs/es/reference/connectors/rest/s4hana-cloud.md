---
title: Conector REST de SAP S/4HANA Cloud
description: Configure una conexión a SAP S/4HANA Cloud Public Edition en PlaidCloud para importar datos del balance de comprobación y de las partidas de asientos de diario mediante OData, y contabilizar asientos de diario mediante SOAP.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/s4hana-cloud.md
---

## Documentación de la API

La [API de balance de comprobación (`API_OPLACCTGDOCITEMCUBE_SRV`)](https://api.sap.com/) y la [API básica de partidas de asientos de diario (`API_JOURNALENTRYITEMBASIC_SRV`)](https://api.sap.com/) de SAP S/4HANA Cloud en SAP API Business Hub documentan los puntos de conexión OData que utiliza este conector, junto con el servicio SOAP de creación masiva de asientos de diario expuesto mediante un acuerdo de comunicación (Communication Arrangement).

## Cómo funciona la autenticación

La conexión se autentica como aplicación mediante **credenciales de cliente de OAuth2**: el ID de cliente y el secreto de un acuerdo de comunicación se intercambian por un token de acceso en el punto de conexión de token OAuth2 del inquilino. No hay inicio de sesión interactivo.

## Configuración

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| Host | Texto | El host de su inquilino de S/4HANA Cloud, por ejemplo `https://yourorg.s4hana.ondemand.com`. |
| URL del token | Texto | El punto de conexión de token OAuth2 del acuerdo de comunicación. |
| ID de cliente | Texto | El ID de cliente OAuth2 del acuerdo de comunicación. |
| Secreto de cliente | Texto | El secreto de cliente OAuth2 del acuerdo de comunicación. Se almacena cifrado. |

## Entidades disponibles para importar

El paso **Import S/4HANA Entity** abarca dos entidades: `trial_balance` (saldos agregados de las cuentas del libro mayor al cierre del período, mediante `API_OPLACCTGDOCITEMCUBE_SRV`) y `journal_entry_items` (partidas de asientos de diario contabilizados, mediante `API_JOURNALENTRYITEMBASIC_SRV`). Ambas admiten filtros del lado del servidor en `CompanyCode`, `GLAccount`, `CostCenter`, `ProfitCenter`, `FiscalYear`, `FiscalPeriod` y `Ledger`, y `PostingDate`, `FiscalYear` y `FiscalPeriod` aceptan límites de rango `ge`/`le`. Consulte [Import S/4HANA Entity](/es/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) (paso) para ver la referencia completa de campos.

## Contabilización de asientos de diario

El paso **S/4HANA: Post Journal Entry** contabiliza asientos de diario del libro mayor a través de la canalización de escritura de ERP compartida de PlaidCloud: envía la solicitud mediante el servicio SOAP `JournalEntryBulkCreateRequest_In` de S/4HANA Cloud, sondea la confirmación `JournalEntryBulkCreateConfirmation_Out` y confirma antes de notificar que un asiento está contabilizado. Una corrección contabiliza un nuevo asiento de reversión con el débito y el crédito intercambiados, en lugar de editar el original. Consulte [S/4HANA: Post Journal Entry](/es/reference/workflow-steps/s4hana-cloud/s4hana-post/) para ver la referencia de campos y [Conectarse a SAP S/4HANA Cloud](/es/guides/connections/s4hana-cloud/) para el tutorial completo de contabilización.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| Latencia de confirmación | El servicio SOAP de creación masiva procesa las solicitudes de forma asíncrona, por lo que es mucho más lento que una escritura OData síncrona del mismo tamaño. |
| Los campos filtrables dependen de su escenario de comunicación | Un objeto de costos o una dimensión que no expone su escenario de comunicación (Communication Scenario) no se puede filtrar en el servidor; limítelo en su flujo de trabajo después de la extracción. |
## Temas relacionados

- [Conectarse a SAP S/4HANA Cloud (guía)](/es/guides/connections/s4hana-cloud/) — paso a paso: crear la conexión, probarla, importar una entidad y contabilizar un diario.
- [Import S/4HANA Entity (paso)](/es/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/)
- [S/4HANA: Post Journal Entry](/es/reference/workflow-steps/s4hana-cloud/s4hana-post/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
- [Conector SAP ECC / S/4HANA](/es/reference/connectors/erp/sap-s4/) — el conector independiente, basado en RFC y agentes, para S/4HANA local o en nube privada.
