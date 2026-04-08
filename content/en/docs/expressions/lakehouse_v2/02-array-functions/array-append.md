---
title: ARRAY_APPEND
description: "Learn how to use the ARRAY_APPEND array function in PlaidCloud Lakehouse. Appends an element to the end of an array - see syntax, examples, and output."
---

Appends an element to the end of an array.

## Analyze Syntax

```python
func.array_append([1, 2, 3], 4)
```

## Analyze Examples

```python
func.array_append([1, 2, 3], 4)

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL Syntax

```sql
ARRAY_APPEND([1, 2, 3], 4)
```

## SQL Examples

```sql
SELECT ARRAY_APPEND([1, 2, 3], 4);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
