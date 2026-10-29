---
title: BIT_SHIFT_LEFT (Lakehouse v2)
description: BIT_SHIFT_LEFT — desplaza a la izquierda los bits de un valor numérico el número de posiciones especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-left.md
---

Desplaza a la izquierda los bits de un valor numérico el número de posiciones especificado.

## Sintaxis de Analyze

```python
func.bit_shift_left(<value>, <shift>)
```

## Ejemplos de Analyze

```python
func.bit_shift_left(1, 4)

┌────┐
│ 16  │
└────┘
```

## Sintaxis de SQL

```sql
BIT_SHIFT_LEFT(<value>, <shift>)
```

## Ejemplos de SQL

```sql
SELECT BIT_SHIFT_LEFT(1, 4);

┌────┐
│ 16  │
└────┘
```
