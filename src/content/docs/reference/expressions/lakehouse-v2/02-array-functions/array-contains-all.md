---
title: ARRAY_CONTAINS_ALL
description: "Learn how to use the ARRAY_CONTAINS_ALL array function in PlaidCloud Lakehouse. Checks whether an array contains all elements of another array."
---

Checks whether an array contains all elements of another array.

## Analyze Syntax

```python
func.array_contains_all([1,2,3], [1,2])
```

## Analyze Examples

```python
func.array_contains_all([1, 2, 3], [1, 2])

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
ARRAY_CONTAINS_ALL([1,2,3], [1,2])
```

## SQL Examples

```sql
SELECT ARRAY_CONTAINS_ALL([1, 2, 3], [1, 2]);

┌───┐
│ 1 │
└───┘
```
