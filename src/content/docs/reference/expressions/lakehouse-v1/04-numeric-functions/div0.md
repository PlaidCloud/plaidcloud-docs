---
title: DIV0
description: DIV0 — returns the quotient by dividing the first number by the second one. Includes syntax and.
---

Returns the quotient by dividing the first number by the second one. Returns 0 if the second number is 0.

See also:

- [DIV](../div)
- [DIVNULL](../divnull)

## Analyze Syntax

```python
func.div0(<numerator>, <denominator>)
```

## Analyze Examples

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## SQL Syntax

```sql
DIV0(<number1>, <number2>)
```

## SQL Examples

```sql
SELECT
  DIV0(20, 6),
  DIV0(20, 0),
  DIV0(20, NULL);

┌───────────────────────────────────────────────────┐
│     div0(20, 6)    │ div0(20, 0) │ div0(20, null) │
├────────────────────┼─────────────┼────────────────┤
│ 3.3333333333333335 │           0 │ NULL           │
└───────────────────────────────────────────────────┘
```
