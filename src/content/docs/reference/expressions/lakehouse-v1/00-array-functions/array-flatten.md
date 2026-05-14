---
title: ARRAY_FLATTEN
description: "Learn how to use the ARRAY_FLATTEN array function in PlaidCloud Lakehouse. Flattens nested arrays, converting them into a single-level array."
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
