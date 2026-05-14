---
title: BITXOR
description: "Learn how to use the BITXOR bit function in PlaidCloud Lakehouse. Returns the bitwise XOR of two numeric values - see syntax, examples, and output."
---

Returns the bitwise XOR of two numeric values.

## Analyze Syntax

```python
func.bitxor(<x>, <y>)
```

## Analyze Examples

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## SQL Syntax

```sql
BITXOR(<x>, <y>)
```

## SQL Examples

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
