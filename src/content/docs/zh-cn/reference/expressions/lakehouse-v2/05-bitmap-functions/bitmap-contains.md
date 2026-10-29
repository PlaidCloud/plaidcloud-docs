---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS：检查位图是否包含指定值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-contains.md
---

检查位图是否包含指定值。

## Analyze 语法

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Analyze 示例

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## SQL 语法

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## SQL 示例

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
