---
title: COVAR_POP
description: "Learn how to use the COVAR_POP aggregate function in PlaidCloud Lakehouse. Returns the population covariance of two expressions - with syntax and examples."
---

Returns the population covariance of two expressions.

## Analyze Syntax

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyze Examples

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## SQL Syntax

```sql
COVAR_POP(<y>, <x>)
```

## SQL Examples

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
