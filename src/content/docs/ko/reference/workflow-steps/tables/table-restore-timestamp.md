---
title: Table Restore to Timestamp 단계
description: 워크플로 단계로, PlaidCloud 테이블을 특정 시점 이전 또는 그 시점에 찍힌 가장 최근 스냅샷으로 제자리에서 복원합니다.
sidebar:
  order: 45
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/tables/table-restore-timestamp.md
---

## 설명

**테이블: 타임스탬프로 복원**은 테이블을 특정 시점 이전 또는 그 시점에 찍힌 가장 최근 스냅샷으로 제자리에서 교체합니다. 테이블을 기간 말 시점이나 잘못된 로드 이전의 상태로 되돌릴 때 사용합니다. 복원은 테이블 자체를 변경하므로 해당 테이블을 읽는 모든 단계와 대시보드에 복원된 행이 표시됩니다.

## 특정 시점으로 복원

| 설정 | 필수 | 기능 |
| --- | --- | --- |
| 테이블 | 예 | 복원할 테이블입니다. |
| 타임스탬프 | 예 | `2026-09-30T23:59:59Z` 같은 ISO-8601 시간 또는 1970년 이후의 초 단위로 나타낸 시점입니다. 시간대가 없는 시간은 UTC입니다. `{restore_time}` 같은 워크플로 변수도 사용할 수 있습니다. |
| 타임스탬프 정확히 그 시점에 찍힌 스냅샷 포함 | 아니요 | 기본적으로 켜져 있습니다. 타임스탬프 이전에 찍힌 스냅샷으로만 복원하려면 해제합니다. |

타임스탬프 이전 또는 그 시점에 찍힌 스냅샷이 없으면 단계는 경고와 함께 완료되고, 테이블은 그대로 두며, 워크플로는 계속 진행됩니다. 테이블을 찾을 수 없는 경우에도 경고와 함께 완료됩니다. 이름이 있는 스냅샷만 보관하는 스토리지 엔진에서는 타임스탬프 정확히 그 시점에 찍힌 스냅샷으로만 테이블을 복원할 수 있으므로, 되돌리고 싶은 시점에 이름이 있는 스냅샷을 찍어 두십시오.

## 관련 항목

- [테이블 복원](/ko/reference/workflow-steps/import/restore-tables/)
- [테이블 단계](/ko/reference/workflow-steps/tables/)
