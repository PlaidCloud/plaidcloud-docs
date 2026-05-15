---
title: INSPECT_TASK_RUNS (Lakehouse v2)
description: INSPECT_TASK_RUNS — returns execution history of a task.
---

Returns execution history of a task.

## Analyze Syntax

```python
func.inspect_task_runs(<task_name>)
```

## Analyze Examples

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## SQL Syntax

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## SQL Examples

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
