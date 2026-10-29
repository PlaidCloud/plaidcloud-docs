---
title: BITMAP_COUNT (Lakehouse v1)
description: BITMAP_COUNT — cuenta el número de bits establecidos en 1 en el mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-count.md
---

Cuenta el número de bits establecidos en 1 en el mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_count( <bitmap> )
```

## Ejemplos de Analyze

```python
func.bitmap_count(build_bitmap([1, 4, 5]))

┌────────────────────────────────────────────┐
│ func.bitmap_count(build_bitmap([1, 4, 5])) │
├────────────────────────────────────────────┤
│                                          3 │
└────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_COUNT( <bitmap> )
```

## Alias

- [BITMAP_CARDINALITY](../bitmap-cardinality)

## Ejemplos de SQL

```sql
SELECT BITMAP_COUNT(BUILD_BITMAP([1,4,5])), BITMAP_CARDINALITY(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────────────────────────────────────────────────────┐
│ bitmap_count(build_bitmap([1, 4, 5])) │ bitmap_cardinality(build_bitmap([1, 4, 5])) │
├───────────────────────────────────────┼─────────────────────────────────────────────┤
│                                     3 │                                           3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
