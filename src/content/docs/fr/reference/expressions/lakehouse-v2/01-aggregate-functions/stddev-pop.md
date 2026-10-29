---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP — renvoie l'écart type de la population.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-pop.md
---

Renvoie l'écart type de la population.

## Syntaxe Analyze

```python
func.stddev_pop(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Syntaxe SQL

```sql
STDDEV_POP(<score>)
```

## Exemples SQL

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
