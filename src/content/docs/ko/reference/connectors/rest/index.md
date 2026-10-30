---
title: REST 연결
description: Salesforce, NetSuite, Workday, Dynamics 등 클라우드 기반 플랫폼의 REST API 서비스에 PlaidCloud를 연결합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/index.md
---

PlaidCloud는 표준 인증 방식(OAuth, API 키, Basic 인증)을 사용하여 REST API 서비스에 연결합니다. 제공자마다 토큰 흐름, 범위 처리, 페이지 나누기에 고유한 특성이 있으며, 아래의 전용 커넥터가 이러한 세부 사항을 캡슐화하므로 직접 다룰 필요가 없습니다.

전용 커넥터가 없는 REST 서비스를 위해 PlaidCloud는 대부분의 인증 및 응답 파싱 방식에 맞게 구성할 수 있는 범용 REST 커넥터를 제공합니다.

## 범용 커넥터

- [범용 REST 연결](/ko/reference/connectors/rest/generic-rest/) — None/Basic/API 키/Bearer/OAuth 2.0 인증, 기본 헤더, 리디렉션 처리, 요청 테스트를 포함해 모든 HTTP API를 구성합니다.

## CRM 및 영업

- [Salesforce](/ko/reference/connectors/rest/salesforce/)
- [Dynamics](/ko/reference/connectors/rest/dynamics/) — Microsoft Dynamics 365

## 재무 및 회계

- [NetSuite](/ko/reference/connectors/rest/netsuite/)
- [HFM / FCCS](/ko/reference/connectors/rest/hfm-fccs/) — Oracle EPM Cloud(Financial Consolidation and Close)
- [TM1](/ko/reference/connectors/rest/tm1/) — IBM TM1 / Planning Analytics
- [Acumatica](/ko/reference/connectors/rest/acumatica/)
- [Business Central](/ko/reference/connectors/rest/business-central/)
- [Dynamics 365 Finance & Operations](/ko/reference/connectors/rest/dynamics-365-fo/)
- [Workday Financials](/ko/reference/connectors/rest/workday-financials/)
- [SAP S/4HANA Cloud](/ko/reference/connectors/rest/s4hana-cloud/)
- [QuickBooks](/ko/reference/connectors/rest/quickbooks/)
- [Xero](/ko/reference/connectors/rest/xero/)
- [Sage Intacct](/ko/reference/connectors/rest/sage-intacct/)
- [Stripe](/ko/reference/connectors/rest/stripe/)
- [Ramp](/ko/reference/connectors/rest/ramp/)

## HR 및 급여

- [Workday](/ko/reference/connectors/rest/workday/)
- [Paycor](/ko/reference/connectors/rest/paycor/)
- [Gusto](/ko/reference/connectors/rest/gusto/)

## 통합 플랫폼

- [MuleSoft](/ko/reference/connectors/rest/mulesoft/)
