---
title: BITMAP_XOR (Lakehouse v1)
description: BITMAP_XOR — realiza una operación XOR (OR exclusivo) bit a bit sobre los dos mapas de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-xor.md
---

Realiza una operación XOR (OR exclusivo) bit a bit sobre los dos mapas de bits.

## Sintaxis de Analyze

```python
func.bitmap_xor( <bitmap1>, <bitmap2> )
```

## Ejemplos de Analyze

```python
func.bitmap_xor(func.build_bitmap([1, 4, 5]), func.build_bitmap([5, 6, 7]))

┌─────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_xor(func.build_bitmap([1, 4, 5]), func.build_bitmap([5, 6, 7])) │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1,4,6,7                                                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
BITMAP_XOR( <bitmap1>, <bitmap2> )
```

## Ejemplos de SQL

```sql
SELECT BITMAP_XOR(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────┐
│ bitmap_xor(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────┤
│ 1,4,6,7                                                              │
└──────────────────────────────────────────────────────────────────────┘
```
