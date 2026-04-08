---
title: ARRAY_CUM_SUM
description: "Learn how to use the ARRAY_CUM_SUM array function in PlaidCloud Lakehouse. Returns the cumulative sum of elements in an array - with syntax and examples."
---

Returns the cumulative sum of elements in an array.

## Analyze Syntax

```python
func.array_cum_sum([1, 2, 3, 4])
```

## Analyze Examples

```python
func.array_cum_sum([1, 2, 3, 4])

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```

## SQL Syntax

```sql
ARRAY_CUM_SUM([1, 2, 3, 4])
```

## SQL Examples

```sql
SELECT ARRAY_CUM_SUM([1, 2, 3, 4]);

┌────────────┐
│ [1,3,6,10] │
└────────────┘
```
