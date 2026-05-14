---
title: ARRAY_SLICE
description: "Learn how to use the ARRAY_SLICE array function in PlaidCloud Lakehouse. Returns a slice of an array from a start position with a given length."
---

Returns a slice of an array from a start position with a given length.

## Analyze Syntax

```python
func.array_slice([1,2,3,4,5], 2, 3)
```

## Analyze Examples

```python
func.array_slice([1, 2, 3, 4, 5], 2, 3)

┌─────────┐
│ [2,3,4] │
└─────────┘
```

## SQL Syntax

```sql
ARRAY_SLICE([1,2,3,4,5], 2, 3)
```

## SQL Examples

```sql
SELECT ARRAY_SLICE([1, 2, 3, 4, 5], 2, 3);

┌─────────┐
│ [2,3,4] │
└─────────┘
```
