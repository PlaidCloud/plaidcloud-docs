---
title: BITMAP_MAX (Lakehouse v2)
description: BITMAP_MAX — renvoie la valeur maximale d'un bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-max.md
---

Renvoie la valeur maximale d'un bitmap.

## Syntaxe Analyze

```python
func.bitmap_max(<bitmap>)
```

## Exemples Analyze

```python
func.bitmap_max(get_column(table, 'bm'))

┌─────┐
│ 100 │
└─────┘
```

## Syntaxe SQL

```sql
BITMAP_MAX(<bitmap>)
```

## Exemples SQL

```sql
SELECT BITMAP_MAX(BITMAP_FROM_STRING('1,50,100'));

┌─────┐
│ 100 │
└─────┘
```
