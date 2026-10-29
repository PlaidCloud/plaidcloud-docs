---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG：将整数值聚合为位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-agg.md
---

将整数值聚合为位图。

## Analyze 语法

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyze 示例

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_AGG(<id>)
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
