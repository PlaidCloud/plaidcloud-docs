---
title: INSPECT_TASK_RUNS (Lakehouse v2)
description: INSPECT_TASK_RUNS — Devuelve el historial de ejecución de una tarea.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-task-runs.md
---

Devuelve el historial de ejecución de una tarea.

## Sintaxis de Analyze

```python
func.inspect_task_runs(<task_name>)
```

## Ejemplos de Analyze

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## Sintaxis de SQL

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## Ejemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
