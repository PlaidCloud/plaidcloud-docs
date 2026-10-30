---
title: Ligações REST
description: Ligue o PlaidCloud a serviços de API REST, incluindo Salesforce, NetSuite, Workday, Dynamics e outras plataformas na nuvem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

O PlaidCloud liga-se a serviços de API REST através de padrões de autenticação comuns (OAuth, chaves de API, autenticação básica). Cada fornecedor tem as suas particularidades no fluxo de tokens, na gestão de âmbitos e na paginação — os conectores dedicados abaixo encapsulam esses detalhes para que não tenha de se preocupar com eles.

Para qualquer serviço REST que não tenha um conector dedicado, o PlaidCloud disponibiliza um conector REST genérico configurável para a maioria dos padrões de autenticação e de análise de respostas.

## Conector genérico

- [Ligação REST genérica](/pt-pt/reference/connectors/rest/generic-rest/) — configure qualquer API HTTP: autenticação Nenhuma/Básica/Chave de API/Portador/OAuth 2.0, cabeçalhos predefinidos, tratamento de redirecionamentos e teste de pedidos.

## CRM e vendas

- [Salesforce](/pt-pt/reference/connectors/rest/salesforce/)
- [Dynamics](/pt-pt/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## Finanças e contabilidade

- [NetSuite](/pt-pt/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/pt-pt/reference/connectors/rest/hfm-fccs/) — Oracle EPM Cloud (Financial Consolidation and Close)
- [TM1](/pt-pt/reference/connectors/rest/tm1/) — IBM TM1 / Planning Analytics
- [Acumatica](/pt-pt/reference/connectors/rest/acumatica/)
- [Business Central](/pt-pt/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/pt-pt/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/pt-pt/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/pt-pt/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/pt-pt/reference/connectors/rest/quickbooks/)
- [Xero](/pt-pt/reference/connectors/rest/xero/)
- [Sage Intacct](/pt-pt/reference/connectors/rest/sage-intacct/)
- [Stripe](/pt-pt/reference/connectors/rest/stripe/)
- [Ramp](/pt-pt/reference/connectors/rest/ramp/)

## RH e processamento salarial

- [Workday](/pt-pt/reference/connectors/rest/workday/)
- [Paycor](/pt-pt/reference/connectors/rest/paycor/)
- [Gusto](/pt-pt/reference/connectors/rest/gusto/)

## Plataformas de integração

- [MuleSoft](/pt-pt/reference/connectors/rest/mulesoft/)
