---
title: DIVNULL (Lakehouse v1)
description: DIVNULL — retorna o quociente da divisão do primeiro número pelo segundo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/divnull.md
---

Retorna o quociente da divisão do primeiro número pelo segundo. Retorna NULL se o segundo número for 0 ou NULL.

Veja também:

- [DIV](../div)
- [DIV0](../div0)

## Sintaxe do Analyze

```python
func.divnull(<numerator>, <denominator>)
```

## Exemplos do Analyze

```python
func.divnull(20, 6), func.divnull(20, 0), func.divnull(20, null)

┌───────────────────────────────────────────────────────────────────┐
│ func.divnull(20, 6)│ func.divnull(20, 0) │ func.divnull(20, null) │
├────────────────────┼─────────────────────┼────────────────────────┤
│ 3.3333333333333335 │ NULL                │ NULL                   │
└───────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
DIVNULL(<number1>, <number2>)
```

## Exemplos de SQL

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
