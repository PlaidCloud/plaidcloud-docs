---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP：将整数数组转换为位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-to-bitmap.md
---

将整数数组转换为位图。

## Analyze 语法

```python
func.array_to_bitmap([1, 2, 3])
```

## Analyze 示例

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
