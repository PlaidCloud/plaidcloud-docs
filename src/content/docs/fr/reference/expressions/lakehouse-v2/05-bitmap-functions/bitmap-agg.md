---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG — agrège des valeurs entières dans un bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-agg.md
---

Agrège des valeurs entières dans un bitmap.

## Syntaxe Analyze

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Exemples Analyze

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP_AGG(<id>)
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
