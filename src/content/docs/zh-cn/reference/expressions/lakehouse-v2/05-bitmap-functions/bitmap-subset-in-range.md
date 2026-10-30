---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v2)
description: BITMAP_SUBSET_IN_RANGE：返回位图在指定范围内的子集。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-in-range.md
---

返回位图在指定范围内的子集。

## Analyze 语法

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Analyze 示例

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
