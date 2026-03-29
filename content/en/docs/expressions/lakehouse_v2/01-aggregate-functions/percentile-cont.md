---
title: PERCENTILE_CONT
---

Returns an interpolated percentile value based on a continuous distribution.

## Analyze Syntax

```python
func.percentile_cont(0.5)
```

## Analyze Examples

```python
func.percentile_cont(0.5)

┌──────────┐
│ 72500.00 │
└──────────┘
```

## SQL Syntax

```sql
PERCENTILE_CONT(0.5)
```

## SQL Examples

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌──────────┐
│ 72500.00 │
└──────────┘
```
