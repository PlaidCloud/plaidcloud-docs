---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION — returns the position of the first occurrence of an element (1-indexed).
---

Returns the position of the first occurrence of an element (1-indexed).

## Analyze Syntax

```python
func.array_position([10, 20, 30], 20)
```

## Analyze Examples

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## SQL Syntax

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## SQL Examples

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
