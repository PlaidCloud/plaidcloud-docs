---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS — ビットマップに特定の値が含まれているかどうかを確認します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-contains.md
---

ビットマップに特定の値が含まれているかどうかを確認します。

## Analyzeの構文

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Analyzeの例

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## SQLの構文

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## SQLの例

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
