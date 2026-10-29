---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND — renvoie l'intersection de deux bitmaps.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-and.md
---

Renvoie l'intersection de deux bitmaps.

## Syntaxe Analyze

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Exemples Analyze

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## Exemples SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
