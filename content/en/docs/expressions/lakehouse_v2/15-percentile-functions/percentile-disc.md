---
title: PERCENTILE_DISC
---

Returns the smallest value whose cumulative distribution is >= the specified percentile.

## Analyze Syntax

```python
func.percentile_disc(<percentile>)
```

## Analyze Examples

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000  │
└───────┘
```

## SQL Syntax

```sql
PERCENTILE_DISC(<percentile>)
```

## SQL Examples

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000  │
└───────┘
```
