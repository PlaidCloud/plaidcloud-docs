---
title: BITMAP_SUBSET_LIMIT (Lakehouse v2)
description: BITMAP_SUBSET_LIMIT — devuelve un subconjunto de un mapa de bits a partir de un desplazamiento y con un límite de cardinalidad.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-limit.md
---

Devuelve un subconjunto de un mapa de bits a partir de un desplazamiento y con un límite de cardinalidad.

## Sintaxis de Analyze

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Ejemplos de Analyze

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
