---
title: Conector REST de Acumatica
description: Configure una conexión a la API REST basada en contratos de Acumatica en PlaidCloud para importar datos maestros y transaccionales y contabilizar transacciones de diario, facturas, facturas de proveedor y pagos.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/acumatica.md
---

## Documentación de la API

La [API REST basada en contratos](https://help.acumatica.com/Help?ScreenId=ShowWiki&pageid=e0dea52d-0339-4f34-a6c0-9615ce6a25c2) de Acumatica documenta los puntos de conexión y las opciones de consulta que utiliza este conector.

## Cómo funciona la autenticación

La conexión se basa en **sesiones**: PlaidCloud inicia sesión una vez por unidad de trabajo acotada (`POST <instance>/entity/auth/login` con su nombre de usuario, contraseña, empresa y sucursal opcional) y reutiliza la cookie de sesión resultante en cada llamada de esa unidad, cerrando la sesión al terminar. No es un flujo de token de portador ni de OAuth: las sesiones cuentan para el límite de sesiones simultáneas de su licencia de Acumatica, que las instancias de prueba y de nivel inferior pueden limitar a tan solo 2, así que evite ejecutar muchos pasos de Acumatica en paralelo en una misma conexión.

## Configuración

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| URL base de la instancia | Texto | La URL de su instancia de Acumatica, por ejemplo `https://yourcompany.acumatica.com`. |
| Nombre del punto de conexión | Texto | El nombre del punto de conexión del contrato. `Default`, a menos que se haya publicado un punto de conexión personalizado. |
| Versión del punto de conexión | Texto | Opcional, por ejemplo `25.200.001`. Déjelo en blanco para usar la última versión publicada del punto de conexión. |
| Empresa / Inquilino | Texto | El ID exacto de la empresa de Acumatica en la que inicia sesión esta conexión. |
| Sucursal | Texto | Opcional. Déjelo en blanco para usar la sucursal predeterminada del usuario que inicia sesión. |
| Nombre de usuario | Texto | El nombre de usuario del usuario de API de PlaidCloud. |
| Contraseña | Texto | La contraseña del usuario de API de PlaidCloud. Se almacena cifrada. |

## Entidades disponibles para importar

El paso **Import Acumatica Entity** abarca 18 entidades basadas en contratos:

**Datos maestros y de referencia** — `account`, `subaccount`, `ledger`, `financial_period`, `branch`, `currency`, `currency_rate`, `customer`, `vendor`, `stock_item`, `warehouse`, `employee`, `tax_category`, `project`

**Datos transaccionales** — `sales_invoice`, `bill`, `sales_order`, `shipment`

Cada extracción admite un interruptor `Active Only`, un límite `Updated After` y filtros del lado del servidor por entidad. Consulte [Import Acumatica Entity](/es/reference/workflow-steps/acumatica/import-acumatica-entity/) (paso) para ver la referencia completa de campos.

## Contabilización de documentos

El paso **Acumatica Post** contabiliza documentos **JournalTransaction**, **SalesInvoice**, **Bill** y **Payment** a través de la canalización de escritura de ERP compartida de PlaidCloud: crea el documento en espera, lo libera (una acción asíncrona) y confirma la liberación antes de notificar que un documento está contabilizado. Consulte [Acumatica: Post Documents](/es/reference/workflow-steps/acumatica/acumatica-post/) para ver la referencia de campos y [Conectarse a Acumatica](/es/guides/connections/acumatica/) para el tutorial completo de contabilización.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| No se cubren las lecturas que dependen de GI | El balance de comprobación, el detalle de transacciones del libro mayor, las existencias disponibles, los presupuestos y los datos entre empresas se encuentran detrás de las consultas genéricas (Generic Inquiries, GI) de Acumatica, no de las 18 entidades basadas en contratos indicadas arriba. Cree la GI en Acumatica y extráigala con una [conexión REST genérica](/es/reference/connectors/rest/generic-rest/). |
| Sin clave de idempotencia nativa en la escritura | La API de escritura de Acumatica basada en PUT no tiene un campo de idempotencia; la reserva propia de PlaidCloud en su libro de registro es la única protección contra una doble contabilización. |
| La reversión es manual | Ningún tipo de documento tiene una acción documentada de anulación o reversión. Un documento contabilizado no se puede revertir desde PlaidCloud; corríjalo directamente en Acumatica. |
| Sin campo de correlación de Payment | Acumatica no expone ningún campo documentado para correlacionar un Payment con la solicitud de PlaidCloud tras un resultado ambiguo; un Payment en duda se pone en cuarentena para su resolución manual. |
| El filtrado de líneas no se hace en el servidor | Los filtros de estilo `$filter` llegan a los campos de la entidad y del encabezado, no a las dimensiones de las líneas de un documento (por ejemplo, un centro de costos a nivel de línea). Limite las líneas en su flujo de trabajo después de la extracción. |
## Temas relacionados

- [Conectarse a Acumatica (guía)](/es/guides/connections/acumatica/) — paso a paso: crear la conexión, probarla, importar una entidad y contabilizar un lote.
- [Import Acumatica Entity (paso)](/es/reference/workflow-steps/acumatica/import-acumatica-entity/)
- [Acumatica: Post Documents](/es/reference/workflow-steps/acumatica/acumatica-post/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
