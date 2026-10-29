---
title: TO_BITMAP (Lakehouse v2)
description: TO_BITMAP：将整数值转换为仅包含该值的位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/to-bitmap.md
---

将整数值转换为仅包含该值的位图。

## Analyze 语法

```python
func.to_bitmap(<value>)
```

## Analyze 示例

```python
func.to_bitmap(42)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
TO_BITMAP(<value>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(TO_BITMAP(42));

┌────┐
│ 42 │
└────┘
```
