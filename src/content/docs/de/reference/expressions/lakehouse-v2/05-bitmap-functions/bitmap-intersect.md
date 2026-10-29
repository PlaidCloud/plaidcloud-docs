---
title: BITMAP_INTERSECT (Lakehouse v2)
description: BITMAP_INTERSECT – gibt die Schnittmenge einer Menge von Bitmaps zurück (Aggregat).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-intersect.md
---

Gibt die Schnittmenge einer Menge von Bitmaps zurück (Aggregat).

## Analyze-Syntax

```python
func.bitmap_intersect(get_column(table, 'bm'))
```

## Analyze-Beispiele

```python
func.bitmap_intersect(get_column(table, 'user_bitmap'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_INTERSECT(<bm>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_INTERSECT(user_bitmap)) FROM segments;

┌─────┐
│ 100 │
└─────┘
```
