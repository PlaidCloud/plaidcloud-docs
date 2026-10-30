---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v2)
description: BITMAP_SUBSET_IN_RANGE — devuelve un subconjunto de un mapa de bits dentro de un rango especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-in-range.md
---

Devuelve un subconjunto de un mapa de bits dentro de un rango especificado.

## Sintaxis de Analyze

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Ejemplos de Analyze

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
