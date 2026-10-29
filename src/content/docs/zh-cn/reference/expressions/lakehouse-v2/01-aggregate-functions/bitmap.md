---
title: BITMAP (Lakehouse v2)
description: BITMAP：返回一组值的位图并集。通常与 BITMAP_AGG 配合使用。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bitmap.md
---

返回一组值的位图并集。通常与 BITMAP_AGG 配合使用。

## Analyze 语法

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyze 示例

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP(<id>)
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```
