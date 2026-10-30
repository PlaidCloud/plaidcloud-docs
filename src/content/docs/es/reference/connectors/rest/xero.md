---
title: Conector REST de Xero
description: Configure una conexión de Xero en PlaidCloud con una autorización OAuth de un clic, importe entidades de la API de contabilidad y contabilice asientos manuales, facturas, facturas de proveedor, pagos y notas de crédito.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/xero.md
---

## Documentación de la API

La [referencia de la API de contabilidad](https://developer.xero.com/documentation/api/accounting/overview) de Xero documenta las entidades, los filtros `where=` y las cargas útiles de creación que utiliza este conector.

## Cómo funciona la autenticación

La conexión se autentica con la concesión **OAuth 2.0** de Xero. PlaidCloud registra la aplicación OAuth por sí mismo, por lo que no hay ningún identificador de cliente ni secreto de cliente que obtener o introducir: usted hace clic en **Conectar con Xero**, inicia sesión en Xero y aprueba la concesión. PlaidCloud almacena los tokens resultantes en la conexión y los actualiza por usted, conservando cada token de actualización rotado para que una conexión inactiva durante mucho tiempo siga funcionando.

Una concesión abarca todas las organizaciones de Xero para las que la apruebe. La conexión apunta exactamente a una de ellas: el selector **Organización** muestra las organizaciones que devolvió la concesión, y cada solicitud lleva el identificador de tenant de esa organización. Para leer o contabilizar en una segunda organización, cree una segunda conexión de Xero y elija esa organización en ella.

La Demo Company de Xero es una propiedad de la organización, no un ajuste de la conexión: una organización de demostración aparece en la lista **Organización** como cualquier otra, de modo que una conexión de pruebas es la que apunta a ella.

## Configuración

| Campo | Tipo | Descripción |
|---|---|---|
| Nombre | Texto | Nombre para mostrar de esta conexión. |
| Conectar con Xero | Botón | Inicia el flujo de inicio de sesión y consentimiento de Xero. |
| Estado de la conexión | Estado | Muestra `Not connected` hasta que se completa la concesión y, después, indica a cuántas organizaciones abarca. |
| Organización | Selección | La organización de Xero con la que esta conexión lee y contabiliza. Se completa a partir de la concesión. |

## Límites de velocidad

Xero limita cada organización a 60 llamadas por minuto y 5000 llamadas por día, con un tope de 5 llamadas simultáneas. PlaidCloud regula por conexión los límites por minuto y de simultaneidad, de modo que la limitación de una organización nunca detiene las llamadas de otra conexión, y respeta el `Retry-After` de Xero en una respuesta limitada. El tope diario queda a su cargo: programe las extracciones amplias en lugar de ejecutar muchas a la vez.

## Entidades disponibles para importar

El paso **Xero: importar entidad** cubre once entidades de la API de contabilidad: `accounts`, `contacts`, `invoices`, `credit_notes`, `payments`, `manual_journals`, `bank_transactions`, `items`, `tracking_categories`, `tax_rates` y `currencies`. Cada extracción admite opcionalmente un filtro de estado, un intervalo de fechas y una fecha límite de modificación. Consulte [Xero: importar entidad](/es/reference/workflow-steps/xero/import-xero-entity/) para ver la referencia completa de campos.

## Contabilización de documentos

El paso **Xero: contabilizar documento** contabiliza asientos manuales, facturas, facturas de proveedor, pagos y notas de crédito a través de la canalización de escritura de ERP compartida de PlaidCloud, a partir de una tabla de encabezados y una tabla de líneas. Consulte [Xero: contabilizar documento](/es/reference/workflow-steps/xero/xero-post/) para ver la referencia de campos y [Conectar con Xero](/es/guides/connections/xero/) para ver el tutorial completo de contabilización.

## Limitaciones conocidas

| Limitación | Qué significa |
|---|---|
| Los asientos manuales y los pagos no se pueden consultar tras un resultado ambiguo | Las facturas, las facturas de proveedor y las notas de crédito llevan un número de documento que PlaidCloud asigna y que puede consultar de vuelta. La narración de un asiento manual y la referencia de un pago no se pueden consultar, por lo que una escritura dudosa de cualquiera de los dos se pone en cuarentena para que usted la resuelva en Xero en lugar de adivinar. |
| La reversión cubre solo asientos manuales y facturas | Un asiento manual se revierte como un asiento con débito y crédito intercambiados; una factura se revierte como una nota de crédito espejo. Las facturas de proveedor, los pagos y las notas de crédito no tienen una carga útil de deshacer documentada, por lo que PlaidCloud rechaza una reversión en lugar de inventarla. |
| Los filtros son campos fijos, no un lenguaje de consulta | La API de consultas de Xero expone un filtro de estado y un intervalo de fechas por entidad, no un lenguaje de filtrado abierto, por lo que el paso de importación ofrece esos campos en lugar de una tabla de campo, operador y valor. |
| Una organización por conexión | Cada solicitud lleva un identificador de tenant. Una segunda organización necesita una segunda conexión. |

## Información relacionada

- [Conectar con Xero (guía)](/es/guides/connections/xero/): paso a paso: cree la conexión, pruébela, importe una entidad y contabilice un documento.
- [Xero: importar entidad](/es/reference/workflow-steps/xero/import-xero-entity/)
- [Xero: contabilizar documento](/es/reference/workflow-steps/xero/xero-post/)
- [Revisar el historial de contabilizaciones de ERP](/es/guides/connections/erp-post-history/)
