---
title: BITMAP_COUNT (Lakehouse v2)
description: BITMAP_COUNT：返回位图中已置位的位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-count.md
---

返回位图中已置位的位数。

## Analyze 语法

```python
func.bitmap_count(<bitmap>)
```

## Analyze 示例

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## SQL 语法

```sql
BITMAP_COUNT(<bitmap>)
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
