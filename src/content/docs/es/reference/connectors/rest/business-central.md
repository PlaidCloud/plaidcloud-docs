---
title: Conector REST de Business Central
description: Configure una conexión a Microsoft Dynamics 365 Business Central en PlaidCloud con credenciales de cliente de Azure AD para importar entidades OData y contabilizar líneas del diario general.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/business-central.md
---

## Documentación de la API

La [API OData v2.0 estándar](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/) de Business Central documenta las entidades y las opciones `$filter`/`$orderby` que utiliza este conector.

## Cómo funciona la autenticación

La conexión se autentica como aplicación mediante **credenciales de cliente (S2S)** de Entra ID (Azure AD): el ID de cliente y el secreto de un registro de aplicación se intercambian por un token de acceso en `https://login.microsoftonline.com/<tenant id>/oauth2/v2.0/token`, con el ámbito `https://api.businesscentral.dynamics.com/.default`. No hay inicio de sesión interactivo. El registro de aplicación necesita permisos de API concedidos a Business Central (`API.ReadWrite.All` o un ámbito más limitado que emita su administrador).

Cada solicitud se limita a un **entorno** (por ejemplo, `Production` o un entorno de pruebas) y a una **empresa** dentro de él; ambos se establecen en la conexión y no se eligen en cada solicitud.

## Configuración

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| ID de cliente | Texto | El ID de aplicación (cliente) del registro de aplicación de Entra. |
| Secreto de cliente | Texto | El secreto de cliente del registro de aplicación. Se almacena cifrado. |
| ID de inquilino | Texto | El ID de su inquilino de Azure AD. |
| Entorno | Texto | El nombre del entorno de Business Central, por ejemplo `Production`. |
| Empresa | Texto | El ID de la empresa de Business Central sobre la que esta conexión lee y contabiliza. |

## Entidades disponibles para importar

El paso **Import Business Central Entity** abarca seis entidades: `accounts`, `generalLedgerEntries`, `customers`, `vendors`, `items`, `journals`. Cada extracción admite filtros del lado del servidor por entidad. Consulte [Import Business Central Entity](/es/reference/workflow-steps/business-central/import-business-central-entity/) (paso) para ver la referencia completa de campos.

`generalLedgerEntries` es de solo lectura y solo contiene movimientos contabilizados: es la entidad que debe extraer para un balance de comprobación o el detalle del libro mayor, ya que nunca incluye una línea que todavía esté en un lote de diario sin contabilizar.

## Contabilización de líneas del diario general

El paso **Business Central Post** crea líneas dentro de un lote de diario **existente** y contabiliza ese lote a través de la canalización de escritura de ERP compartida de PlaidCloud; verifica que el lote contenga solo las líneas de esta solicitud antes de contabilizar y confirma la contabilización con `generalLedgerEntries` (no con el propio lote de diario). Consulte [Business Central: Post General Journal Lines](/es/reference/workflow-steps/business-central/business-central-post/) para ver la referencia de campos y [Conectarse a Business Central](/es/guides/connections/business-central/) para el tutorial completo de contabilización.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| Un solo tipo de documento de escritura | Solo se admite la contabilización de líneas del diario general. El flujo de documentos en borrador (facturas de venta y de compra, de Borrador a Contabilizado) no se admite, porque la acción de contabilización de ese flujo no está especificada en la documentación publicada de Microsoft. |
| Solo contabiliza en un lote existente | Este conector nunca crea un lote de diario en Business Central; créelo allí primero. |
| Contabilizaciones simultáneas en el mismo lote | La protección de idempotencia se limita por número de documento, no por lote de diario; no se garantiza que dos números de documento distintos que se contabilicen al mismo tiempo en el mismo lote se serialicen. |
## Temas relacionados

- [Conectarse a Business Central (guía)](/es/guides/connections/business-central/) — paso a paso: crear la conexión, probarla, importar una entidad y contabilizar un diario.
- [Import Business Central Entity (paso)](/es/reference/workflow-steps/business-central/import-business-central-entity/)
- [Business Central: Post General Journal Lines](/es/reference/workflow-steps/business-central/business-central-post/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
