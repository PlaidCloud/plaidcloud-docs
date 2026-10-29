---
title: Set Project Variable Values from Table 단계
description: 프로젝트 테이블에서 값을 읽어 워크플로 실행 간에 유지되는 프로젝트 변수에 할당합니다.
sidebar:
  order: 17
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-project-variable-from-table.md
---

## 설명

프로젝트 테이블에서 값을 읽어 *프로젝트* 변수에 할당합니다. [Set Workflow Variable Values from Table 단계](/ko/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)와 달리 이 값은 실행이 끝난 뒤에도 유지되므로, 값이 다시 바뀔 때까지 프로젝트의 모든 워크플로에서 볼 수 있습니다.

마지막으로 성공적으로 로드된 기간, 워터마크 타임스탬프, 현재 시나리오 이름처럼 한 번의 실행보다 오래 유지되어야 하는 상태에 사용하십시오.

## 구성

### 소스 열

각 소스 열을 채울 프로젝트 변수에 매핑합니다. 이 단계는 한 행만 읽으므로 실행 전에 테이블을 한 행으로 좁혀야 합니다.

### 데이터 하위 집합 선택

소스 행을 좁히는 필터 식입니다.

### 결과 데이터에 보조 필터 적용

집계 후에 적용되는 `HAVING` 방식의 필터입니다.

### 최종 데이터 테이블 슬라이싱(제한)

기본적으로 꺼져 있으며, 켜면 한 행으로 제한됩니다. 소스에서 후보 행이 여러 개 반환될 수 있는 경우 명시적인 정렬과 함께 켜십시오.

## 관련 항목

- [워크플로 제어 단계](/ko/reference/workflow-steps/workflow-control/)
- [Set Project Variable 단계](/ko/reference/workflow-steps/workflow-control/set-project-variable/)
- [Set Workflow Variable Values from Table 단계](/ko/reference/workflow-steps/workflow-control/set-workflow-variable-from-table/)
