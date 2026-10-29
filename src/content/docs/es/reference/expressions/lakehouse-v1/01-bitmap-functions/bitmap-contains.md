---
title: BITMAP_CONTAINS (Lakehouse v1)
description: BITMAP_CONTAINS — comprueba si el mapa de bits contiene un valor específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-contains.md
---

Comprueba si el mapa de bits contiene un valor específico.


## Sintaxis de Analyze

```python
func.bitmap_contains( <bitmap>, <value> )
```

## Ejemplos de Analyze

```python
func.bitmap_contains(build_bitmap([1, 4, 5]), 1)

┌───────────────────────────────────────────────────┐
│ func.bitmap_contains(build_bitmap([1, 4, 5]), 1)  │
├───────────────────────────────────────────────────┤
│ true                                              │
└───────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_CONTAINS( <bitmap>, <value> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_CONTAINS(BUILD_BITMAP([1,4,5]), 1);

┌─────────────────────────────────────────────┐
│ bitmap_contains(build_bitmap([1, 4, 5]), 1) │
├─────────────────────────────────────────────┤
│ true                                        │
└─────────────────────────────────────────────┘
```
