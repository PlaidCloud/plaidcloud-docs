---
title: BITMAP_SUBSET_LIMIT (Lakehouse v2)
description: BITMAP_SUBSET_LIMIT：从指定偏移量开始，返回受基数上限约束的位图子集。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-limit.md
---

从指定偏移量开始，返回受基数上限约束的位图子集。

## Analyze 语法

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Analyze 示例

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
