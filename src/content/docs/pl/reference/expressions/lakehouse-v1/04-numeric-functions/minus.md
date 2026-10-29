---
title: MINUS (Lakehouse v1)
description: MINUS — zmienia znak wartości liczbowej na przeciwny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/minus.md
---

Zmienia znak wartości liczbowej na przeciwny.

## Składnia Analyze

```python
func.minus( <x> )
```

## Przykłady Analyze

```python
func.minus(func.pi())

┌─────────────────────────┐
│  func.minus(func.pi())  │
├─────────────────────────┤
│      -3.141592653589793 │
└─────────────────────────┘
```

## Składnia SQL

```sql
MINUS( <x> )
```

## Aliasy

- [NEG](../neg)
- [NEGATE](../negate)
- [SUBTRACT](../subtract)

## Przykłady SQL

```sql
SELECT MINUS(PI()), NEG(PI()), NEGATE(PI()), SUBTRACT(PI());

┌───────────────────────────────────────────────────────────────────────────────────┐
│     minus(pi())    │      neg(pi())     │    negate(pi())    │   subtract(pi())   │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┤
│ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │
└───────────────────────────────────────────────────────────────────────────────────┘
```
