---
title: ARRAY_DISTINCT
---

Removes duplicate elements from an array.

## Analyze Syntax

```python
func.array_distinct([1, 2, 2, 3, 3])
```

## Analyze Examples

```python
func.array_distinct([1, 2, 2, 3, 3])

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## SQL Syntax

```sql
ARRAY_DISTINCT([1, 2, 2, 3, 3])
```

## SQL Examples

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 3, 3]);

┌─────────┐
│ [1,2,3] │
└─────────┘
```
