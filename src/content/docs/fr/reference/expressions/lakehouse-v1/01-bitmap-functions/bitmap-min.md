---
title: BITMAP_MIN (Lakehouse v1)
description: "BITMAP_MIN : obtient la valeur minimale du bitmap."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-min.md
---

Obtient la valeur minimale du bitmap.

## Syntaxe Analyze

```python
func.bitmap_min( <bitmap> )
```

## Exemples Analyze

```python
func.bitmap_min(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_min(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             1 │
└───────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
BITMAP_MIN( <bitmap> )
```

## Exemples SQL

```sql
SELECT BITMAP_MIN(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_min(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘
```
