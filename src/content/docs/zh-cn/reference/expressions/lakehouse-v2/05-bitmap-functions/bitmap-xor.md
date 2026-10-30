---
title: BITMAP_XOR (Lakehouse v2)
description: BITMAP_XOR：返回两个位图的对称差。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-xor.md
---

返回两个位图的对称差。

## Analyze 语法

```python
func.bitmap_xor(<bm1>, <bm2>)
```

## Analyze 示例

```python
func.bitmap_xor(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_XOR(<bm1>, <bm2>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BITMAP_XOR(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3,4')));

┌─────┐
│ 1,4 │
└─────┘
```
