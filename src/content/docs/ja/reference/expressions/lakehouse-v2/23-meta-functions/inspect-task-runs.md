---
title: INSPECT_TASK_RUNS（Lakehouse v2）
description: INSPECT_TASK_RUNS — タスクの実行履歴を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-task-runs.md
---

タスクの実行履歴を返します。

## Analyze 構文

```python
func.inspect_task_runs(<task_name>)
```

## Analyze の例

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## SQL 構文

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## SQL の例

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
