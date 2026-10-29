---
title: Oracle Fusion 단계
description: Oracle Fusion 연결을 통해 Oracle Fusion Cloud에서 읽고 쓰는 워크플로 단계입니다. OData/BIP 또는 대량 FBDI 추출로 GL 잔액과 분개 배치를 가져오고 분개 전표를 전기합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-fusion/index.md
---

[Oracle Fusion 연결](/ko/guides/connections/oracle-fusion/)을 통해 Oracle Fusion Cloud에서 읽고 쓰는 워크플로 단계입니다. 가져오기 단계 두 가지가 서로 다른 데이터 규모를 처리합니다. 일상적인 가져오기에는 OData/BIP 직접 호출을, 대용량 가져오기에는 비동기 FBDI/BIP 대량 추출을 사용합니다. 전기 단계는 PlaidCloud의 공유 ERP 쓰기 파이프라인을 통해 분개 배치를 전기합니다.

## 단계

- [Import Fusion Entity](/ko/reference/workflow-steps/oracle-fusion/import-fusion-entity/) 단계 — 서버 측 날짜, 기간, 숫자 범위 필터를 지원하는 GL 잔액 및 분개 배치 가져오기.
- [Import Fusion Bulk Extract](/ko/reference/workflow-steps/oracle-fusion/import-fusion-bulk-extract/) 단계 — 동일한 엔터티를 비동기 FBDI/BIP 내보내기 작업으로 가져오며, 대용량 데이터에 적합합니다.
- [Oracle Fusion: Post Journal Entry](/ko/reference/workflow-steps/oracle-fusion/oracle-fusion-post/) 단계 — FBDI GL 인터페이스를 통해 총계정원장 분개 배치를 전기하며, 정정이 필요하면 전기된 역분개 전표를 사용합니다.

## 관련 항목

- [Oracle Fusion 커넥터](/ko/reference/connectors/erp/oracle-fusion/)
- [Oracle Fusion에 연결](/ko/guides/connections/oracle-fusion/)
- [ERP 전기 이력 검토](/ko/guides/connections/erp-post-history/)
