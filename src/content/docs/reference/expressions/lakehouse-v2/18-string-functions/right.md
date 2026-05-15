---
title: RIGHT (Lakehouse v2)
description: RIGHT — returns the rightmost N characters of a string.
---

Returns the rightmost N characters of a string.

## Analyze Syntax

```python
func.right(<str>, <len>)
```

## Analyze Examples

```python
func.right('StarRocks', 5)

┌─────────┐
│ 'Rocks'  │
└─────────┘
```

## SQL Syntax

```sql
RIGHT(<str>, <len>)
```

## SQL Examples

```sql
SELECT RIGHT('StarRocks', 5);

┌───────┐
│ Rocks  │
└───────┘
```
