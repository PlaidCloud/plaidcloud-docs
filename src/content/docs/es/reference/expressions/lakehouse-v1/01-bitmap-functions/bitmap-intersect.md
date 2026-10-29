---
title: BITMAP_INTERSECT (Lakehouse v1)
description: BITMAP_INTERSECT — cuenta el número de bits establecidos en 1 en el mapa de bits mediante una operación lógica INTERSECT.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-intersect.md
---

Cuenta el número de bits establecidos en 1 en el mapa de bits mediante una operación lógica INTERSECT.

## Sintaxis de Analyze

```python
func.bitmap_intersect( <bitmap> )
```

## Ejemplos de Analyze

```python
func.bitmap_intersect(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_intersect(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│ 1,3,5                                            │
└──────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_INTERSECT( <bitmap> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_INTERSECT(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────────┐
│ bitmap_intersect(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────────┤
│ 1,3,5                                          │
└────────────────────────────────────────────────┘
```
