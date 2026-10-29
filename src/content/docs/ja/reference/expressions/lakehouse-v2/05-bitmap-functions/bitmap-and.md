---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND — 2 つのビットマップの積集合を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-and.md
---

2 つのビットマップの積集合を返します。

## Analyzeの構文

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Analyzeの例

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
