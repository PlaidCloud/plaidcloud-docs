---
title: CARDINALITY
---

Returns the number of elements in an array. Alias for `ARRAY_LENGTH`.

## Analyze Syntax

```python
func.cardinality([1, 2, 3])
```

## Analyze Examples

```python
func.cardinality([10, 20, 30])

┌───┐
│ 3 │
└───┘
```

## SQL Syntax

```sql
CARDINALITY([1, 2, 3])
```

## SQL Examples

```sql
SELECT CARDINALITY([10, 20, 30]);

┌───┐
│ 3 │
└───┘
```
