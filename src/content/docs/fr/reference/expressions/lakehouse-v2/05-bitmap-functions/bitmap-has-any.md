---
title: BITMAP_HAS_ANY (Lakehouse v2)
description: BITMAP_HAS_ANY — vérifie si deux bitmaps ont des éléments en commun.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-has-any.md
---

Vérifie si deux bitmaps ont des éléments en commun.

## Syntaxe Analyze

```python
func.bitmap_has_any(<bm1>, <bm2>)
```

## Exemples Analyze

```python
func.bitmap_has_any(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
BITMAP_HAS_ANY(<bm1>, <bm2>)
```

## Exemples SQL

```sql
SELECT BITMAP_HAS_ANY(BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3'));

┌───┐
│ 1 │
└───┘
```
