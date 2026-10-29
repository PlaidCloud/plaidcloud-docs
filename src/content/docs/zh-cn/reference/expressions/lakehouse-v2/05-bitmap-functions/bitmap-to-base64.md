---
title: BITMAP_TO_BASE64 (Lakehouse v2)
description: BITMAP_TO_BASE64：将位图转换为 base64 编码的字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-base64.md
---

将位图转换为 base64 编码的字符串。

## Analyze 语法

```python
func.bitmap_to_base64(<bitmap>)
```

## Analyze 示例

```python
func.bitmap_to_base64(get_column(table, 'bm'))

┌──────────┐
│ 'AQI...' │
└──────────┘
```

## SQL 语法

```sql
BITMAP_TO_BASE64(<bitmap>)
```

## SQL 示例

```sql
SELECT BITMAP_TO_BASE64(BITMAP_FROM_STRING('1,2,3'));

┌─────────────────┐
│ (base64 string) │
└─────────────────┘
```
