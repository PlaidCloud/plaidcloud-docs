---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP — divide un mapa de bits en varios submapas de bits de un tamaño determinado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/subdivide-bitmap.md
---

Divide un mapa de bits en varios submapas de bits de un tamaño determinado.

## Sintaxis de Analyze

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Ejemplos de Analyze

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## Sintaxis de SQL

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(bm) FROM TABLE(
  SUBDIVIDE_BITMAP(BITMAP_FROM_STRING('1,2,3,4'), 2));

┌──────┐
│ bm   │
├──────┤
│ 1,2  │
│ 3,4  │
└──────┘
```
