---
title: BITMAP_FROM_BINARY (Lakehouse v2)
description: BITMAP_FROM_BINARY – wandelt einen Binärwert in eine Bitmap um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-from-binary.md
---

Wandelt einen Binärwert in eine Bitmap um.

## Analyze-Syntax

```python
func.bitmap_from_binary(<binary>)
```

## Analyze-Beispiele

```python
func.bitmap_from_binary(get_column(table, 'bin_col'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_FROM_BINARY(<binary>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_BINARY(bm_binary)) FROM data;

┌───┐
│ 5 │
└───┘
```
