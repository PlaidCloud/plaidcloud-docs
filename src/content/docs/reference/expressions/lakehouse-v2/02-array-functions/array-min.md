---
title: ARRAY_MIN
description: "Learn how to use the ARRAY_MIN array function in PlaidCloud Lakehouse. Returns the minimum element in an array - see syntax, examples, and output."
---

Returns the minimum element in an array.

## Analyze Syntax

```python
func.array_min([3, 1, 4, 1, 5])
```

## Analyze Examples

```python
func.array_min([3, 1, 4, 1, 5])

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
ARRAY_MIN([3, 1, 4, 1, 5])
```

## SQL Examples

```sql
SELECT ARRAY_MIN([3, 1, 4, 1, 5]);

┌───┐
│ 1 │
└───┘
```
