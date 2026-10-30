---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND：返回两个位图的交集。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-and.md
---

返回两个位图的交集。

## Analyze 语法

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Analyze 示例

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
