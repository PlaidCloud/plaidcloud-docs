---
title: SUB_BITMAP (Lakehouse v2)
description: SUB_BITMAP：从指定位置开始，返回受基数上限约束的子位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/sub-bitmap.md
---

从指定位置开始，返回受基数上限约束的子位图。

## Analyze 语法

```python
func.sub_bitmap(<bitmap>, <offset>, <limit>)
```

## Analyze 示例

```python
func.sub_bitmap(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
SUB_BITMAP(<bitmap>, <offset>, <limit>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(SUB_BITMAP(BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
