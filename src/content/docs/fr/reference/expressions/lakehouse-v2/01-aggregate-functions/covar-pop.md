---
title: COVAR_POP (Lakehouse v2)
description: COVAR_POP — renvoie la covariance de population de deux expressions.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-pop.md
---

Renvoie la covariance de population de deux expressions.

## Syntaxe Analyze

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Exemples Analyze

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## Syntaxe SQL

```sql
COVAR_POP(<y>, <x>)
```

## Exemples SQL

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
