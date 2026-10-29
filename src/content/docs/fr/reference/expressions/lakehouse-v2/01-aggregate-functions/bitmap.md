---
title: BITMAP (Lakehouse v2)
description: BITMAP — renvoie l'union bitmap d'un ensemble de valeurs. S'utilise généralement avec BITMAP_AGG.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bitmap.md
---

Renvoie l'union bitmap d'un ensemble de valeurs. S'utilise généralement avec BITMAP_AGG.

## Syntaxe Analyze

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Exemples Analyze

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Syntaxe SQL

```sql
BITMAP(<id>)
```

## Exemples SQL

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```
