---
title: PERCENTILE_APPROX_WEIGHT (Lakehouse v2)
description: PERCENTILE_APPROX_WEIGHT — renvoie une valeur de percentile approximative pondérée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx-weight.md
---

Renvoie une valeur de percentile approximative pondérée.

## Syntaxe Analyze

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)
```

## Exemples Analyze

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)

┌──────┐
│ 72.5 │
└──────┘
```

## Syntaxe SQL

```sql
PERCENTILE_APPROX_WEIGHT(<val>, <weight>, 0.5)
```

## Exemples SQL

```sql
SELECT PERCENTILE_APPROX_WEIGHT(val, weight, 0.5) FROM data;

┌──────┐
│ 72.5 │
└──────┘
```
