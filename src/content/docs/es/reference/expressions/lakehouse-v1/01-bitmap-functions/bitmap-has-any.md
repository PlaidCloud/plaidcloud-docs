---
title: BITMAP_HAS_ANY (Lakehouse v1)
description: BITMAP_HAS_ANY — comprueba si el primer mapa de bits tiene algún bit que coincida con los bits del segundo mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-has-any.md
---

Comprueba si el primer mapa de bits tiene algún bit que coincida con los bits del segundo mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_has_any( <bitmap1>, <bitmap2> )
```

## Ejemplos de Analyze

```python
func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))

┌───────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_has_any(func.build_bitmap([1, 4, 5]), func.build_bitmap([1, 2]))  │
├───────────────────────────────────────────────────────────────────────────────┤
│ true                                                                          │
└───────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_HAS_ANY( <bitmap1>, <bitmap2> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_HAS_ANY(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([1,2]));

┌───────────────────────────────────────────────────────────────┐
│ bitmap_has_any(build_bitmap([1, 4, 5]), build_bitmap([1, 2])) │
├───────────────────────────────────────────────────────────────┤
│ true                                                          │
└───────────────────────────────────────────────────────────────┘
```
