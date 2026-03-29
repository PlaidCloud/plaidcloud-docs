---
title: ARRAYS_OVERLAP
---

Checks whether two arrays have any common elements.

## Analyze Syntax

```python
func.arrays_overlap([1,2,3], [3,4,5])
```

## Analyze Examples

```python
func.arrays_overlap([1, 2, 3], [3, 4, 5])

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
ARRAYS_OVERLAP([1,2,3], [3,4,5])
```

## SQL Examples

```sql
SELECT ARRAYS_OVERLAP([1, 2, 3], [3, 4, 5]);

┌───┐
│ 1 │
└───┘
```
