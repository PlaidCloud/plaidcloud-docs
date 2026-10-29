---
title: BITMAP_HAS_ALL (Lakehouse v1)
description: BITMAP_HAS_ALL — comprueba si el primer mapa de bits contiene todos los bits del segundo mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-all.md
---

Comprueba si el primer mapa de bits contiene todos los bits del segundo mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_has_all( <bitmap1>, <bitmap2> )
```

## Ejemplos de Analyze

```python
func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) 

┌─────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2]))  │
├─────────────────────────────────────────────────────────────────────┤
│ false                                                               │
└─────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_HAS_ALL( <bitmap1>, <bitmap2> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_HAS_ALL(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_all(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ false                                                         │
└───────────────────────────────────────────────────────────────┘
```
