---
title: Conexiones REST
description: Conecte PlaidCloud a servicios de API REST, incluidos Salesforce, NetSuite, Workday, Dynamics y otras plataformas basadas en la nube.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

PlaidCloud se conecta a servicios de API REST mediante patrones de autenticación estándar (OAuth, claves de API, autenticación básica). Cada proveedor tiene sus propias particularidades en el flujo de tokens, el manejo de ámbitos y la paginación; los conectores específicos que se indican a continuación encapsulan esos detalles para que usted no tenga que ocuparse de ellos.

Para cualquier servicio REST que no tenga un conector específico, PlaidCloud ofrece un conector REST genérico que se puede configurar para la mayoría de los patrones de autenticación y análisis de respuestas.

## Conector genérico

- [Conexión REST genérica](/es/reference/connectors/rest/generic-rest/) — configure cualquier API HTTP: autenticación None/Basic/API Key/Bearer/OAuth 2.0, encabezados predeterminados, manejo de redirecciones y pruebas de solicitudes.

## CRM y ventas

- [Salesforce](/es/reference/connectors/rest/salesforce/)
- [Dynamics](/es/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## Finanzas y contabilidad

- [NetSuite](/es/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/es/reference/connectors/rest/hfm-fccs/) — Oracle EPM Cloud (Financial Consolidation and Close)
- [TM1](/es/reference/connectors/rest/tm1/) — IBM TM1 / Planning Analytics
- [Acumatica](/es/reference/connectors/rest/acumatica/)
- [Business Central](/es/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/es/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/es/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/es/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/es/reference/connectors/rest/quickbooks/)
- [Xero](/es/reference/connectors/rest/xero/)
- [Sage Intacct](/es/reference/connectors/rest/sage-intacct/)
- [Stripe](/es/reference/connectors/rest/stripe/)
- [Ramp](/es/reference/connectors/rest/ramp/)

## Recursos humanos y nómina

- [Workday](/es/reference/connectors/rest/workday/)
- [Paycor](/es/reference/connectors/rest/paycor/)
- [Gusto](/es/reference/connectors/rest/gusto/)

## Plataformas de integración

- [MuleSoft](/es/reference/connectors/rest/mulesoft/)
