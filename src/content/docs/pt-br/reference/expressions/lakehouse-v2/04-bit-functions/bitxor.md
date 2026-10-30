---
title: BITXOR (Lakehouse v2)
description: BITXOR — retorna o XOR bit a bit de dois valores numéricos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitxor.md
---

Retorna o XOR bit a bit de dois valores numéricos.

## Sintaxe do Analyze

```python
func.bitxor(<x>, <y>)
```

## Exemplos do Analyze

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## Sintaxe SQL

```sql
BITXOR(<x>, <y>)
```

## Exemplos SQL

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
