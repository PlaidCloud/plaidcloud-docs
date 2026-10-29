---
title: BITMAP_UNION_COUNT (Lakehouse v2)
description: BITMAP_UNION_COUNT – gibt die Anzahl der eindeutigen Werte in der Vereinigungsmenge einer Menge von Bitmaps zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-count.md
---

Gibt die Anzahl der eindeutigen Werte in der Vereinigungsmenge einer Menge von Bitmaps zurück.

## Analyze-Syntax

```python
func.bitmap_union_count(get_column(table, 'bm'))
```

## Analyze-Beispiele

```python
func.bitmap_union_count(get_column(table, 'user_bitmap'))

┌──────┐
│ 5000 │
└──────┘
```

## SQL-Syntax

```sql
BITMAP_UNION_COUNT(<bm>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_UNION_COUNT(user_bitmap) FROM daily_visits;

┌──────┐
│ 5000 │
└──────┘
```
