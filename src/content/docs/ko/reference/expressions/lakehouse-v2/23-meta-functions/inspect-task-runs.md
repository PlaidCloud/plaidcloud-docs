---
title: INSPECT_TASK_RUNS (Lakehouse v2)
description: INSPECT_TASK_RUNS — 작업의 실행 기록을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-task-runs.md
---

작업의 실행 기록을 반환합니다.

## Analyze 구문

```python
func.inspect_task_runs(<task_name>)
```

## Analyze 예제

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## SQL 구문

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
