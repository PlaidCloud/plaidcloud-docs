---
title: STDDEV (Lakehouse v2)
description: STDDEV — returns the population standard deviation. Alias for `STDDEV_POP`.
---

Returns the population standard deviation. Alias for `STDDEV_POP`.

## Analyze Syntax

```python
func.stddev(get_column(table, 'score'))
```

## Analyze Examples

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL Syntax

```sql
STDDEV(<score>)
```

## SQL Examples

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
