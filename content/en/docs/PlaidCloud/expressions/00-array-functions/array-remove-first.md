---
title: ARRAY_REMOVE_FIRST
---

Removes the first element from the array.

## Analyze Syntax

```python
func.array_remove_first( <array> )
```

## Analyze Examples

```python
func.array_remove_first([1, 2, 3]) 

┌─────────────────────────────────────┐
│ func.array_remove_first([1, 2, 3])  │
├─────────────────────────────────────┤
│ [2,3]                               │
└─────────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_REMOVE_FIRST( <array> )
```

## SQL Examples

```sql
SELECT ARRAY_REMOVE_FIRST([1, 2, 3]);

┌───────────────────────────────┐
│ array_remove_first([1, 2, 3]) │
├───────────────────────────────┤
│ [2,3]                         │
└───────────────────────────────┘
```