---
title: BASE64_TO_BITMAP (Lakehouse v2)
description: BASE64_TO_BITMAP — Base64 エンコードされた文字列をビットマップに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/base64-to-bitmap.md
---

Base64 エンコードされた文字列をビットマップに変換します。

## Analyzeの構文

```python
func.base64_to_bitmap(<str>)
```

## Analyzeの例

```python
func.base64_to_bitmap(get_column(table, 'b64_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BASE64_TO_BITMAP(<str>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BASE64_TO_BITMAP(b64_col)) FROM data;

┌───────┐
│ 1,2,3 │
└───────┘
```
