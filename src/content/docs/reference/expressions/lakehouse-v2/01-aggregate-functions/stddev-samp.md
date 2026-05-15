---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP — returns the sample standard deviation.
---

Returns the sample standard deviation.

## Analyze Syntax

```python
func.stddev_samp(get_column(table, 'score'))
```

## Analyze Examples

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## SQL Syntax

```sql
STDDEV_SAMP(<score>)
```

## SQL Examples

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
