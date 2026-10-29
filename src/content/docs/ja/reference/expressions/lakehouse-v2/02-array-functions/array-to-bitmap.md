---
title: ARRAY_TO_BITMAP (Lakehouse v2)
description: ARRAY_TO_BITMAP — 整数の配列をビットマップに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-to-bitmap.md
---

整数の配列をビットマップに変換します。

## Analyzeの構文

```python
func.array_to_bitmap([1, 2, 3])
```

## Analyzeの例

```python
func.array_to_bitmap([1, 2, 3])

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
ARRAY_TO_BITMAP([1, 2, 3])
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(ARRAY_TO_BITMAP([1, 2, 3]));

┌───────┐
│ 1,2,3 │
└───────┘
```
