---
title: BITMAP_CONTAINS (Lakehouse v2)
description: BITMAP_CONTAINS — vérifie si un bitmap contient une valeur donnée.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-contains.md
---

Vérifie si un bitmap contient une valeur donnée.

## Syntaxe Analyze

```python
func.bitmap_contains(<bitmap>, <value>)
```

## Exemples Analyze

```python
func.bitmap_contains(get_column(table, 'bm'), 42)

┌───┐
│ 1 │
└───┘
```

## Syntaxe SQL

```sql
BITMAP_CONTAINS(<bitmap>, <value>)
```

## Exemples SQL

```sql
SELECT BITMAP_CONTAINS(BITMAP_FROM_STRING('1,2,42'), 42);

┌───┐
│ 1 │
└───┘
```
