---
title: DIV0 (Lakehouse v1)
description: DIV0 — devuelve el cociente de dividir el primer número entre el segundo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div0.md
---

Devuelve el cociente de dividir el primer número entre el segundo. Devuelve 0 si el segundo número es 0.

Consulte también:

- [DIV](../div)
- [DIVNULL](../divnull)

## Sintaxis de Analyze

```python
func.div0(<numerator>, <denominator>)
```

## Ejemplos de Analyze

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
DIV0(<number1>, <number2>)
```

## Ejemplos de SQL

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
