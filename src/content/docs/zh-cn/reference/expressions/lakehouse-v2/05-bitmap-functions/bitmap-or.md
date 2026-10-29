---
title: BITMAP_OR (Lakehouse v2)
description: BITMAP_OR：返回两个位图的并集。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-or.md
---

返回两个位图的并集。

## Analyze 语法

```python
func.bitmap_or(<bm1>, <bm2>)
```

## Analyze 示例

```python
func.bitmap_or(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_OR(<bm1>, <bm2>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BITMAP_OR(
  BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3')));

┌───────┐
│ 1,2,3 │
└───────┘
```
