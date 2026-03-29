---
title: VARIANCE_SAMP
---

Returns the sample variance.

## Analyze Syntax

```python
func.variance_samp(get_column(table, 'score'))
```

## Analyze Examples

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQL Syntax

```sql
VARIANCE_SAMP(<score>)
```

## SQL Examples

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
