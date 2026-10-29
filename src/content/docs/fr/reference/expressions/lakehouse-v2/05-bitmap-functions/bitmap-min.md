---
title: BITMAP_MIN (Lakehouse v2)
description: BITMAP_MIN — renvoie la valeur minimale d'un bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-min.md
---

Renvoie la valeur minimale d'un bitmap.

## Syntaxe Analyze

```python
func.bitmap_min(<bitmap>)
```

## Exemples Analyze

```python
func.bitmap_min(get_column(table, 'bm'))

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
BITMAP_MIN(<bitmap>)
```

## Exemples SQL

```sql
SELECT BITMAP_MIN(BITMAP_FROM_STRING('1,50,100'));

┌───┐
│ 1 │
└───┘
```
