---
title: ARRAY_FILTER
---

Filters elements in an array using a lambda expression.

## Analyze Syntax

```python
func.array_filter(get_column(table, 'arr'), lambda x: x > 2)
```

## Analyze Examples

```python
func.array_filter([1, 2, 3, 4, 5], lambda x: x > 2)

┌─────────┐
│ [3,4,5] │
└─────────┘
```

## SQL Syntax

```sql
ARRAY_FILTER(<arr>, lambda x: x > 2)
```

## SQL Examples

```sql
SELECT ARRAY_FILTER([1, 2, 3, 4, 5], x -> x > 2);

┌─────────┐
│ [3,4,5] │
└─────────┘
```
