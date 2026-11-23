---
title: 파운데이션 학습 경로
description: PlaidCloud 파운데이션 랩에 앞서 읽어야 할 내용과 랩에서 만들어야 하는 것을 안내합니다.
sidebar:
  label: 파운데이션
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/foundations.md
---

파운데이션은 이후 어떤 트랙으로 가든 모든 사용자가 취득하는 배지 하나입니다. 이 랩에는 시간 제한이 없습니다. 랩이 진행되는 방식은 [PlaidCloud 인증](/ko/guides/certification/)을 참조하십시오.

## 읽는 순서

1. [첫 15분](/ko/get-started/tutorials/first-15-minutes/)
2. [데이터 로드, 변환, 게시](/ko/get-started/tutorials/load-and-transform-data/)
3. [워크플로 만들기](/ko/guides/workflows/create-workflow/)
4. [Table Inner Join 단계](/ko/reference/workflow-steps/tables/table-inner-join/)
5. [워크플로 실행](/ko/guides/workflows/run-a-workflow/)
6. [워크플로 로그 보기](/ko/guides/workflows/viewing-workflow-log/)
7. [테이블 게시](/ko/guides/data/publish/)

## 랩에서 요구하는 작업

랩의 이름은 *기초: 지역별 매출*입니다.

주문과 고객은 랩 프로젝트에 이미 로드되어 있습니다. 랩의 워크플로에서 완료된 주문만 남기고, 이를 고객과 조인하여 지역별로 총 금액과 주문 수를 담은 행 하나씩을 기록하는 단계를 만듭니다. 그런 다음 워크플로를 실행하고 결과 테이블을 게시합니다.

랩은 워크플로가 실행되는지, 그리고 결과 테이블의 합계가 올바른지 검사합니다.
