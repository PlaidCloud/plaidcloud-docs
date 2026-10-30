---
title: MINUS (Lakehouse v1)
description: MINUS — renvoie l'opposé d'une valeur numérique.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/minus.md
---

Renvoie l'opposé d'une valeur numérique.

## Syntaxe Analyze

```python
func.minus( <x> )
```

## Exemples Analyze

```python
func.minus(func.pi())

┌─────────────────────────┐
│  func.minus(func.pi())  │
├─────────────────────────┤
│      -3.141592653589793 │
└─────────────────────────┘
```

## Syntaxe SQL

```sql
MINUS( <x> )
```

## Alias

- [NEG](../neg)
- [NEGATE](../negate)
- [SUBTRACT](../subtract)

## Exemples SQL

```sql
SELECT MINUS(PI()), NEG(PI()), NEGATE(PI()), SUBTRACT(PI());

┌───────────────────────────────────────────────────────────────────────────────────┐
│     minus(pi())    │      neg(pi())     │    negate(pi())    │   subtract(pi())   │
├────────────────────┼────────────────────┼────────────────────┼────────────────────┤
│ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │ -3.141592653589793 │
└───────────────────────────────────────────────────────────────────────────────────┘
```
