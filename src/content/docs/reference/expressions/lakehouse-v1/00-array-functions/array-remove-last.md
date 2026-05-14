---
title: ARRAY_REMOVE_LAST
description: "Learn how to use the ARRAY_REMOVE_LAST array function in PlaidCloud Lakehouse. Removes the last element from the array. Includes syntax and examples."
---

Removes the last element from the array.

## Analyze Syntax

```python
func.array_remove_last( <array> )
```

## Analyze Examples

```python
func.array_remove_last([1, 2, 3]) 

┌────────────────────────────────────┐
│ func.array_remove_last([1, 2, 3])  │
├────────────────────────────────────┤
│ [1,2]                              │
└────────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_REMOVE_LAST( <array> )
```

## SQL Examples

```sql
SELECT ARRAY_REMOVE_LAST([1, 2, 3]);

┌──────────────────────────────┐
│ array_remove_last([1, 2, 3]) │
├──────────────────────────────┤
│ [1,2]                        │
└──────────────────────────────┘
```
