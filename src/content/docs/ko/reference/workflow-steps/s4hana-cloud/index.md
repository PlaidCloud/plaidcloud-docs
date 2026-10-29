---
title: SAP S/4HANA Cloud 단계
description: S/4HANA Cloud 연결을 통해 SAP S/4HANA Cloud Public Edition에서 읽고 쓰는 워크플로 단계입니다. 시산표와 분개 전표 항목을 가져오고 분개 전표를 전기합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/s4hana-cloud/index.md
---

[S/4HANA Cloud 연결](/ko/guides/connections/s4hana-cloud/)을 통해 SAP S/4HANA Cloud Public Edition에서 읽고 쓰는 워크플로 단계입니다. 가져오기 단계는 OData를 작성하지 않고도 시산표 또는 분개 전표 항목 데이터를 가져오며, 전기 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 분개 전표를 전기합니다.

## 단계

- [Import S/4HANA Entity](/ko/reference/workflow-steps/s4hana-cloud/import-s4hana-entity/) 단계 — 서버 측 필터를 지원하는 시산표 및 분개 전표 항목 데이터.
- [S/4HANA: Post Journal Entry](/ko/reference/workflow-steps/s4hana-cloud/s4hana-post/) 단계 — SOAP으로 분개 전표를 전기하며, 정정이 필요하면 전기된 역분개 전표를 사용합니다.

## 관련 항목

- [SAP S/4HANA Cloud REST 커넥터](/ko/reference/connectors/rest/s4hana-cloud/)
- [SAP S/4HANA Cloud에 연결](/ko/guides/connections/s4hana-cloud/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
