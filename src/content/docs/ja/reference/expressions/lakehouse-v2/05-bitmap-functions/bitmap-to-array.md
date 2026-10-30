---
title: BITMAP_TO_ARRAY (Lakehouse v2)
description: BITMAP_TO_ARRAY — ビットマップを整数の配列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-to-array.md
---

ビットマップを整数の配列に変換します。

## Analyzeの構文

```python
func.bitmap_to_array(<bitmap>)
```

## Analyzeの例

```python
func.bitmap_to_array(get_column(table, 'bm'))

┌─────────┐
│ [1,2,3] │
└─────────┘
```

## SQLの構文

```sql
BITMAP_TO_ARRAY(<bitmap>)
```

## SQLの例

```sql
SELECT BITMAP_TO_ARRAY(BITMAP_FROM_STRING('1,2,3'));

┌─────────┐
│ [1,2,3] │
└─────────┘
```
