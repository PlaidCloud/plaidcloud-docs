---
title: BITMAP_FROM_STRING (Lakehouse v2)
description: BITMAP_FROM_STRING：将以逗号分隔的整数字符串转换为位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-string.md
---

将以逗号分隔的整数字符串转换为位图。

## Analyze 语法

```python
func.bitmap_from_string(<str>)
```

## Analyze 示例

```python
func.bitmap_from_string('1,2,3,4,5')

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_FROM_STRING(<str>)
```

## SQL 示例

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3,4,5'));

┌───┐
│ 5 │
└───┘
```
