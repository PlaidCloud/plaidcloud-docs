---
title: BITMAP_XOR (Lakehouse v2)
description: BITMAP_XOR — 2 つのビットマップの対称差を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-xor.md
---

2 つのビットマップの対称差を返します。

## Analyzeの構文

```python
func.bitmap_xor(<bm1>, <bm2>)
```

## Analyzeの例

```python
func.bitmap_xor(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_XOR(<bm1>, <bm2>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BITMAP_XOR(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3,4')));

┌─────┐
│ 1,4 │
└─────┘
```
