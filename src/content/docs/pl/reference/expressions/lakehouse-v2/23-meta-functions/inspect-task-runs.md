---
title: INSPECT_TASK_RUNS (Lakehouse v2)
description: INSPECT_TASK_RUNS — zwraca historię wykonania zadania.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-task-runs.md
---

Zwraca historię wykonania zadania.

## Składnia Analyze

```python
func.inspect_task_runs(<task_name>)
```

## Przykłady Analyze

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## Składnia SQL

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## Przykłady SQL

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
