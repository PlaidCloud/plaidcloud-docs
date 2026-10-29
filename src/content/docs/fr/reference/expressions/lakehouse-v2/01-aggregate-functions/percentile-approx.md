---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX — renvoie une valeur de percentile approximative à l'aide de l'algorithme t-digest.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

Renvoie une valeur de percentile approximative à l'aide de l'algorithme t-digest.

## Syntaxe Analyze

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Exemples Analyze

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## Syntaxe SQL

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## Exemples SQL

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
