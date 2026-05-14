---
title: ARRAY_FLATTEN
description: "Learn how to use the ARRAY_FLATTEN array function in PlaidCloud Lakehouse. Flattens nested arrays into a single-level array - with syntax and examples."
---

Flattens nested arrays into a single-level array.

## Analyze Syntax

```python
func.array_flatten([[1,2],[3,4]])
```

## Analyze Examples

```python
func.array_flatten([[1, 2], [3, 4]])

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```

## SQL Syntax

```sql
ARRAY_FLATTEN([[1,2],[3,4]])
```

## SQL Examples

```sql
SELECT ARRAY_FLATTEN([[1, 2], [3, 4]]);

┌───────────┐
│ [1,2,3,4] │
└───────────┘
```
