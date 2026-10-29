---
title: BIT_SHIFT_RIGHT (Lakehouse v2)
description: "Use la función de bits BIT_SHIFT_RIGHT en PlaidCloud Lakehouse. Desplaza a la derecha los bits de un valor numérico el número de posiciones especificado (desplazamiento aritmético)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right.md
---

Desplaza a la derecha los bits de un valor numérico el número de posiciones especificado (desplazamiento aritmético).

## Sintaxis de Analyze

```python
func.bit_shift_right(<value>, <shift>)
```

## Ejemplos de Analyze

```python
func.bit_shift_right(16, 2)

┌───┐
│ 4  │
└───┘
```

## Sintaxis de SQL

```sql
BIT_SHIFT_RIGHT(<value>, <shift>)
```

## Ejemplos de SQL

```sql
SELECT BIT_SHIFT_RIGHT(16, 2);

┌───┐
│ 4  │
└───┘
```
