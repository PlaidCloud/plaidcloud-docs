---
title: ARRAY_REMOVE
description: "Learn how to use the ARRAY_REMOVE array function in PlaidCloud Lakehouse. Removes all occurrences of a specified element from an array."
---

Removes all occurrences of a specified element from an array.

## Analyze Syntax

```python
func.array_remove([1, 2, 3, 2, 1], 2)
```

## Analyze Examples

```python
func.array_remove([1, 2, 3, 2, 1], 2)

┌─────────┐
│ [1,3,1] │
└─────────┘
```

## SQL Syntax

```sql
ARRAY_REMOVE([1, 2, 3, 2, 1], 2)
```

## SQL Examples

```sql
SELECT ARRAY_REMOVE([1, 2, 3, 2, 1], 2);

┌─────────┐
│ [1,3,1] │
└─────────┘
```
