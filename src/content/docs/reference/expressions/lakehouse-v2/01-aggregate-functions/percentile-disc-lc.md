---
title: PERCENTILE_DISC_LC
description: PERCENTILE_DISC_LC — returns the percentile value using a low-cardinality optimized algorithm.
---

Returns the percentile value using a low-cardinality optimized algorithm.

## Analyze Syntax

```python
func.percentile_disc_lc(0.5)
```

## Analyze Examples

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQL Syntax

```sql
PERCENTILE_DISC_LC(0.5)
```

## SQL Examples

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
