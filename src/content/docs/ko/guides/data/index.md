---
title: 데이터 관리 - 테이블 형식
description: 테이블, 뷰, 그리고 모든 규모의 데이터 처리를 지원하는 고성능 Lakehouse 엔진으로 PlaidCloud의 테이블 형식 데이터를 관리합니다.
sidebar:
  label: 개요
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

PlaidCloud의 데이터 계층은 **테이블**(행과 열로 구성된 정형 데이터)과 **뷰**(테이블에 대한 저장된 쿼리)를 중심으로 구성됩니다. 둘 다 프로젝트 안에 있으며 Lakehouse 엔진을 기반으로 동작하므로, 별도의 구성 변경 없이 작은 참조 테이블부터 수십억 행 규모의 분석 데이터 세트까지 확장할 수 있습니다.

## 이 섹션의 내용

- [테이블과 뷰](/ko/guides/data/tables-views/) — 각각이 무엇인지, 언제 무엇을 사용하는지, 서로 어떻게 연동되는지
- [테이블 탐색기](/ko/guides/data/table-explorer/) — 프로젝트의 테이블 탐색 및 검사
- [Currency 데이터 유형](/ko/guides/data/currency-data-type/) — 금액 값에 사용하는 정확한 반각 열 유형과 Numeric 대신 선택해야 하는 경우
- [Vector 데이터 유형](/ko/guides/data/vector-data-type/) — 미리 계산한 임베딩을 프로젝트 테이블에 저장하고, 예상 너비를 선언하고, 가장 가까운 행 검색
- [테이블 스냅샷](/ko/guides/data/table-snapshots/) — 스냅샷 기록 탐색, 과거 스냅샷 시점의 데이터 보기, 테이블 되돌리기 및 복원
- [데이터 게시](/ko/guides/data/publish/) — 프로젝트 테이블을 대시보드, BI 도구, 다운스트림 시스템에서 사용할 수 있도록 하고 성능 지침 검토
- [대용량 이력 테이블에서 최신 레코드 선택](/ko/guides/data/selecting-latest-record-in-large-history-table/) — 성능을 고려한 해결 방법이 있는 일반적인 패턴
- [지오코딩 API](/ko/guides/data/geocoding-api/) — Google 또는 Mapbox 지오코딩 통합을 PlaidCloud의 REST 지오코딩 엔드포인트로 마이그레이션
- [이동 시간 라우팅 API](/ko/guides/data/drive-time-routing-api/) — 옵트인 미리 보기: REST를 통한 이동 시간 등시선과 이동 시간 기준 최근접 순위 지정

## 데이터의 출처

테이블은 일반적으로 **워크플로**가 채웁니다. 워크플로는 데이터를 가져와 변환하고 결과를 다시 기록하는 자동화된 파이프라인입니다. 구성 방법은 [워크플로](/ko/guides/workflows/)를, 사용할 수 있는 모든 단계 유형은 [워크플로 단계 참조](/ko/reference/workflow-steps/)를 참조하십시오.

외부 시스템을 데이터 소스로 연결하는 방법은 [연결(가이드)](/ko/guides/connections/) 및 [커넥터(참조)](/ko/reference/connectors/)를 참조하십시오.

## 관련 항목

- [개념](/ko/get-started/concepts/) — 테이블이 워크플로, 차원 및 더 넓은 데이터 모델과 어떻게 관련되는지
- [프로젝트](/ko/guides/projects/) — 프로젝트가 테이블을 소유하며, 테이블은 프로젝트 밖에 존재하지 않음
- [대시보드](/ko/guides/dashboards/) — 게시된 테이블을 시각화에 사용
