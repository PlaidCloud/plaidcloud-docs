---
title: ARRAY_AVG
---

Returns the average of elements in an array.

## Analyze Syntax

```python
func.array_avg([1, 2, 3, 4])
```

## Analyze Examples

```python
func.array_avg([10, 20, 30])

┌──────┐
│ 20.0 │
└──────┘
```

## SQL Syntax

```sql
ARRAY_AVG([1, 2, 3, 4])
```

## SQL Examples

```sql
SELECT ARRAY_AVG([10, 20, 30]);

┌──────┐
│ 20.0 │
└──────┘
```
