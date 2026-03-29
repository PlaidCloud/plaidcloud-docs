---
title: ARRAY_CONCAT
---

Concatenates multiple arrays into a single array.

## Analyze Syntax

```python
func.array_concat([1, 2], [3, 4])
```

## Analyze Examples

```python
func.array_concat([1, 2], [3, 4])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL Syntax

```sql
ARRAY_CONCAT([1, 2], [3, 4])
```

## SQL Examples

```sql
SELECT ARRAY_CONCAT([1, 2], [3, 4]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
