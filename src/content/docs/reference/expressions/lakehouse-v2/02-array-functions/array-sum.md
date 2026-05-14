---
title: ARRAY_SUM
description: "Learn how to use the ARRAY_SUM array function in PlaidCloud Lakehouse. Returns the sum of elements in an array - see syntax, examples, and output."
---

Returns the sum of elements in an array.

## Analyze Syntax

```python
func.array_sum([1, 2, 3, 4, 5])
```

## Analyze Examples

```python
func.array_sum([10, 20, 30])

┌────┐
│ 60 │
└────┘
```

## SQL Syntax

```sql
ARRAY_SUM([1, 2, 3, 4, 5])
```

## SQL Examples

```sql
SELECT ARRAY_SUM([10, 20, 30]);

┌────┐
│ 60 │
└────┘
```
