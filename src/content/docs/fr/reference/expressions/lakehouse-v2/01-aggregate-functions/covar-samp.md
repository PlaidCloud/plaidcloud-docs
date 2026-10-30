---
title: COVAR_SAMP (Lakehouse v2)
description: COVAR_SAMP — renvoie la covariance d'échantillon de deux expressions.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-samp.md
---

Renvoie la covariance d'échantillon de deux expressions.

## Syntaxe Analyze

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Exemples Analyze

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## Syntaxe SQL

```sql
COVAR_SAMP(<y>, <x>)
```

## Exemples SQL

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
