---
title: 분석 학습 경로
description: PlaidCloud 분석 프랙티셔너 및 엑스퍼트 랩에 앞서 읽어야 할 내용과 각 랩에서 요구하는 작업을 안내합니다.
sidebar:
  label: 분석
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/analytics.md
---

분석 트랙은 어떻게 나누어 보더라도 하나의 올바른 답을 주는 지표와, 테이블 간에 공유되는 의미를 다룹니다. [파운데이션](/ko/guides/certification/foundations/) 경로부터 시작하십시오. 랩이 진행되는 방식은 [PlaidCloud 인증](/ko/guides/certification/)을 참조하십시오.

## 프랙티셔너

### 읽는 순서

1. [워크플로 실행](/ko/guides/workflows/run-a-workflow/)
2. [워크플로 로그 보기](/ko/guides/workflows/viewing-workflow-log/)
3. [지표 정의](/ko/integrations/ai-coding-agents/metric-definitions/): 다른 지표에서 지표를 파생하는 방법 포함
4. [게시된 테이블로 대시보드 만들기](/ko/get-started/tutorials/build-a-dashboard/): 선택 사항인 대시보드용

### 랩에서 요구하는 작업

랩의 이름은 *분석: 세 가지 질문을 위한 지표 정의*입니다.

판매 테이블을 준비하는 워크플로를 실행한 다음, 그 테이블에 지표를 정의합니다. 각 지표의 그레인에는 지역과 채널이 포함됩니다. 지역별 매출, 주문 수에서 파생한 채널별 평균 주문 금액, 비용 지표에서 파생한 지역별 매출 대비 비용 비율입니다. 모든 지표는 원본 테이블이 아니라 준비된 테이블을 기반으로 만듭니다. 세 가지 답을 위한 대시보드는 다음 단계로 권장하지만 채점 대상은 아닙니다.

랩은 워크플로가 실행되는지, 그리고 세 지표 각각이 올바른 답을 주는지 검사합니다.

## 엑스퍼트

엑스퍼트 랩은 시간 제한이 있습니다. 시작한 시점부터 4시간이 주어집니다.

### 읽는 순서

1. [지표 정의](/ko/integrations/ai-coding-agents/metric-definitions/)
2. [데이터 모델과 프로젝트 요소](/ko/guides/projects/data-model/)
3. [분석 경로](/ko/integrations/ai-coding-agents/analysis-paths/)

### 랩에서 요구하는 작업

랩의 이름은 *분석 전문가: 일치하는 지표*입니다.

두 지표가 나누는 방식에 따라 서로 다른 답을 내며, 매출 합계는 주문의 합보다 큽니다. 이름은 그대로 유지하면서 두 지표가 지역별과 제품별로 각각 하나의 올바른 답을 반환하도록 수정합니다. 그런 다음 의미가 같은 열을 하나의 공유 요소로 만듭니다. 지역에 대해서는 서로 다른 열 이름으로 지역을 담고 있는 테이블 전체에 걸쳐 하나, 제품에 대해서도 하나입니다.

랩은 워크플로가 실행되는지, 지역별·제품별 매출과 제품별 수량이 올바른지, 그리고 요소가 올바른 열을 포함하는지 검사합니다.
