---
title: MINUS (Lakehouse v1)
description: MINUS — inverte o sinal de um valor numérico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/minus.md
---

Inverte o sinal de um valor numérico.

## Sintaxe do Analyze

```python
func.minus( <x> )
```

## Exemplos do Analyze

```python
func.minus(func.pi())

┌─────────────────────────┐
│  func.minus(func.pi())  │
├─────────────────────────┤
│      -3.141592653589793 │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
MINUS( <x> )
```

## Aliases

- [NEG](../neg)
- [NEGATE](../negate)
- [SUBTRACT](../subtract)

## Exemplos SQL

```sql
SELECT MINUS(PI()), NEG(PI()), NEGATE(PI()), SUBTRACT(PI());

┌───────────────────────────────────────────────────────────────────────────────────┐
│     minus(pi())    │      neg(pi())     │    negate(pi())    │   subtract(pi())   │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┤
│ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │
└───────────────────────────────────────────────────────────────────────────────────┘
```
