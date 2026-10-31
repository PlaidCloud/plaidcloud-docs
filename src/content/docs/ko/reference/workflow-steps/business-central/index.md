---
title: Business Central 단계
description: Business Central 연결을 통해 Microsoft Dynamics 365 Business Central에서 읽고 쓰는 워크플로 단계입니다. OData 엔터티를 가져오고 일반 분개장 라인을 전기합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/business-central/index.md
---

[Business Central 연결](/ko/guides/connections/business-central/)을 통해 Business Central에서 읽고 쓰는 워크플로 단계입니다. 가져오기 단계는 쿼리를 작성하지 않고 Business Central의 표준 OData v2.0 엔터티를 가져오며, 전기 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 일반 분개장 라인을 전기합니다.

## 단계

- [Import Business Central Entity 단계](/ko/reference/workflow-steps/business-central/import-business-central-entity/) — 계정, 원장 항목, 고객, 공급업체, 품목, 분개장을 서버 측 필터로 가져옵니다.
- [Business Central: Post General Journal Lines 단계](/ko/reference/workflow-steps/business-central/business-central-post/) — 기존 분개장 배치에 라인을 입력하고 배치를 전기합니다.

## 관련 항목

- [Business Central REST 커넥터](/ko/reference/connectors/rest/business-central/)
- [Business Central에 연결](/ko/guides/connections/business-central/)
- [ERP 전기 내역 검토](/ko/guides/connections/erp-post-history/)
