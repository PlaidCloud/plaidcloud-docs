---
title: 데이터 엔지니어링 학습 경로
description: PlaidCloud 데이터 엔지니어링 프랙티셔너 및 엑스퍼트 랩에 앞서 읽어야 할 내용과 각 랩에서 요구하는 작업을 안내합니다.
sidebar:
  label: 데이터 엔지니어링
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/data-engineering.md
---

데이터 엔지니어링 트랙은 올바르고, 변수로 구동되며, 빠른 워크플로를 만드는 방법을 다룹니다. [파운데이션](/ko/guides/certification/foundations/) 경로부터 시작하십시오. 랩이 진행되는 방식은 [PlaidCloud 인증](/ko/guides/certification/)을 참조하십시오.

## 프랙티셔너

### 읽는 순서

1. [워크플로 만들기](/ko/guides/workflows/create-workflow/)
2. [워크플로 단계](/ko/reference/workflow-steps/), 특히 [Table Inner Join 단계](/ko/reference/workflow-steps/tables/table-inner-join/)와 [Table Extract 단계](/ko/reference/workflow-steps/tables/table-extract/)
3. [워크플로 변수 관리](/ko/guides/workflows/manage-workflow-variables/)
4. [작업 재사용: 변수, 매크로, UDF](/ko/get-started/tutorials/reuse-variables-macros-udfs/)
5. [워크플로 실행](/ko/guides/workflows/run-a-workflow/)
6. [워크플로 로그 보기](/ko/guides/workflows/viewing-workflow-log/)

### 랩에서 요구하는 작업

랩의 이름은 *데이터 엔지니어링: 월별 매출 구축*입니다.

원시 테이블 세 개, 즉 판매 라인, 매장, 제품이 로드되어 있습니다. 랩의 워크플로에서 한 달 동안 판매된 라인에 대해 지역과 제품 카테고리별로 행 하나씩, 수량과 매출을 담은 월별 요약을 만듭니다. 월은 단계에 직접 입력한 값이 아니라 프로젝트 변수에서 가져옵니다. 랩은 변수를 바꾼 다음 워크플로를 다시 실행합니다. 표준 단계만 사용하고 SQL 또는 코드 단계는 사용하지 않습니다.

랩은 워크플로가 실행되는지, 표준 단계만 사용하는지, 그리고 요약이 해당 월과 다른 월 모두에서 올바른지 검사합니다.

## 엑스퍼트

엑스퍼트 랩은 시간 제한이 있습니다. 시작한 시점부터 4시간이 주어집니다.

### 읽는 순서

1. [워크플로 디버그](/ko/get-started/tutorials/debug-a-workflow/)
2. [워크플로 로그 보기](/ko/guides/workflows/viewing-workflow-log/)
3. [단계 오류 관리](/ko/guides/workflows/managing-step-errors/)
4. [단계 데이터 미리 보기](/ko/guides/workflows/preview-step-data/)
5. [워크플로 최적화](/ko/guides/workflows/optimize-a-workflow/)
6. [워크플로 단계](/ko/reference/workflow-steps/), 특히 [Table Inner Join 단계](/ko/reference/workflow-steps/tables/table-inner-join/)

### 랩에서 요구하는 작업

랩의 이름은 *데이터 엔지니어링 전문가: 야간 빌드 수정 및 속도 개선*입니다.

야간 워크플로가 실행되지 않게 되었고, 그 전에도 너무 느렸습니다. 실행 로그를 읽고 원인을 모두 찾아 워크플로가 성공하고, 올바른 요약을 만들고, 이전 소요 시간의 극히 일부 안에 끝나도록 수정합니다. 계정이 없는 행은 제외하며, 두 번 나열된 계정이 개수를 부풀려서는 안 됩니다. 표준 단계만 사용하고 입력 테이블은 그대로 둡니다.

랩은 워크플로가 실행되는지, 표준 단계만 사용하는지, 요약이 올바른지, 입력 테이블이 변경되지 않았는지, 그리고 워크플로가 충분히 빠른지 검사합니다.
