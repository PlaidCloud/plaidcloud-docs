---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP — Returns the sample variance. Alias for `VARIANCE_SAMP`.
---

Returns the sample variance. Alias for `VARIANCE_SAMP`.

## Analyze Syntax

```python
func.var_samp(get_column(table, 'score'))
```

## Analyze Examples

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQL Syntax

```sql
VAR_SAMP(<score>)
```

## SQL Examples

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
