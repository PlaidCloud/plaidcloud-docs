---
title: INSPECT_TASK_RUNS (Lakehouse v2)
description: INSPECT_TASK_RUNS：返回任务的执行历史。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-task-runs.md
---

返回任务的执行历史。

## Analyze 语法

```python
func.inspect_task_runs(<task_name>)
```

## Analyze 示例

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## SQL 语法

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## SQL 示例

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
