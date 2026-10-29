---
title: INSPECT_TASK_RUNS (Lakehouse v2)
description: INSPECT_TASK_RUNS — gibt den Ausführungsverlauf einer Aufgabe zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-task-runs.md
---

Gibt den Ausführungsverlauf einer Aufgabe zurück.

## Analyze-Syntax

```python
func.inspect_task_runs(<task_name>)
```

## Analyze-Beispiele

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## SQL-Syntax

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
