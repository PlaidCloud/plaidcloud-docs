---
title: BITMAP_MAX (Lakehouse v2)
description: BITMAP_MAX：返回位图中的最大值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-max.md
---

返回位图中的最大值。

## Analyze 语法

```python
func.bitmap_max(<bitmap>)
```

## Analyze 示例

```python
func.bitmap_max(get_column(table, 'bm'))

┌─────┐
│ 100 │
└─────┘
```

## SQL 语法

```sql
BITMAP_MAX(<bitmap>)
```

## SQL 示例

```sql
SELECT BITMAP_MAX(BITMAP_FROM_STRING('1,50,100'));

┌─────┐
│ 100 │
└─────┘
```
