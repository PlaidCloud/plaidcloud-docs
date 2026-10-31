---
title: Workday Financials 단계
description: Workday Financials 연결을 통해 Workday Financials에서 읽고 쓰는 워크플로 단계 — RaaS 보고서를 통한 데이터 가져오기와 회계 분개 전기.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workday-financials/index.md
---

[Workday Financials 연결](/ko/guides/connections/workday-financials/)을 통해 Workday Financials에서 읽고 쓰는 워크플로 단계입니다. 가져오기 단계는 고객이 제공한 Report-as-a-Service(RaaS) 보고서를 가져오고, 전기 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 회계 분개를 전기합니다.

## 단계

- [Import Workday Entity 단계](/ko/reference/workflow-steps/workday-financials/import-workday-entity/) — 보고서 매개변수 필터와 함께 RaaS 보고서를 가져옵니다.
- [Workday Financials: Post Journal Entry 단계](/ko/reference/workflow-steps/workday-financials/workday-post/) — `Submit_Accounting_Journal`을 통해 회계 분개를 전기하며, 수정에는 전기된 역분개를 사용합니다.

## 관련 항목

- [Workday Financials Connector](/ko/reference/connectors/rest/workday-financials/)
- [Connect to Workday Financials](/ko/guides/connections/workday-financials/)
- [Review ERP Post History](/ko/guides/connections/erp-post-history/)
