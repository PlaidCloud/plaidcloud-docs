---
title: BITMAP_REMOVE (Lakehouse v2)
description: BITMAP_REMOVE — ビットマップから特定の値を削除します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-remove.md
---

ビットマップから特定の値を削除します。

## Analyzeの構文

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Analyzeの例

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQLの構文

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## SQLの例

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
