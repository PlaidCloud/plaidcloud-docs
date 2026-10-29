---
title: MINUS (Lakehouse v1)
description: MINUS — cambia el signo de un valor numérico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/minus.md
---

Cambia el signo de un valor numérico.

## Sintaxis de Analyze

```python
func.minus( <x> )
```

## Ejemplos de Analyze

```python
func.minus(func.pi())

┌─────────────────────────┐
│  func.minus(func.pi())  │
├─────────────────────────┤
│      -3.141592653589793 │
└─────────────────────────┘
```

## Sintaxis de SQL

```sql
MINUS( <x> )
```

## Alias

- [NEG](../neg)
- [NEGATE](../negate)
- [SUBTRACT](../subtract)

## Ejemplos de SQL

```sql
SELECT MINUS(PI()), NEG(PI()), NEGATE(PI()), SUBTRACT(PI());

┌───────────────────────────────────────────────────────────────────────────────────┐
│     minus(pi())    │      neg(pi())     │    negate(pi())    │   subtract(pi())   │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┤
│ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │
└───────────────────────────────────────────────────────────────────────────────────┘
```
