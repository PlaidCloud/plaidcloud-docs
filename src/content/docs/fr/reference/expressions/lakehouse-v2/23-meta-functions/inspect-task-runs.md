---
title: INSPECT_TASK_RUNS (Lakehouse v2)
description: INSPECT_TASK_RUNS — renvoie l'historique d'exécution d'une tâche.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-task-runs.md
---

Renvoie l'historique d'exécution d'une tâche.

## Syntaxe Analyze

```python
func.inspect_task_runs(<task_name>)
```

## Exemples Analyze

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## Syntaxe SQL

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
