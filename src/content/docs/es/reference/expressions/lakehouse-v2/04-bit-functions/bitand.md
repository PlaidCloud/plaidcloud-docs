---
title: BITAND (Lakehouse v2)
description: BITAND — devuelve el AND bit a bit de dos valores numéricos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitand.md
---

Devuelve el AND bit a bit de dos valores numéricos.

## Sintaxis de Analyze

```python
func.bitand(<x>, <y>)
```

## Ejemplos de Analyze

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## Sintaxis de SQL

```sql
BITAND(<x>, <y>)
```

## Ejemplos de SQL

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
