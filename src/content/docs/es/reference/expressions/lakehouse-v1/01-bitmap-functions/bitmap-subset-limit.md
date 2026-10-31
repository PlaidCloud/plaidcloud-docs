---
title: BITMAP_SUBSET_LIMIT (Lakehouse v1)
description: BITMAP_SUBSET_LIMIT — genera un submapa de bits del mapa de bits de origen, a partir de un intervalo que empieza en el valor inicial, con un límite de tamaño.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-subset-limit.md
---

Genera un submapa de bits del mapa de bits de origen, a partir de un intervalo que empieza en el valor inicial, con un límite de tamaño.

## Sintaxis de Analyze

```python
func.bitmap_subset_limit( <bitmap>, <start>, <limit> )
```

## Ejemplos de Analyze

```python
func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2)

┌──────────────────────────────────────────────────────────────┐
│ func.bitmap_subset_limit(func.build_bitmap([1, 4, 5]), 2, 2) │
├──────────────────────────────────────────────────────────────┤
│ 4,5                                                          │
└──────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_SUBSET_LIMIT( <bitmap>, <start>, <limit> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_SUBSET_LIMIT(BUILD_BITMAP([1,4,5]), 2, 2)::String;

┌────────────────────────────────────────────────────────────┐
│ bitmap_subset_limit(build_bitmap([1, 4, 5]), 2, 2)::string │
├────────────────────────────────────────────────────────────┤
│ 4,5                                                        │
└────────────────────────────────────────────────────────────┘
```
