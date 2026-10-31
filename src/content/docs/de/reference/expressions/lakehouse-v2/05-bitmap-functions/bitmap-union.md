---
title: BITMAP_UNION (Lakehouse v2)
description: BITMAP_UNION – gibt die Vereinigungsmenge einer Menge von Bitmaps zurück (Aggregat).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union.md
---

Gibt die Vereinigungsmenge einer Menge von Bitmaps zurück (Aggregat).

## Analyze-Syntax

```python
func.bitmap_union(get_column(table, 'bm'))
```

## Analyze-Beispiele

```python
func.bitmap_union(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_UNION(<bm>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_UNION(user_bitmap)) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
