---
title: STD (Lakehouse v2)
description: STD — renvoie l'écart type de la population. Alias de `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/std.md
---

Renvoie l'écart type de la population. Alias de `STDDEV_POP`.

## Syntaxe Analyze

```python
func.std(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.std(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Syntaxe SQL

```sql
STD(<score>)
```

## Exemples SQL

```sql
SELECT STD(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
