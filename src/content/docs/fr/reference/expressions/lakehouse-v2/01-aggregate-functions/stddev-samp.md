---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP — renvoie l'écart type de l'échantillon.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-samp.md
---

Renvoie l'écart type de l'échantillon.

## Syntaxe Analyze

```python
func.stddev_samp(get_column(table, 'score'))
```

## Exemples Analyze

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## Syntaxe SQL

```sql
STDDEV_SAMP(<score>)
```

## Exemples SQL

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
