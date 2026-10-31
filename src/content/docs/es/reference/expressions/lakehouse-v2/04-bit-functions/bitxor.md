---
title: BITXOR (Lakehouse v2)
description: BITXOR — devuelve el XOR bit a bit de dos valores numéricos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitxor.md
---

Devuelve el XOR bit a bit de dos valores numéricos.

## Sintaxis de Analyze

```python
func.bitxor(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## Sintaxis de SQL

```sql
BITXOR(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
