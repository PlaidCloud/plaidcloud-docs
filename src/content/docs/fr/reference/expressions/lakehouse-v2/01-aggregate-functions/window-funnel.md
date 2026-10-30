---
title: WINDOW_FUNNEL (Lakehouse v2)
description: "Utilisez la fonction d'agrégation WINDOW_FUNNEL dans PlaidCloud Lakehouse. Recherche des chaînes d'événements dans une séquence ordonnée dans le temps et renvoie la longueur maximale de chaîne."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/window-funnel.md
---

Recherche des chaînes d'événements dans une séquence ordonnée dans le temps et renvoie la longueur maximale de chaîne.

## Syntaxe Analyze

```python
func.window_funnel(86400, get_column(table, 'ts'), cond1, cond2)
```

## Exemples Analyze

```python
func.window_funnel(86400, get_column(table, 'event_time'), get_column(table, 'step1'), get_column(table, 'step2'))
```

## Syntaxe SQL

```sql
WINDOW_FUNNEL(86400, <ts>, cond1, cond2)
```

## Exemples SQL

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
