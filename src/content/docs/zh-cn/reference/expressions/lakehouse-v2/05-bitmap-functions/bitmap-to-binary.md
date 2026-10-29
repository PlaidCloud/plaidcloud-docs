---
title: BITMAP_TO_BINARY (Lakehouse v2)
description: BITMAP_TO_BINARY：将位图转换为二进制值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-binary.md
---

将位图转换为二进制值。

## Analyze 语法

```python
func.bitmap_to_binary(<bitmap>)
```

## Analyze 示例

```python
func.bitmap_to_binary(get_column(table, 'bm'))

┌──────────┐
│ (binary) │
└──────────┘
```

## SQL 语法

```sql
BITMAP_TO_BINARY(<bitmap>)
```

## SQL 示例

```sql
SELECT HEX(BITMAP_TO_BINARY(BITMAP_FROM_STRING('1,2,3')));

┌──────────────┐
│ (hex string) │
└──────────────┘
```
