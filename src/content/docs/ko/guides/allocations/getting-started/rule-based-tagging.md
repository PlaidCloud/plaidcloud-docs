---
title: 규칙 기반 태깅
description: 정의된 기준을 사용하여 데이터 레코드를 자동으로 분류하고 레이블을 지정하도록 PlaidCloud 배부에서 규칙 기반 태깅을 구성합니다.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/rule-based-tagging.md
---

규칙 기반 태깅을 사용하면 원천 행에 메타데이터를 표시하여 배부 엔진이 해당 행을 *어디로* 보낼지 결정하는 데 사용하게 할 수 있습니다. 행마다 배부 동작이 달라야 할 때 사용합니다. 예를 들어 한 비용 센터의 비용은 인원 수로 분배하고 다른 비용 센터의 비용은 매출로 분배해야 하는 경우입니다.

## 사용 시기

- 단일 배부 규칙으로는 비용을 실제로 분배해야 하는 방식(비용 유형별로 다른 규칙)을 반영할 수 없는 경우
- 특정 원천 행은 지정한 대상으로 보내고 나머지는 정상적으로 분배되도록 하려는 경우
- 각 풀이 서로 다른 동인을 사용하는 다중 풀 배부를 모델링하는 경우

## 태깅의 작동 방식

1. **원천에 태그를 지정합니다.** 값 테이블에 각 행을 분류하는 태그 열을 하나 이상 추가합니다.
2. **배부 규칙에서 태그를 참조합니다.** 배부 단계를 구성할 때 *"원천 태그 X = 값 Y이면 동인 D와 대상 차원 T를 사용하여 배부"*와 같은 형태로 규칙을 표현합니다.
3. **엔진이 행을 라우팅합니다.** 각 원천 행은 규칙과 순서대로 매칭되며, 처음으로 일치하는 규칙이 배부 동작을 결정합니다.

## 태그에 적합한 원천 패턴

- `payroll`, `facilities`, `it`, `marketing` 같은 값을 가진 `cost_category`라는 열
- 행이 속한 배부 풀의 이름을 담은 `pool`이라는 열
- 다른 처리를 적용하는 `is_overhead` 같은 불리언 열

## 예

`cost_center`와 `cost_category`가 있는 비용 테이블:

| cost_center | cost_category | amount |
|---|---|---|
| 1010 | payroll | 50,000 |
| 1010 | it | 8,000 |
| 1020 | payroll | 35,000 |

배부 규칙을 두 개 구성할 수 있습니다.

- **급여 행**은 인원 수 동인으로 분배
- **IT 행**은 사용자 수 동인으로 분배

두 규칙 모두 동일한 원천 테이블에 대해 실행되며, 각 행에 어느 규칙이 적용되는지는 태그가 결정합니다.

## 관련 항목

- [배부 빠른 시작](/ko/guides/allocations/getting-started/allocations-quick-start/) — 태깅을 추가하기 전의 기본 흐름
- [배부 구성](/ko/guides/allocations/setup/configure-an-allocation/) — 전체 단계 참조
- [배부 규칙 단계](/ko/reference/workflow-steps/allocation/allocation-rules/) — 태그가 지정된 데이터를 사용하는 워크플로 단계
