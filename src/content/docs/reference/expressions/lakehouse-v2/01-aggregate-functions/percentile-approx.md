---
title: PERCENTILE_APPROX
description: PERCENTILE_APPROX — returns an approximate percentile value using the t-digest algorithm.
---

Returns an approximate percentile value using the t-digest algorithm.

## Analyze Syntax

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Analyze Examples

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## SQL Syntax

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## SQL Examples

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
