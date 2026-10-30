---
title: BIT_SHIFT_RIGHT_LOGICAL (Lakehouse v2)
description: "Utilize a função de bits BIT_SHIFT_RIGHT_LOGICAL no PlaidCloud Lakehouse. Desloca os bits de um valor numérico para a direita num número especificado de posições."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right-logical.md
---

Desloca os bits de um valor numérico para a direita num número especificado de posições (deslocamento lógico).

## Sintaxe do Analyze

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Exemplos do Analyze

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## Sintaxe SQL

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## Exemplos SQL

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
