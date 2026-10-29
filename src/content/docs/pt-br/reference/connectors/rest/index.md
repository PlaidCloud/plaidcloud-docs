---
title: Conexões REST
description: Conecte o PlaidCloud a serviços de API REST, incluindo Salesforce, NetSuite, Workday, Dynamics e outras plataformas em nuvem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

O PlaidCloud se conecta a serviços de API REST usando padrões de autenticação comuns (OAuth, chaves de API, Basic Auth). Cada provedor tem suas particularidades de fluxo de token, tratamento de escopo e paginação; os conectores dedicados abaixo encapsulam esses detalhes para que você não precise lidar com eles.

Para qualquer serviço REST que não tenha um conector dedicado, o PlaidCloud oferece um conector REST genérico que pode ser configurado para a maioria dos padrões de autenticação e de análise de respostas.

## Conector genérico

- [Conexão REST genérica](/pt-br/reference/connectors/rest/generic-rest/) — configure qualquer API HTTP: autenticação None/Basic/API Key/Bearer/OAuth 2.0, cabeçalhos padrão, tratamento de redirecionamentos e teste de solicitações.

## CRM e vendas

- [Salesforce](/pt-br/reference/connectors/rest/salesforce/)
- [Dynamics](/pt-br/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## Finanças e contabilidade

- [NetSuite](/pt-br/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/pt-br/reference/connectors/rest/hfm-fccs/) — Oracle EPM Cloud (Financial Consolidation and Close)
- [TM1](/pt-br/reference/connectors/rest/tm1/) — IBM TM1 / Planning Analytics
- [Acumatica](/pt-br/reference/connectors/rest/acumatica/)
- [Business Central](/pt-br/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/pt-br/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/pt-br/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/pt-br/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/pt-br/reference/connectors/rest/quickbooks/)
- [Xero](/pt-br/reference/connectors/rest/xero/)
- [Sage Intacct](/pt-br/reference/connectors/rest/sage-intacct/)
- [Stripe](/pt-br/reference/connectors/rest/stripe/)
- [Ramp](/pt-br/reference/connectors/rest/ramp/)

## RH e folha de pagamento

- [Workday](/pt-br/reference/connectors/rest/workday/)
- [Paycor](/pt-br/reference/connectors/rest/paycor/)
- [Gusto](/pt-br/reference/connectors/rest/gusto/)

## Plataformas de integração

- [MuleSoft](/pt-br/reference/connectors/rest/mulesoft/)
