---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN：返回位图中的最小值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-min.md
---

返回位图中的最小值。

## Analyze 语法

```python
func.bitmap_min(<bitmap>)
```

## Analyze 示例

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
BITMAP_MIN(<bitmap>)
```

## SQL 示例

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
