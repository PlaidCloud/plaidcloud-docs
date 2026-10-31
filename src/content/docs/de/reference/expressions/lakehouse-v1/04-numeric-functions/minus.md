---
title: MINUS (Lakehouse v1)
description: MINUS – kehrt das Vorzeichen eines numerischen Werts um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/minus.md
---

Kehrt das Vorzeichen eines numerischen Werts um.

## Analyze-Syntax

```python
func.minus( <x> )
```

## Analyze-Beispiele

```python
func.minus(func.pi())

┌─────────────────────────┐
│  func.minus(func.pi())  │
├─────────────────────────┤
│      -3.141592653589793 │
└─────────────────────────┘
```

## SQL-Syntax

```sql
MINUS( <x> )
```

## Aliase

- [NEG](../neg)
- [NEGATE](../negate)
- [SUBTRACT](../subtract)

## SQL-Beispiele

```sql
SELECT MINUS(PI()), NEG(PI()), NEGATE(PI()), SUBTRACT(PI());

┌───────────────────────────────────────────────────────────────────────────────────┐
│     minus(pi())    │      neg(pi())     │    negate(pi())    │   subtract(pi())   │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┤
│ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │
└───────────────────────────────────────────────────────────────────────────────────┘
```
