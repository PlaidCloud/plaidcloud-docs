---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP：将位图拆分为多个给定大小的子位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/subdivide-bitmap.md
---

将位图拆分为多个给定大小的子位图。

## Analyze 语法

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Analyze 示例

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## SQL 语法

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(bm) FROM TABLE(
  SUBDIVIDE_BITMAP(BITMAP_FROM_STRING('1,2,3,4'), 2));

┌──────┐
│ bm   │
├──────┤
│ 1,2  │
│ 3,4  │
└──────┘
```
