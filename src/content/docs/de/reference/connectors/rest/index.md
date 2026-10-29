---
title: REST-Verbindungen
description: Verbinden Sie PlaidCloud mit REST-API-Diensten wie Salesforce, NetSuite, Workday, Dynamics und anderen Cloud-Plattformen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

PlaidCloud verbindet sich mit REST-API-Diensten über Standardmuster der Authentifizierung (OAuth, API-Schlüssel, Basic Auth). Jeder Anbieter hat seine Eigenheiten bei Token-Ablauf, Geltungsbereichen und Paginierung – die folgenden dedizierten Konnektoren kapseln diese Besonderheiten, sodass Sie sich nicht darum kümmern müssen.

Für jeden REST-Dienst ohne dedizierten Konnektor bietet PlaidCloud einen generischen REST-Konnektor, der sich auf die meisten Muster der Authentifizierung und Antwortverarbeitung konfigurieren lässt.

## Generischer Konnektor

- [Generische REST-Verbindung](/de/reference/connectors/rest/generic-rest/) – konfigurieren Sie jede HTTP-API: Authentifizierung mit None/Basic/API Key/Bearer/OAuth 2.0, Standard-Header, Umgang mit Weiterleitungen und Anfragetests.

## CRM und Vertrieb

- [Salesforce](/de/reference/connectors/rest/salesforce/)
- [Dynamics](/de/reference/connectors/rest/dynamics/) – Microsoft Dynamics 365

## Finanzen und Buchhaltung

- [NetSuite](/de/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/de/reference/connectors/rest/hfm-fccs/) – Oracle EPM Cloud (Financial Consolidation and Close)
- [TM1](/de/reference/connectors/rest/tm1/) – IBM TM1 / Planning Analytics
- [Acumatica](/de/reference/connectors/rest/acumatica/)
- [Business Central](/de/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/de/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/de/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/de/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/de/reference/connectors/rest/quickbooks/)
- [Xero](/de/reference/connectors/rest/xero/)
- [Sage Intacct](/de/reference/connectors/rest/sage-intacct/)
- [Stripe](/de/reference/connectors/rest/stripe/)
- [Ramp](/de/reference/connectors/rest/ramp/)

## Personal und Gehaltsabrechnung

- [Workday](/de/reference/connectors/rest/workday/)
- [Paycor](/de/reference/connectors/rest/paycor/)
- [Gusto](/de/reference/connectors/rest/gusto/)

## Integrationsplattformen

- [MuleSoft](/de/reference/connectors/rest/mulesoft/)
