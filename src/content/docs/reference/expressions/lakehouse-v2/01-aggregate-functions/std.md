---
title: STD
description: STD — returns the population standard deviation. Alias for `STDDEV_POP`.
---

Returns the population standard deviation. Alias for `STDDEV_POP`.

## Analyze Syntax

```python
func.std(get_column(table, 'score'))
```

## Analyze Examples

```python
func.std(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL Syntax

```sql
STD(<score>)
```

## SQL Examples

```sql
SELECT STD(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
