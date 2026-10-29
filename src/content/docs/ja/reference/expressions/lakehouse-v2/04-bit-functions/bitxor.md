---
title: BITXOR (Lakehouse v2)
description: BITXOR — 2 つの数値のビット単位の XOR を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitxor.md
---

2 つの数値のビット単位の XOR を返します。

## Analyzeの構文

```python
func.bitxor(<x>, <y>)
```

## Analyzeの例

```python
func.bitxor(12, 10)

┌───┐
│ 6  │
└───┘
```

## SQLの構文

```sql
BITXOR(<x>, <y>)
```

## SQLの例

```sql
SELECT BITXOR(12, 10);

┌───┐
│ 6  │
└───┘
```
