---
title: VARIANCE_POP
description: "Learn how to use the VARIANCE_POP aggregate function in PlaidCloud Lakehouse. Returns the population variance - see syntax, examples, and output."
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
