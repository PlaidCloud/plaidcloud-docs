---
title: NetSuite 단계
description: NetSuite 워크플로 단계입니다. NetSuite 연결을 통해 잔액, 총계정원장 상세, 마스터 데이터 또는 직접 작성한 SuiteQL 쿼리를 가져오고 분개 전표를 전기합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/netsuite/index.md
---

[NetSuite 연결](/ko/guides/connections/netsuite/)을 통해 NetSuite에서 읽고 NetSuite에 쓰는 워크플로 단계입니다. 미리 만들어진 가져오기 단계는 일반적인 재무 데이터와 기준 데이터를 가져오는 가장 간단한 방법입니다. 연결, 대상 테이블, 날짜 범위 또는 레코드 유형만 선택하면 되며 SuiteQL을 작성할 필요가 없습니다.

## 가져오기 단계

- [NetSuite: 잔액 가져오기](/ko/reference/workflow-steps/netsuite/import-balances/) — 날짜 범위와 자회사별 계정 잔액(시산표)입니다.
- [NetSuite: 총계정원장 상세 가져오기](/ko/reference/workflow-steps/netsuite/import-gl-detail/) — 날짜 범위와 자회사별 총계정원장 거래 라인 상세입니다.
- [NetSuite: 마스터 데이터 가져오기](/ko/reference/workflow-steps/netsuite/import-master-data/) — 마스터 목록(계정, 자회사, 부서, 클래스, 위치, 공급업체, 고객)입니다.
- [NetSuite: SuiteQL 쿼리 가져오기](/ko/reference/workflow-steps/netsuite/import-suiteql-query/) — 직접 작성한 SuiteQL 쿼리를 실행하여 결과를 유형이 지정된 테이블로 로드하며, 날짜 구간과 페이징은 자동으로 처리됩니다.

## 전기 단계

- [Post NetSuite Journal Entry 단계](/ko/reference/workflow-steps/netsuite/post-netsuite-journal-entry/) — 헤더/라인 구조의 분개 전표를 NetSuite로 다시 전기합니다.

## 사용자 지정 가져오기

미리 만들어진 가져오기 단계가 다루지 않는 데이터, 즉 맞춤 쿼리나 미리 만들어진 단계가 없는 NetSuite 레코드에는 직접 작성한 SuiteQL과 함께 [NetSuite: SuiteQL 쿼리 가져오기](/ko/reference/workflow-steps/netsuite/import-suiteql-query/)를 사용하십시오. 시작점으로는 [NetSuite SuiteQL 쿼리 예제](/ko/guides/connections/netsuite-financial-queries/)를 참조하십시오.

## 관련 항목

- [NetSuite REST 커넥터](/ko/reference/connectors/rest/netsuite/)
- [NetSuite에 연결](/ko/guides/connections/netsuite/)
- [NetSuite 재무 데이터 가져오기](/ko/guides/connections/import-netsuite-financials/)
