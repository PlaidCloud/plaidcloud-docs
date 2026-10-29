---
title: Połączenia REST
description: Połącz PlaidCloud z usługami REST API, w tym Salesforce, NetSuite, Workday, Dynamics i innymi platformami chmurowymi.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

PlaidCloud łączy się z usługami REST API przy użyciu standardowych wzorców uwierzytelniania (OAuth, klucze API, uwierzytelnianie podstawowe). Każdy dostawca ma własną specyfikę przepływu tokenów, obsługi zakresów i stronicowania — dedykowane konektory wymienione poniżej ukrywają te szczegóły, abyś nie musiał się nimi zajmować.

Dla każdej usługi REST, która nie ma dedykowanego konektora, PlaidCloud udostępnia ogólny konektor REST, który można skonfigurować dla większości wzorców uwierzytelniania i analizy odpowiedzi.

## Konektor ogólny

- [Ogólne połączenie REST](/pl/reference/connectors/rest/generic-rest/) — skonfiguruj dowolny interfejs HTTP API: uwierzytelnianie None/Basic/API Key/Bearer/OAuth 2.0, domyślne nagłówki, obsługę przekierowań i testowanie żądań.

## CRM i sprzedaż

- [Salesforce](/pl/reference/connectors/rest/salesforce/)
- [Dynamics](/pl/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## Finanse i księgowość

- [NetSuite](/pl/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/pl/reference/connectors/rest/hfm-fccs/) — Oracle EPM Cloud (Financial Consolidation and Close)
- [TM1](/pl/reference/connectors/rest/tm1/) — IBM TM1 / Planning Analytics
- [Acumatica](/pl/reference/connectors/rest/acumatica/)
- [Business Central](/pl/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/pl/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/pl/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/pl/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/pl/reference/connectors/rest/quickbooks/)
- [Xero](/pl/reference/connectors/rest/xero/)
- [Sage Intacct](/pl/reference/connectors/rest/sage-intacct/)
- [Stripe](/pl/reference/connectors/rest/stripe/)
- [Ramp](/pl/reference/connectors/rest/ramp/)

## HR i płace

- [Workday](/pl/reference/connectors/rest/workday/)
- [Paycor](/pl/reference/connectors/rest/paycor/)
- [Gusto](/pl/reference/connectors/rest/gusto/)

## Platformy integracyjne

- [MuleSoft](/pl/reference/connectors/rest/mulesoft/)
