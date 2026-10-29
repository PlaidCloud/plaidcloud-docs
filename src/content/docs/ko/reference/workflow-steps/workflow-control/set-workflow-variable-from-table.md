---
title: Set Workflow Variable Values from Table 단계
description: 프로젝트 테이블에서 값을 읽어 워크플로 변수에 할당하여, 이후 단계가 하드 코딩된 값이 아니라 데이터를 기준으로 분기하거나 필터링하도록 합니다.
sidebar:
  order: 16
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable-from-table.md
---

## 설명

프로젝트 테이블에서 값을 읽어 워크플로 변수에 할당합니다. 워크플로 자체의 데이터로 워크플로를 구동할 때 사용합니다. 예를 들어 제어 테이블에서 가장 최근에 마감된 기간, 행 수, 파일 경로를 읽어 하위 단계에서 참조하게 할 수 있습니다.

여기서 설정한 변수는 워크플로 실행 동안에만 유지됩니다. 프로젝트의 워크플로 간에 유지되는 값을 설정하려면 [Set Project Variable Values from Table 단계](/ko/reference/workflow-steps/workflow-control/set-project-variable-from-table/)를 사용하십시오.

## 구성

### 소스 열

각 소스 열을 채울 워크플로 변수에 매핑합니다. 이 단계는 한 행만 읽으므로 실행 전에 테이블을 한 행으로 좁혀야 합니다.

### 데이터 하위 집합 선택

소스 행을 좁히는 필터 식으로, 일반적으로 원하는 값이 들어 있는 한 행으로 좁힙니다.

### 결과 데이터에 보조 필터 적용

집계 후에 적용되는 `HAVING` 방식의 필터로, 값이 그룹화된 계산에서 나올 때 사용합니다.

### 최종 데이터 테이블 슬라이싱(제한)

기본적으로 꺼져 있으며, 켜면 한 행으로 제한됩니다. 소스에서 후보 행이 여러 개 반환될 수 있고 그중 특정 행이 필요한 경우 명시적인 정렬과 함께 켜십시오.

## 관련 항목

- [워크플로 제어 단계](/ko/reference/workflow-steps/workflow-control/)
- [Set Workflow Variable 단계](/ko/reference/workflow-steps/workflow-control/set-workflow-variable/)
- [Set Project Variable Values from Table 단계](/ko/reference/workflow-steps/workflow-control/set-project-variable-from-table/)
- [워크플로 변수 관리](/ko/guides/workflows/manage-workflow-variables/)
