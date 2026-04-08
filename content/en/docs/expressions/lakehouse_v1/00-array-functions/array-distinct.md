---
title: ARRAY_DISTINCT
description: "Learn how to use the ARRAY_DISTINCT array function in PlaidCloud Lakehouse. Removes all duplicates and NULLs from the array without preserving the original..."
---

Removes all duplicates and NULLs from the array without preserving the original order.

## Analyze Syntax

```python
func.array_distinct( <array> )
```

## Analyze Examples

```python
func.array_distinct([1, 2, 2, 4, 3])

┌───────────────────────────────────────┐
│ func.array_distinct([1, 2, 2, 4, 3])  │
├───────────────────────────────────────┤
│ [1,2,4,3]                             │
└───────────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_DISTINCT( <array> )
```

## SQL Examples

```sql
SELECT ARRAY_DISTINCT([1, 2, 2, 4, 3]);

┌─────────────────────────────────┐
│ array_distinct([1, 2, 2, 4, 3]) │
├─────────────────────────────────┤
│ [1,2,4,3]                       │
└─────────────────────────────────┘
```