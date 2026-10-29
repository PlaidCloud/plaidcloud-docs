---
title: BITMAP_COUNT (Lakehouse v2)
description: BITMAP_COUNT — renvoie le nombre de bits positionnés dans un bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-count.md
---

Renvoie le nombre de bits positionnés dans un bitmap.

## Syntaxe Analyze

```python
func.bitmap_count(<bitmap>)
```

## Exemples Analyze

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## Syntaxe SQL

```sql
BITMAP_COUNT(<bitmap>)
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
