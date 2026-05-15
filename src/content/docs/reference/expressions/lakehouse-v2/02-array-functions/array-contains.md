---
title: ARRAY_CONTAINS (Lakehouse v2)
description: ARRAY_CONTAINS — Checks whether an array contains a specific element.
---

Checks whether an array contains a specific element.

## Analyze Syntax

```python
func.array_contains([1, 2, 3], 2)
```

## Analyze Examples

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## SQL Examples

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
