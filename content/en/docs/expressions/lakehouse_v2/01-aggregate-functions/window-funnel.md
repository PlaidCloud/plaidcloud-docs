---
title: WINDOW_FUNNEL
---

Searches for event chains in a time-ordered sequence and returns the maximum chain length.

## Analyze Syntax

```python
func.window_funnel(86400, get_column(table, 'ts'), cond1, cond2)
```

## Analyze Examples

```python
func.window_funnel(86400, get_column(table, 'event_time'), get_column(table, 'step1'), get_column(table, 'step2'))
```

## SQL Syntax

```sql
WINDOW_FUNNEL(86400, <ts>, cond1, cond2)
```

## SQL Examples

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
