---
title: ARRAY_JOIN
description: ARRAY_JOIN — Concatenates array elements into a string with a separator.
---

Concatenates array elements into a string with a separator.

## Analyze Syntax

```python
func.array_join([1,2,3], '-')
```

## Analyze Examples

```python
func.array_join(['a', 'b', 'c'], '-')

┌─────────┐
│ 'a-b-c' │
└─────────┘
```

## SQL Syntax

```sql
ARRAY_JOIN([1,2,3], '-')
```

## SQL Examples

```sql
SELECT ARRAY_JOIN(['a', 'b', 'c'], '-');

┌───────┐
│ a-b-c │
└───────┘
```
