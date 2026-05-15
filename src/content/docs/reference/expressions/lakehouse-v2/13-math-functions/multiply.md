---
title: MULTIPLY (Lakehouse v2)
description: MULTIPLY — returns the product of two numbers.
---

Returns the product of two numbers.

## Analyze Syntax

```python
func.multiply(<x>, <y>)
```

## Analyze Examples

```python
func.multiply(6, 7)

┌────┐
│ 42  │
└────┘
```

## SQL Syntax

```sql
MULTIPLY(<x>, <y>)
```

## SQL Examples

```sql
SELECT MULTIPLY(6, 7);

┌────┐
│ 42  │
└────┘
```
