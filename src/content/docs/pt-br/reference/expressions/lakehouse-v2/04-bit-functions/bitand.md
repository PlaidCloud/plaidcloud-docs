---
title: BITAND (Lakehouse v2)
description: BITAND — retorna o AND bit a bit de dois valores numéricos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitand.md
---

Retorna o AND bit a bit de dois valores numéricos.

## Sintaxe do Analyze

```python
func.bitand(<x>, <y>)
```

## Exemplos do Analyze

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## Sintaxe SQL

```sql
BITAND(<x>, <y>)
```

## Exemplos SQL

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
