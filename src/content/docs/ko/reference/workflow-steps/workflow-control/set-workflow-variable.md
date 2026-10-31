---
title: Set Workflow Variable 단계
description: PlaidCloud 워크플로 단계에서 실행 중에 워크플로 변수를 설정하여 워크플로의 단계 간에 동적 값을 전달합니다.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/set-workflow-variable.md
---

## 설명


"Set Workflow Variable" 단계는 워크플로 중에 사용할 워크플로 변수를 설정합니다. 변수 이름과 값에는 공백을 포함하여 유효한 문자를 자유롭게 조합해 사용할 수 있습니다. 변수는 중괄호 안에 넣어 워크플로 내에서 참조합니다. 예를 들어 *a_variable*은 변환 내에서 *\{a_variable}*로 참조하며, 수식이나 필드 값(예: \{a_variable} * 2)과 같은 곳에 사용할 수 있습니다.



## 변수 목록


이 테이블에는 워크플로에 등록된 모든 변수가 **현재 값**과 **메모**와 함께 표시되며, 단계를 열 때마다 최신 값을 읽어 옵니다. 따라서 변수에 무엇을 설정할지 결정하기 전에 현재 변수가 어떤 값을 갖고 있는지 확인할 수 있습니다.

변수를 설정하려면 해당 행에서 **설정**을 선택하고 **값 설정** 아래에 새 값을 입력합니다. 단계가 실행될 때는 선택된 행만 기록되므로, **설정**을 선택하지 않고 입력한 값은 무시됩니다. 아직 등록되지 않은 변수도 설정할 수 있습니다. 행을 추가하고 같은 방식으로 설정하면 단계를 실행할 때 변수가 생성됩니다.







## 예시

아직 예시가 없습니다...
