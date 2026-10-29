---
title: BITMAP_SUBSET_LIMIT (Lakehouse v2)
description: BITMAP_SUBSET_LIMIT — オフセットから始まり、要素数の上限を指定したビットマップの部分集合を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-limit.md
---

オフセットから始まり、要素数の上限を指定したビットマップの部分集合を返します。

## Analyzeの構文

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Analyzeの例

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
