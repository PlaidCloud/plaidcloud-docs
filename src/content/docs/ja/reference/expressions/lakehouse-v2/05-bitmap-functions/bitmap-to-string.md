---
title: BITMAP_TO_STRING (Lakehouse v2)
description: BITMAP_TO_STRING — ビットマップをカンマ区切りの文字列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-string.md
---

ビットマップをカンマ区切りの文字列に変換します。

## Analyzeの構文

```python
func.bitmap_to_string(<bitmap>)
```

## Analyzeの例

```python
func.bitmap_to_string(get_column(table, 'bm'))

┌─────────┐
│ '1,2,3' │
└─────────┘
```

## SQLの構文

```sql
BITMAP_TO_STRING(<bitmap>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BITMAP_FROM_STRING('1,2,3'));

┌───────┐
│ 1,2,3 │
└───────┘
```
