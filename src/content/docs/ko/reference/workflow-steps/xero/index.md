---
title: Xero 단계
description: Xero 연결을 통해 Xero에서 읽고 쓰는 워크플로 단계입니다. Accounting API 엔터티를 가져오고, 수동 분개, 송장, 청구서, 결제, 대변 메모를 전기합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/xero/index.md
---

[Xero 연결](/ko/guides/connections/xero/)을 통해 Xero에서 읽고 쓰는 워크플로 단계입니다. 가져오기 단계는 작성할 쿼리 없이 Xero의 Accounting API 엔터티를 가져오고, 전기 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 수동 분개, 송장, 청구서, 결제, 대변 메모를 전기합니다.

## 단계

- [Xero: 엔터티 가져오기](/ko/reference/workflow-steps/xero/import-xero-entity/) — 계정, 연락처, 송장, 대변 메모, 결제, 수동 분개, 은행 거래, 항목, 추적 범주, 세율, 통화.
- [Xero: 문서 전기](/ko/reference/workflow-steps/xero/xero-post/) — 수동 분개, 송장, 청구서, 결제, 대변 메모를 전기합니다.

## 관련 항목

- [Xero REST 커넥터](/ko/reference/connectors/rest/xero/)
- [Xero에 연결](/ko/guides/connections/xero/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
