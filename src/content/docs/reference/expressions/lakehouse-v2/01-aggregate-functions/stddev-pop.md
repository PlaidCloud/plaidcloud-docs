---
title: STDDEV_POP (Lakehouse v2)
description: STDDEV_POP — returns the population standard deviation.
---

Returns the population standard deviation.

## Analyze Syntax

```python
func.stddev_pop(get_column(table, 'score'))
```

## Analyze Examples

```python
func.stddev_pop(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL Syntax

```sql
STDDEV_POP(<score>)
```

## SQL Examples

```sql
SELECT STDDEV_POP(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
