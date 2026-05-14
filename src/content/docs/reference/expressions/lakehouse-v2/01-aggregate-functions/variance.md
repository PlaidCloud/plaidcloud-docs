---
title: VARIANCE
description: "Learn how to use the VARIANCE aggregate function in PlaidCloud Lakehouse. Returns the population variance. Alias for `VARIANCE_POP` - with syntax and examples."
---

Returns the population variance. Alias for `VARIANCE_POP`.

## Analyze Syntax

```python
func.variance(get_column(table, 'score'))
```

## Analyze Examples

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQL Syntax

```sql
VARIANCE(<score>)
```

## SQL Examples

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
