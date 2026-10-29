---
title: 워크플로 오류 발생
description: PlaidCloud 워크플로 단계에서 사용자 지정 오류를 발생시켜 조건이 충족되지 않을 때 오류 처리를 트리거하고 실행을 중단합니다.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/raise-workflow-error.md
---

## 설명

사용자 지정 메시지와 함께 워크플로를 오류 상태로 만듭니다. 앞선 단계에서 감지한 데이터 조건에 따라 워크플로를 실패시켜야 할 때 사용합니다. 예를 들어 "행 수가 0이면 실패", "핵심 검증 테이블에 매핑되지 않은 값이 있으면 실패", "잔액 검사가 일치하지 않으면 실패" 같은 경우입니다.

실제로 문제가 있을 때만 오류가 발생하도록 [단계 조건](/ko/guides/workflows/step-conditions/)과 함께 사용하십시오. 이 단계가 실행되면 워크플로가 즉시 중지되고 오류가 워크플로 로그에 기록되며, 설정된 경우 이 로그가 복구 워크플로를 트리거할 수 있습니다.


## 워크플로 오류 발생


주로 단계 조건과 함께 사용하며, 조건이 충족되면 실행되어 워크플로 내에서 오류를 발생시키도록 단계를 설정할 수 있습니다.
