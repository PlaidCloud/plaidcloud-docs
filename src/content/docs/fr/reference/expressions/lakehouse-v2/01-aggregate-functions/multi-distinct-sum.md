---
title: MULTI_DISTINCT_SUM (Lakehouse v2)
description: MULTI_DISTINCT_SUM — renvoie la somme des valeurs distinctes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/multi-distinct-sum.md
---

Renvoie la somme des valeurs distinctes.

## Syntaxe Analyze

```python
func.multi_distinct_sum(get_column(table, 'bonus'))
```

## Exemples Analyze

```python
func.multi_distinct_sum(get_column(table, 'bonus'))

┌───────┐
│ 25000 │
└───────┘
```

## Syntaxe SQL

```sql
MULTI_DISTINCT_SUM(<bonus>)
```

## Exemples SQL

```sql
SELECT MULTI_DISTINCT_SUM(bonus) FROM employees;

┌───────┐
│ 25000 │
└───────┘
```
