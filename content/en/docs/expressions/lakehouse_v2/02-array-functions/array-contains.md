---
title: ARRAY_CONTAINS
description: "Learn how to use the ARRAY_CONTAINS array function in PlaidCloud Lakehouse. Checks whether an array contains a specific element - with syntax and examples."
---

Checks whether an array contains a specific element.

## Analyze Syntax

```python
func.array_contains([1, 2, 3], 2)
```

## Analyze Examples

```python
func.array_contains([1, 2, 3], 2)

┌───┐
│ 1 │
└───┘
```

## SQL Syntax

```sql
ARRAY_CONTAINS([1, 2, 3], 2)
```

## SQL Examples

```sql
SELECT ARRAY_CONTAINS([1, 2, 3], 2);

┌───┐
│ 1 │
└───┘
```
