---
title: UNNEST_BITMAP (Lakehouse v2)
description: UNNEST_BITMAP — développe un bitmap en un ensemble de lignes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/unnest-bitmap.md
---

Développe un bitmap en un ensemble de lignes.

## Syntaxe Analyze

```python
func.unnest_bitmap(<bitmap>)
```

## Exemples Analyze

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## Syntaxe SQL

```sql
UNNEST_BITMAP(<bitmap>)
```

## Exemples SQL

```sql
SELECT * FROM TABLE(UNNEST_BITMAP(BITMAP_FROM_STRING('1,2,3')));

┌───────┐
│ value │
├───────┤
│     1 │
│     2 │
│     3 │
└───────┘
```
