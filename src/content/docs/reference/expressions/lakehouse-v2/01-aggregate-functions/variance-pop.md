---
title: VARIANCE_POP (Lakehouse v2)
description: VARIANCE_POP — returns the population variance.
---

Returns the population variance.

## Analyze Syntax

```python
func.variance_pop(get_column(table, 'score'))
```

## Analyze Examples

```python
func.variance_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL Syntax

```sql
VARIANCE_POP(<score>)
```

## SQL Examples

```sql
SELECT VARIANCE_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
