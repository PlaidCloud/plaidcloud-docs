---
title: Dynamics 365 F&O 단계
description: D365 F&O 연결을 통해 Dynamics 365 Finance & Operations에서 읽고 쓰는 워크플로 단계로, OData/DMF 엔터티를 가져오고 분개 전표를 전기합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dynamics-365-fo/index.md
---

[D365 F&O 연결](/ko/guides/connections/dynamics-365-fo/)을 통해 Dynamics 365 Finance & Operations(D365 F&O)에서 읽고 쓰는 워크플로 단계입니다. 가져오기 단계는 OData를 작성할 필요 없이 OData 엔터티나 대량 DMF 추출을 가져오고, 전기 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 총계정원장 분개 전표를 전기합니다.

## 단계

- [Import D365 F&O Entity 단계](/ko/reference/workflow-steps/dynamics-365-fo/import-d365fo-entity/) — OData 또는 DMF 대량 모드로 마스터 데이터와 분개 헤더를 가져오며 서버 측 필터를 지원합니다.
- [D365 F&O: Post Journal Entry 단계](/ko/reference/workflow-steps/dynamics-365-fo/dynamics-365-fo-post/) — 총계정원장 분개 전표를 전기하며, 정정은 전기된 역분개 전표로 처리합니다.

## 관련 항목

- [Dynamics 365 F&O REST 커넥터](/ko/reference/connectors/rest/dynamics-365-fo/)
- [Dynamics 365 Finance & Operations에 연결](/ko/guides/connections/dynamics-365-fo/)
- [ERP 전기 내역 검토](/ko/guides/connections/erp-post-history/)
