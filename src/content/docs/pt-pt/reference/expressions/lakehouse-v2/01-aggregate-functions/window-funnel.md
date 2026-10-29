---
title: WINDOW_FUNNEL (Lakehouse v2)
description: "Utilize a função de agregação WINDOW_FUNNEL no PlaidCloud Lakehouse. Procura cadeias de eventos numa sequência ordenada no tempo e devolve o comprimento máximo da cadeia."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/window-funnel.md
---

Procura cadeias de eventos numa sequência ordenada no tempo e devolve o comprimento máximo da cadeia.

## Sintaxe do Analyze

```python
func.window_funnel(86400, get_column(table, 'ts'), cond1, cond2)
```

## Exemplos do Analyze

```python
func.window_funnel(86400, get_column(table, 'event_time'), get_column(table, 'step1'), get_column(table, 'step2'))
```

## Sintaxe SQL

```sql
WINDOW_FUNNEL(86400, <ts>, cond1, cond2)
```

## Exemplos SQL

```sql
SELECT user_id,
  WINDOW_FUNNEL(86400, event_time,
    event = 'view', event = 'cart', event = 'purchase')
FROM user_events GROUP BY user_id;

┌─────────┬─────────────────┐
│ user_id │ window_funnel    │
├─────────┼─────────────────┤
│       1 │               3 │
│       2 │               2 │
│       3 │               1 │
└─────────┴─────────────────┘
```
