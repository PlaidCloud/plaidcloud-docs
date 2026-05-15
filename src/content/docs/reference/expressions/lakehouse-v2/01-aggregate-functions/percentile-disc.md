---
title: "PERCENTILE_DISC (Aggregate, Lakehouse v2)"
description: "Use the PERCENTILE_DISC aggregate function in PlaidCloud Lakehouse. Returns the smallest value whose cumulative distribution is >= the specified percentile."
---

Returns the smallest value whose cumulative distribution is >= the specified percentile.

## Analyze Syntax

```python
func.percentile_disc(0.5)
```

## Analyze Examples

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQL Syntax

```sql
PERCENTILE_DISC(0.5)
```

## SQL Examples

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
