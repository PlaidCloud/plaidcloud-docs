---
title: ARRAY_MAP
---

Applies a lambda expression to each element of an array.

## Analyze Syntax

```python
func.array_map(get_column(table, 'arr'), lambda x: x * 2)
```

## Analyze Examples

```python
func.array_map([1, 2, 3], lambda x: x * 2)

┌─────────┐
│ [2,4,6] │
└─────────┘
```

## SQL Syntax

```sql
ARRAY_MAP(<arr>, lambda x: x * 2)
```

## SQL Examples

```sql
SELECT ARRAY_MAP([1, 2, 3], x -> x * 2);

┌─────────┐
│ [2,4,6] │
└─────────┘
```
