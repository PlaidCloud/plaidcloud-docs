---
title: COVAR_SAMP
---

Returns the sample covariance of two expressions.

## Analyze Syntax

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Analyze Examples

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## SQL Syntax

```sql
COVAR_SAMP(<y>, <x>)
```

## SQL Examples

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
