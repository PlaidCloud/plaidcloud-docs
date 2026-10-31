---
title: BITMAP_UNION_INT (Lakehouse v2)
description: BITMAP_UNION_INT — renvoie le nombre de valeurs entières distinctes (agrégation).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-union-int.md
---

Renvoie le nombre de valeurs entières distinctes (agrégation).

## Syntaxe Analyze

```python
func.bitmap_union_int(get_column(table, 'id'))
```

## Exemples Analyze

```python
func.bitmap_union_int(get_column(table, 'user_id'))

┌─────┐
│ 500 │
└─────┘
```

## Syntaxe SQL

```sql
BITMAP_UNION_INT(<id>)
```

## Exemples SQL

```sql
SELECT BITMAP_UNION_INT(user_id) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
