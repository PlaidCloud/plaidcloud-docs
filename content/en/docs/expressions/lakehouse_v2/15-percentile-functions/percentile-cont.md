---
title: PERCENTILE_CONT
---

Returns an interpolated percentile value based on a continuous distribution.

## Analyze Syntax

```python
func.percentile_cont(<percentile>)
```

## Analyze Examples

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## SQL Syntax

```sql
PERCENTILE_CONT(<percentile>)
```

## SQL Examples

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
