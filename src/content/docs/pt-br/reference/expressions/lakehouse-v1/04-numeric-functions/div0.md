---
title: DIV0 (Lakehouse v1)
description: DIV0 — retorna o quociente da divisão do primeiro número pelo segundo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/div0.md
---

Retorna o quociente da divisão do primeiro número pelo segundo. Retorna 0 se o segundo número for 0.

Veja também:

- [DIV](../div)
- [DIVNULL](../divnull)

## Sintaxe do Analyze

```python
func.div0(<numerator>, <denominator>)
```

## Exemplos do Analyze

```python
func.div0(20, 6), func.div0(20, 0), func.div0(20, null)

┌─────────────────────────────────────────────────────────────┐
│  func.div0(20, 6)  │ func.div0(20, 0) │ func.div0(20, null) │
├────────────────────┼──────────────────┼─────────────────────┤
│ 3.3333333333333335 │                0 │ NULL                │
└─────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
DIV0(<number1>, <number2>)
```

## Exemplos de SQL

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
