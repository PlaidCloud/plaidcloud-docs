---
title: COS (Lakehouse v2)
description: COS — returns the cosine of a number in radians.
---

Returns the cosine of a number in radians.

## Analyze Syntax

```python
func.cos(<x>)
```

## Analyze Examples

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL Syntax

```sql
COS(<x>)
```

## SQL Examples

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
