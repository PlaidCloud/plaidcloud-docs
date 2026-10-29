---
title: BITMAP_ANDNOT (Lakehouse v2)
description: BITMAP_ANDNOT — 2 つのビットマップの差集合（1 つ目にあって 2 つ目にない要素）を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-andnot.md
---

2 つのビットマップの差集合（1 つ目にあって 2 つ目にない要素）を返します。

## Analyzeの構文

```python
func.bitmap_andnot(<bm1>, <bm2>)
```

## Analyzeの例

```python
func.bitmap_andnot(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_ANDNOT(<bm1>, <bm2>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BITMAP_ANDNOT(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3')));

┌───┐
│ 1 │
└───┘
```
