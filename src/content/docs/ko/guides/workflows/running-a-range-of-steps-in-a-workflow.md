---
title: 워크플로에서 여러 단계 실행
description: PlaidCloud 워크플로에서 특정 범위의 단계를 실행하여 데이터 처리 파이프라인의 일부분만 선택적으로 실행합니다.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/running-a-range-of-steps-in-a-workflow.md
---

개별 단계를 실행하는 것도 유용하지만, 개발, 테스트 또는 문제 해결을 위해 전체 워크플로의 일부만 실행해야 할 때도 있습니다. 일부 단계만 실행하려면 실행할 단계를 모두 선택한 다음 워크플로 단계 계층 상단의 **작업** 메뉴에서 **선택한 단계 실행**을 선택합니다. 그러면 일반 워크플로 처리가 시작되며, 선택한 단계의 시작 지점에서 워크플로를 시작하여 선택한 마지막 단계가 완료되면 중지합니다.

선택한 마지막 단계가 [**Execute in Parallel**](/ko/guides/workflows/controlling-parallel-execution/)으로 설정된 그룹 안에 있으면, 실행은 해당 그룹에서 선택된 나머지 단계가 모두 끝날 때까지 기다린 후 중지합니다.
