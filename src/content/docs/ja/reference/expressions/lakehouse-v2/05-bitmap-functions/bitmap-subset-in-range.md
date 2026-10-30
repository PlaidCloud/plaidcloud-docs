---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v2)
description: BITMAP_SUBSET_IN_RANGE — 指定した範囲内にあるビットマップの部分集合を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-in-range.md
---

指定した範囲内にあるビットマップの部分集合を返します。

## Analyzeの構文

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Analyzeの例

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
