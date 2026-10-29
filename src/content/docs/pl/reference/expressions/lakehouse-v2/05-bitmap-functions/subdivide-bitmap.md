---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP — dzieli bitmapę na wiele podbitmap o podanym rozmiarze.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/subdivide-bitmap.md
---

Dzieli bitmapę na wiele podbitmap o podanym rozmiarze.

## Składnia Analyze

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Przykłady Analyze

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## Składnia SQL

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(bm) FROM TABLE(
  SUBDIVIDE_BITMAP(BITMAP_FROM_STRING('1,2,3,4'), 2));

┌──────┐
│ bm   │
├──────┤
│ 1,2  │
│ 3,4  │
└──────┘
```
