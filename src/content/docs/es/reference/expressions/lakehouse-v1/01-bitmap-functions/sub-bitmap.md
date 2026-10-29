---
title: SUB_BITMAP (Lakehouse v1)
description: SUB_BITMAP — genera un submapa de bits del mapa de bits de origen, a partir del índice inicial y con un tamaño especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/sub-bitmap.md
---

Genera un submapa de bits del mapa de bits de origen, a partir del índice inicial y con un tamaño especificado.

## Sintaxis de Analyze

```python
func.sub_bitmap( <bitmap>, <start>, <size> )
```

## Ejemplos de Analyze

```python
func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3)

┌───────────────────────────────────────────────────────────┐
│ func.sub_bitmap(func.build_bitmap([1, 2, 3, 4, 5]), 1, 3) │
├───────────────────────────────────────────────────────────┤
│ 2,3,4                                                     │
└───────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
SUB_BITMAP( <bitmap>, <start>, <size> )
```

## Ejemplos de SQL

```sql
SELECT SUB_BITMAP(BUILD_BITMAP([1, 2, 3, 4, 5]), 1, 3)::String;

┌─────────────────────────────────────────────────────────┐
│ sub_bitmap(build_bitmap([1, 2, 3, 4, 5]), 1, 3)::string │
├─────────────────────────────────────────────────────────┤
│ 2,3,4                                                   │
└─────────────────────────────────────────────────────────┘
```
