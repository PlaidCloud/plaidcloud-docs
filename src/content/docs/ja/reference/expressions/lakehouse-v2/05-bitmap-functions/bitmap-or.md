---
title: BITMAP_OR (Lakehouse v2)
description: BITMAP_OR — 2 つのビットマップの和集合を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-or.md
---

2 つのビットマップの和集合を返します。

## Analyzeの構文

```python
func.bitmap_or(<bm1>, <bm2>)
```

## Analyzeの例

```python
func.bitmap_or(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_OR(<bm1>, <bm2>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BITMAP_OR(
  BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3')));

┌───────┐
│ 1,2,3 │
└───────┘
```
