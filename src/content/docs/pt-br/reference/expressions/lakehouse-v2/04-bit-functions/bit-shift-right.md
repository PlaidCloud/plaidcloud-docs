---
title: BIT_SHIFT_RIGHT (Lakehouse v2)
description: "Use a função de bits BIT_SHIFT_RIGHT no PlaidCloud Lakehouse. Desloca os bits de um valor numérico para a direita pelo número de posições especificado (aritmético)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right.md
---

Desloca os bits de um valor numérico para a direita pelo número de posições especificado (aritmético).

## Sintaxe do Analyze

```python
func.bit_shift_right(<value>, <shift>)
```

## Exemplos do Analyze

```python
func.bit_shift_right(16, 2)

┌───┐
│ 4  │
└───┘
```

## Sintaxe SQL

```sql
BIT_SHIFT_RIGHT(<value>, <shift>)
```

## Exemplos SQL

```sql
SELECT BIT_SHIFT_RIGHT(16, 2);

┌───┐
│ 4  │
└───┘
```
