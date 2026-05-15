---
title: ANY_MATCH
description: ANY_MATCH — returns TRUE if any element in an array matches the given predicate.
---

Returns TRUE if any element in an array matches the given predicate.

## Analyze Syntax

```python
func.any_match(get_column(table, 'arr'), lambda x: x > 5)
```

## Analyze Examples

```python
func.any_match([1, 2, 8], lambda x: x > 5)

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
ANY_MATCH(<arr>, lambda x: x > 5)
```

## SQL Examples

```sql
SELECT ANY_MATCH([1, 2, 8], x -> x > 5);

┌───┐
│ 1 │
└───┘
```
