---
title: BITMAP_TO_STRING (Lakehouse v2)
description: BITMAP_TO_STRING：将位图转换为以逗号分隔的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-string.md
---

将位图转换为以逗号分隔的字符串。

## Analyze 语法

```python
func.bitmap_to_string(<bitmap>)
```

## Analyze 示例

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## SQL 语法

```sql
BITMAP_TO_STRING(<bitmap>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
