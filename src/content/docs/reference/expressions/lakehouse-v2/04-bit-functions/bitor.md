---
title: BITOR (Lakehouse v2)
description: BITOR — returns the bitwise OR of two numeric values.
---

Returns the bitwise OR of two numeric values.

## Analyze Syntax

```python
func.bitor(<x>, <y>)
```

## Analyze Examples

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## SQL Syntax

```sql
BITOR(<x>, <y>)
```

## SQL Examples

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
