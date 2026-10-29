---
title: STDDEV (Lakehouse v2)
description: STDDEV — renvoie l'écart type de la population. Alias de `STDDEV_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev.md
---

Renvoie l'écart type de la population. Alias de `STDDEV_POP`.

## Syntaxe Analyze

```python
func.stddev(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## Syntaxe SQL

```sql
STDDEV(<score>)
```

## Exemples SQL

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
