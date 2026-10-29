---
title: INSPECT_TASK_RUNS (Lakehouse v2)
description: INSPECT_TASK_RUNS — retorna o histórico de execuções de uma tarefa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-task-runs.md
---

Retorna o histórico de execuções de uma tarefa.

## Sintaxe do Analyze

```python
func.inspect_task_runs(<task_name>)
```

## Exemplos do Analyze

```python
func.inspect_task_runs('my_task')

┌─────────────┐
│ (task runs)  │
└─────────────┘
```

## Sintaxe SQL

```sql
INSPECT_TASK_RUNS(<task_name>)
```

## Exemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_TASK_RUNS('my_task'));

┌────────────────────┐
│ (task run history)  │
└────────────────────┘
```
