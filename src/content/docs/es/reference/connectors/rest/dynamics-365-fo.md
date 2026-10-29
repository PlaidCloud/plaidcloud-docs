---
title: Conector REST de Dynamics 365 Finance & Operations
description: Configure una conexión a Dynamics 365 Finance & Operations en PlaidCloud para importar entidades OData/DMF y contabilizar asientos de diario de forma asíncrona.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/dynamics-365-fo.md
---

## Documentación de la API

Los [puntos de conexión OData v4](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/odata) y el [Data Management Framework](https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/data-management-import-export) de D365 F&O documentan los puntos de conexión y la ruta de extracción masiva que utiliza este conector.

## Cómo funciona la autenticación

La conexión se autentica como aplicación mediante **credenciales de cliente** de Entra ID (Azure AD): el ID de cliente y el secreto de un registro de aplicación se intercambian por un token de acceso, con el ámbito del recurso del entorno. No hay inicio de sesión interactivo.

## Configuración

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| URL del entorno | Texto | La URL de su entorno de D365 F&O, por ejemplo `https://yourorg.operations.dynamics.com`. |
| ID de cliente | Texto | El ID de aplicación (cliente) del registro de aplicación de Entra. |
| Secreto de cliente | Texto | El secreto de cliente del registro de aplicación. Se almacena cifrado. |
| ID de inquilino | Texto | El ID de su inquilino de Azure AD. |
| Recurso/Ámbito | Texto | El ámbito de OAuth2 solicitado, normalmente la URL del entorno más `/.default`. |

## Entidades disponibles para importar

El paso **Import D365 F&O Entity** abarca seis entidades: `main_accounts`, `currencies`, `customers`, `vendors`, `released_products`, `ledger_journal_headers`. Cada extracción se ejecuta en modo de sincronización `odata` (una llamada directa, para extracciones rutinarias) o en modo masivo `dmf` (un trabajo de exportación asíncrono del Data Management Framework, para extracciones grandes), y admite filtros del lado del servidor por entidad, incluidos rangos de fechas, cuentas y dimensiones. Consulte [Import D365 F&O Entity](/es/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) (paso) para ver la referencia completa de campos.

## Contabilización de asientos de diario

El paso **D365 F&O: Post Journal Entry** contabiliza asientos de diario del libro mayor a través de la canalización de escritura de ERP compartida de PlaidCloud: envía la solicitud a la acción asíncrona de contabilización de diarios del servicio personalizado de D365 F&O, consulta su estado hasta que llega a un estado terminal y confirma antes de notificar que un asiento está contabilizado. Una corrección contabiliza un nuevo asiento de reversión con el débito y el crédito intercambiados, en lugar de editar el original. Consulte [D365 F&O: Post Journal Entry](/es/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) para ver la referencia de campos y [Conectarse a Dynamics 365 Finance & Operations](/es/guides/connections/dynamics-365-fo/) para el tutorial completo de contabilización.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| El modo de sincronización DMF tiene latencia de extracción | Una extracción `dmf` espera un trabajo de exportación asíncrono, por lo que es mucho más lenta que una extracción `odata` del mismo tamaño. |
| El filtrado por dimensión depende de la estructura | Una dimensión financiera que no forma parte de su estructura de cuentas no se puede filtrar en el servidor; limítela en su flujo de trabajo después de la extracción. |
## Temas relacionados

- [Conectarse a Dynamics 365 Finance & Operations (guía)](/es/guides/connections/dynamics-365-fo/) — paso a paso: crear la conexión, probarla, importar una entidad y contabilizar un diario.
- [Import D365 F&O Entity (paso)](/es/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/)
- [D365 F&O: Post Journal Entry](/es/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
