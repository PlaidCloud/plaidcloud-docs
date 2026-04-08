---
title: BIT_SHIFT_RIGHT_LOGICAL
description: "Use the BIT_SHIFT_RIGHT_LOGICAL bit function in PlaidCloud Lakehouse. Shifts the bits of a numeric value to the right by a specified number of positions."
---

Shifts the bits of a numeric value to the right by a specified number of positions (logical).

## Analyze Syntax

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Analyze Examples

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## SQL Syntax

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## SQL Examples

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
