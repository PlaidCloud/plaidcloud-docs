---
title: WINDOW_FUNNEL (Lakehouse v2)
description: "Use la función de agregación WINDOW_FUNNEL en PlaidCloud Lakehouse. Busca cadenas de eventos en una secuencia ordenada por tiempo y devuelve la longitud máxima de la cadena."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/window-funnel.md
---

Busca cadenas de eventos en una secuencia ordenada por tiempo y devuelve la longitud máxima de la cadena.

## Sintaxis de Analyze

```python
func.window_funnel(86400, get_column(table, 'ts'), cond1, cond2)
```

## Ejemplos de Analyze

```python
func.window_funnel(86400, get_column(table, 'event_time'), get_column(table, 'step1'), get_column(table, 'step2'))
```

## Sintaxis de SQL

```sql
WINDOW_FUNNEL(86400, <ts>, cond1, cond2)
```

## Ejemplos de SQL

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
