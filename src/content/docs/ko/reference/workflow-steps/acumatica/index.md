---
title: Acumatica 단계
description: Acumatica 연결을 통해 Acumatica에서 읽고 쓰는 워크플로 단계로, 계약 기반 REST 엔터티를 가져오고 분개 거래, 인보이스, 청구서, 결제를 전기합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/acumatica/index.md
---

[Acumatica 연결](/ko/guides/connections/acumatica/)을 통해 Acumatica에서 읽고 쓰는 워크플로 단계입니다. 가져오기 단계는 OData를 작성하지 않고 Acumatica의 계약 기반 REST 엔터티를 가져오며, 전기 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 분개 거래, 판매 인보이스, 청구서, 결제를 전기합니다.

## 단계

- [Import Acumatica Entity 단계](/ko/reference/workflow-steps/acumatica/import-acumatica-entity/) — 서버 측 필터를 사용하는 마스터 데이터 및 트랜잭션 엔터티.
- [Acumatica: Post Documents 단계](/ko/reference/workflow-steps/acumatica/acumatica-post/) — 분개 거래, 판매 인보이스, 청구서, 결제를 전기합니다.

## 관련 항목

- [Acumatica REST 커넥터](/ko/reference/connectors/rest/acumatica/)
- [Acumatica에 연결](/ko/guides/connections/acumatica/)
- [ERP 전기 내역 검토](/ko/guides/connections/erp-post-history/)
