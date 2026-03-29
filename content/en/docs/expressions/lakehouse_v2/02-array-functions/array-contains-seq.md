---
title: ARRAY_CONTAINS_SEQ
---

Checks whether an array contains all elements of another array in order.

## Analyze Syntax

```python
func.array_contains_seq([1,2,3], [1,2])
```

## Analyze Examples

```python
func.array_contains_seq([1, 2, 3, 4], [2, 3])

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
ARRAY_CONTAINS_SEQ([1,2,3], [1,2])
```

## SQL Examples

```sql
SELECT ARRAY_CONTAINS_SEQ([1, 2, 3, 4], [2, 3]);

┌───┐
│ 1 │
└───┘
```
