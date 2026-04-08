---
title: BITAND
description: "Learn how to use the BITAND bit function in PlaidCloud Lakehouse. Returns the bitwise AND of two numeric values - see syntax, examples, and output."
---

Returns the bitwise AND of two numeric values.

## Analyze Syntax

```python
func.bitand(<x>, <y>)
```

## Analyze Examples

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## SQL Syntax

```sql
BITAND(<x>, <y>)
```

## SQL Examples

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
