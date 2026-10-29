---
title: BIT_SHIFT_RIGHT_LOGICAL (Lakehouse v2)
description: "Use la función de bits BIT_SHIFT_RIGHT_LOGICAL en PlaidCloud Lakehouse. Desplaza a la derecha los bits de un valor numérico el número de posiciones especificado."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bit-shift-right-logical.md
---

Desplaza a la derecha los bits de un valor numérico el número de posiciones especificado (desplazamiento lógico).

## Sintaxis de Analyze

```python
func.bit_shift_right_logical(<value>, <shift>)
```

## Ejemplos de Analyze

```python
func.bit_shift_right_logical(16, 2)

┌───┐
│ 4  │
└───┘
```

## Sintaxis de SQL

```sql
BIT_SHIFT_RIGHT_LOGICAL(<value>, <shift>)
```

## Ejemplos de SQL

```sql
SELECT BIT_SHIFT_RIGHT_LOGICAL(16, 2);

┌───┐
│ 4  │
└───┘
```
