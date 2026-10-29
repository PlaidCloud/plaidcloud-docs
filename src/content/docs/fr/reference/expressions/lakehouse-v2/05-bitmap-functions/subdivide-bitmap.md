---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP — divise un bitmap en plusieurs sous-bitmaps d'une taille donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/subdivide-bitmap.md
---

Divise un bitmap en plusieurs sous-bitmaps d'une taille donnée.

## Syntaxe Analyze

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Exemples Analyze

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## Syntaxe SQL

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## Exemples SQL

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
