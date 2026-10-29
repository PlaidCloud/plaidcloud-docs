---
title: BITMAP_REMOVE (Lakehouse v2)
description: BITMAP_REMOVE：从位图中移除指定值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-remove.md
---

从位图中移除指定值。

## Analyze 语法

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Analyze 示例

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
