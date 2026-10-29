---
title: BITAND (Lakehouse v2)
description: BITAND — 2 つの数値のビット単位の AND を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitand.md
---

2 つの数値のビット単位の AND を返します。

## Analyzeの構文

```python
func.bitand(<x>, <y>)
```

## Analyzeの例

```python
func.bitand(12, 10)

┌───┐
│ 8  │
└───┘
```

## SQLの構文

```sql
BITAND(<x>, <y>)
```

## SQLの例

```sql
SELECT BITAND(12, 10);

┌───┐
│ 8  │
└───┘
```
