---
title: BIT_SHIFT_RIGHT
description: "Use the BIT_SHIFT_RIGHT bit function in PlaidCloud Lakehouse. Shifts the bits of a numeric value to the right by a specified number of positions (arithmetic)."
---

Shifts the bits of a numeric value to the right by a specified number of positions (arithmetic).

## Analyze Syntax

```python
func.bit_shift_right(<value>, <shift>)
```

## Analyze Examples

```python
func.bit_shift_right(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQL Syntax

```sql
BIT_SHIFT_RIGHT(<value>, <shift>)
```

## SQL Examples

```sql
SELECT BIT_SHIFT_RIGHT(16, 2);

┌───┐
│ 4  │
└───┘
```
