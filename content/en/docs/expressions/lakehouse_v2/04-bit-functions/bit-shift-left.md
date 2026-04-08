---
title: BIT_SHIFT_LEFT
description: "Learn how to use the BIT_SHIFT_LEFT bit function in PlaidCloud Lakehouse. Shifts the bits of a numeric value to the left by a specified number of positions."
---

Shifts the bits of a numeric value to the left by a specified number of positions.

## Analyze Syntax

```python
func.bit_shift_left(<value>, <shift>)
```

## Analyze Examples

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## SQL Syntax

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## SQL Examples

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
