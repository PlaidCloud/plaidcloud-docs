---
title: BASE64_TO_BITMAP (Lakehouse v2)
description: BASE64_TO_BITMAP：将 base64 编码的字符串转换为位图。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/base64-to-bitmap.md
---

将 base64 编码的字符串转换为位图。

## Analyze 语法

```python
func.base64_to_bitmap(<str>)
```

## Analyze 示例

```python
func.base64_to_bitmap(get_column(table, 'b64_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL 语法

```sql
BASE64_TO_BITMAP(<str>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_STRING(BASE64_TO_BITMAP(b64_col)) FROM data;

┌───────┐
│ 1,2,3 │
└───────┘
```
