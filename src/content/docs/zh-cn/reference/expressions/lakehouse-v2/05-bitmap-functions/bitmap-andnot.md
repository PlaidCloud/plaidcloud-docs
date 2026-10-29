---
title: BITMAP_ANDNOT (Lakehouse v2)
description: BITMAP_ANDNOT：返回两个位图的差集（属于第一个位图但不属于第二个位图的元素）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-andnot.md
---

返回两个位图的差集（属于第一个位图但不属于第二个位图的元素）。

## Analyze 语法

```python
func.bitmap_andnot(<bm1>, <bm2>)
```

## Analyze 示例

```python
func.bitmap_andnot(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_ANDNOT(<bm1>, <bm2>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BITMAP_ANDNOT(
  BITMAP_FROM_STRING('1,2,3'), BITMAP_FROM_STRING('2,3')));

┌───┐
│ 1 │
└───┘
```
