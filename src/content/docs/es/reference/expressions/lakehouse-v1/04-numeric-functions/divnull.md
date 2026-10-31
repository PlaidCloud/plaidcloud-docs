---
title: DIVNULL (Lakehouse v1)
description: DIVNULL — devuelve el cociente de dividir el primer número entre el segundo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/divnull.md
---

Devuelve el cociente de dividir el primer número entre el segundo. Devuelve NULL si el segundo número es 0 o NULL.

Consulte también:

- [DIV](../div)
- [DIV0](../div0)

## Sintaxis de Analyze

```python
func.divnull(<numerator>, <denominator>)
```

## Ejemplos de Analyze

```python
func.divnull(20, 6), func.divnull(20, 0), func.divnull(20, null)

┌───────────────────────────────────────────────────────────────────┐
│ func.divnull(20, 6)│ func.divnull(20, 0) │ func.divnull(20, null) │
├────────────────────┼─────────────────────┼────────────────────────┤
│ 3.3333333333333335 │ NULL                │ NULL                   │
└───────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
DIVNULL(<number1>, <number2>)
```

## Ejemplos de SQL

```sql
SELECT
  DIVNULL(20, 6),
  DIVNULL(20, 0),
  DIVNULL(20, NULL);

┌─────────────────────────────────────────────────────────┐
│   divnull(20, 6)   │ divnull(20, 0) │ divnull(20, null) │
├────────────────────┼────────────────┼───────────────────┤
│ 3.3333333333333335 │ NULL           │ NULL              │
└─────────────────────────────────────────────────────────┘
```
