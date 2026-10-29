---
title: Connexions REST
description: Connectez PlaidCloud à des services d'API REST, dont Salesforce, NetSuite, Workday, Dynamics et d'autres plateformes cloud.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

PlaidCloud se connecte à des services d'API REST à l'aide de schémas d'authentification standard (OAuth, clés d'API, Basic Auth). Chaque fournisseur a ses particularités en matière de flux de jetons, de gestion des portées et de pagination ; les connecteurs dédiés ci-dessous encapsulent ces spécificités pour vous éviter d'avoir à les gérer.

Pour tout service REST qui n'a pas de connecteur dédié, PlaidCloud propose un connecteur REST générique configurable pour la plupart des schémas d'authentification et d'analyse de réponses.

## Connecteur générique

- [Connexion REST générique](/fr/reference/connectors/rest/generic-rest/) — configurez n'importe quelle API HTTP : authentification None/Basic/API Key/Bearer/OAuth 2.0, en-têtes par défaut, gestion des redirections et test des requêtes.

## CRM et ventes

- [Salesforce](/fr/reference/connectors/rest/salesforce/)
- [Dynamics](/fr/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## Finance et comptabilité

- [NetSuite](/fr/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/fr/reference/connectors/rest/hfm-fccs/) — Oracle EPM Cloud (Financial Consolidation and Close)
- [TM1](/fr/reference/connectors/rest/tm1/) — IBM TM1 / Planning Analytics
- [Acumatica](/fr/reference/connectors/rest/acumatica/)
- [Business Central](/fr/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/fr/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/fr/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/fr/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/fr/reference/connectors/rest/quickbooks/)
- [Xero](/fr/reference/connectors/rest/xero/)
- [Sage Intacct](/fr/reference/connectors/rest/sage-intacct/)
- [Stripe](/fr/reference/connectors/rest/stripe/)
- [Ramp](/fr/reference/connectors/rest/ramp/)

## RH et paie

- [Workday](/fr/reference/connectors/rest/workday/)
- [Paycor](/fr/reference/connectors/rest/paycor/)
- [Gusto](/fr/reference/connectors/rest/gusto/)

## Plateformes d'intégration

- [MuleSoft](/fr/reference/connectors/rest/mulesoft/)
