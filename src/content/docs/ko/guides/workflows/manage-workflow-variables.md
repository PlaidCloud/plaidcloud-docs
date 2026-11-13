---
title: 워크플로 변수 관리
description: PlaidCloud에서 워크플로 변수를 관리하여 단계 간에 동적 값을 저장하고 전달함으로써 유연한 데이터 처리 로직을 구현합니다.
sidebar:
  order: 14
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/manage-workflow-variables.md
---

PlaidCloud에서는 프로젝트 범위와 워크플로 범위 모두에서 변수를 사용할 수 있습니다. 이를 통해 프로젝트 전체 변수를 설정하거나 워크플로 간에 정보를 쉽게 전달할 수 있습니다. 변수와 값은 **워크플로** 계층의 변수 아이콘을 클릭하여 볼 수 있습니다.



변수 테이블에서 변수와 현재 값을 확인하고 값을 편집할 수 있습니다. 새 변수를 추가하거나 기존 변수를 삭제할 수도 있습니다.

## 기본 제공 변수

단계 설정과 식에서는 다음 기본 제공 변수를 정의하지 않고도 사용할 수 있습니다.

| 변수 | 값 |
|---|---|
| `{project}`, `{model}`, `{cloud}` | 프로젝트, 모델, 워크스페이스 이름입니다. |
| `{date}` | `Wednesday, 11 November 2026 10:30PM UTC +0`와 같이 긴 형식으로 표시한 실행 시점의 현재 UTC 시간입니다. |
| `{date_iso}` | `2026-11-12T22:49:56+00:00`와 같이 ISO 8601 형식으로 표시한 같은 시점입니다. |

식에서 날짜의 일부를 읽어야 할 때는 `{date_iso}`를 사용하십시오. 처음 7자를 가져오면 월(`2026-11`)이 되고, 처음 10자를 가져오면 일(`2026-11-12`)이 됩니다. `{date_iso}`는 알림 이메일 템플릿, Forecast, Parity, Solver 단계를 포함해 `{date}`를 사용할 수 있는 모든 곳에서 작동합니다.
