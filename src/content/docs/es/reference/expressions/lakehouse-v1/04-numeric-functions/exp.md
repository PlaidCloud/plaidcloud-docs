---
title: EXP (Lakehouse v1)
description: EXP — devuelve el valor de e (la base de los logaritmos naturales) elevado a la potencia x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/exp.md
---

Devuelve el valor de e (la base de los logaritmos naturales) elevado a la potencia `x`.

## Sintaxis de Analyze

```python
func.exp( <x> )
```

## Ejemplos de Analyze

```python
func.exp(2)

┌──────────────────┐
│   func.exp(2)    │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```

## Sintaxis de SQL

```sql
EXP( <x> )
```

## Ejemplos de SQL

```sql
SELECT EXP(2);

┌──────────────────┐
│      exp(2)      │
├──────────────────┤
│ 7.38905609893065 │
└──────────────────┘
```
