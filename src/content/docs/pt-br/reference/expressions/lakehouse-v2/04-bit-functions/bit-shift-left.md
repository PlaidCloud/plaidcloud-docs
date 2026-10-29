---
title: BIT_SHIFT_LEFT (Lakehouse v2)
description: BIT_SHIFT_LEFT — desloca os bits de um valor numérico para a esquerda pelo número de posições especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-left.md
---

Desloca os bits de um valor numérico para a esquerda pelo número de posições especificado.

## Sintaxe do Analyze

```python
func.bit_shift_left(<value>, <shift>)
```

## Exemplos do Analyze

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## Sintaxe SQL

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## Exemplos SQL

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
