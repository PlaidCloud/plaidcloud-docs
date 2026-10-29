---
title: BITMAP_XOR (Lakehouse v1)
description: "BITMAP_XOR : effectue une opération XOR (OU exclusif) bit à bit sur les deux bitmaps."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-xor.md
---

Effectue une opération XOR (OU exclusif) bit à bit sur les deux bitmaps.

## Syntaxe Analyze

```python
func.bitmap_xor( <bitmap1>, <bitmap2> )
```

## Exemples Analyze

```python
func.bitmap_xor(func.build_bitmap([1, 4, 5]), func.build_bitmap([5, 6, 7]))

┌─────────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_xor(func.build_bitmap([1, 4, 5]), func.build_bitmap([5, 6, 7])) │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1,4,6,7                                                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_XOR( <bitmap1>, <bitmap2> )
```

## Exemples SQL

```sql
SELECT BITMAP_XOR(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([5,6,7]))::String;

┌──────────────────────────────────────────────────────────────────────┐
│ bitmap_xor(build_bitmap([1, 4, 5]), build_bitmap([5, 6, 7]))::string │
├──────────────────────────────────────────────────────────────────────┤
│ 1,4,6,7                                                              │
└──────────────────────────────────────────────────────────────────────┘
```
