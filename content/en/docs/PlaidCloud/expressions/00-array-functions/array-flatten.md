---
title: ARRAY_FLATTEN
---

Flattens nested arrays, converting them into a single-level array.

## Analyze Syntax

```python
func.array_flatten( <array> )
```

## Analyze Examples

```python
func.array_flatten([[1, 2], [3, 4, 5]]) 

┌──────────────────────────────────────────┐
│ func.array_flatten([[1, 2], [3, 4, 5]])  │
├──────────────────────────────────────────┤
│ [1,2,3,4,5]                              │
└──────────────────────────────────────────┘
```

## SQL Syntax

```sql
ARRAY_FLATTEN( <array> )
```

## SQL Examples

```sql
SELECT ARRAY_FLATTEN([[1,2], [3,4,5]]);

┌────────────────────────────────────┐
│ array_flatten([[1, 2], [3, 4, 5]]) │
├────────────────────────────────────┤
│ [1,2,3,4,5]                        │
└────────────────────────────────────┘
```