---
title: LOG2 (Lakehouse v2)
description: LOG2 — returns the base-2 logarithm of a number.
---

Returns the base-2 logarithm of a number.

## Analyze Syntax

```python
func.log2(<x>)
```

## Analyze Examples

```python
func.log2(8)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL Syntax

```sql
LOG2(<x>)
```

## SQL Examples

```sql
SELECT LOG2(8);

┌─────┐
│ 3.0  │
└─────┘
```
