---
title: REVERSE
description: "Learn how to use the REVERSE array function in PlaidCloud Lakehouse. Returns an array with elements in reverse order - see syntax, examples, and output."
---

Returns an array with elements in reverse order.

## Analyze Syntax

```python
func.reverse([1, 2, 3])
```

## Analyze Examples

```python
func.reverse([1, 2, 3])

┌─────────┐
│ [3,2,1] │
└─────────┘
```

## SQL Syntax

```sql
REVERSE([1, 2, 3])
```

## SQL Examples

```sql
SELECT ARRAY_REVERSE([1, 2, 3]);

┌─────────┐
│ [3,2,1] │
└─────────┘
```
