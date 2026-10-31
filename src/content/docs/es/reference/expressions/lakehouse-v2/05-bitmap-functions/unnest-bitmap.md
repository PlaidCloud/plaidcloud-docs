---
title: UNNEST_BITMAP (Lakehouse v2)
description: UNNEST_BITMAP — expande un mapa de bits en un conjunto de filas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/unnest-bitmap.md
---

Expande un mapa de bits en un conjunto de filas.

## Sintaxis de Analyze

```python
func.unnest_bitmap(<bitmap>)
```

## Ejemplos de Analyze

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## Sintaxis de SQL

```sql
UNNEST_BITMAP(<bitmap>)
```

## Ejemplos de SQL

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
