---
title: BITMAP_MAX (Lakehouse v1)
description: BITMAP_MAX：获取位图中的最大值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-max.md
---

获取位图中的最大值。

## Analyze 语法

```python
func.bitmap_max( <bitmap> )
```

## Analyze 示例

```python
func.bitmap_max(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_max(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             5 │
└───────────────────────────────────────────────┘
```

## SQL 语法

```sql
BITMAP_MAX( <bitmap> )
```

## SQL 示例

```sql
SELECT BITMAP_MAX(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_max(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   5 │
└─────────────────────────────────────┘
```
