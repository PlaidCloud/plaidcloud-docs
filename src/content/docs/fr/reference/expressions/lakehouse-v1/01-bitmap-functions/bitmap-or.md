---
title: BITMAP_OR (Lakehouse v1)
description: "BITMAP_OR : effectue une opération OU bit à bit sur les deux bitmaps."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or.md
---

Effectue une opération OU bit à bit sur les deux bitmaps.

## Syntaxe Analyze

```python
func.bitmap_or( <bitmap1>, <bitmap2> )
```

## Exemples Analyze

```python
func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7]))

┌─────────────────────────────────────────────────────────────────────────┐
│ func.bitmap_or(func.build_bitmap([1, 4, 5]), func.build_bitmap([6, 7])) │
├─────────────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                               │
└─────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_OR( <bitmap1>, <bitmap2> )
```

## Exemples SQL

```sql
SELECT BITMAP_OR(BUILD_BITMAP([1,4,5]), BUILD_BITMAP([6,7]))::String;

┌──────────────────────────────────────────────────────────────────┐
│ bitmap_or(build_bitmap([1, 4, 5]), build_bitmap([6, 7]))::string │
├──────────────────────────────────────────────────────────────────┤
│ 1,4,5,6,7                                                        │
└──────────────────────────────────────────────────────────────────┘
```
