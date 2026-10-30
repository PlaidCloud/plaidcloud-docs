---
title: BITMAP_UNION (Lakehouse v1)
description: BITMAP_UNION — cuenta el número de bits establecidos en 1 en el mapa de bits mediante una operación lógica UNION.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-union.md
---

Cuenta el número de bits establecidos en 1 en el mapa de bits mediante una operación lógica UNION.

## Sintaxis de Analyze

```python
func.bitmap_union( <bitmap> )
```

## Ejemplos de Analyze

```python
func.bitmap_union(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────┐
│ func.bitmap_union(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────┤
│ 1,3,5                                        │
└──────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_UNION( <bitmap> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_UNION(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────┐
│ bitmap_union(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────┤
│ 1,3,5                                      │
└────────────────────────────────────────────┘
```
