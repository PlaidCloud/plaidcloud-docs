---
title: BITMAP_MIN (Lakehouse v1)
description: BITMAP_MIN — pobiera minimalną wartość z mapy bitowej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-min.md
---

Pobiera minimalną wartość z mapy bitowej.

## Składnia Analyze

```python
func.bitmap_min( <bitmap> )
```

## Przykłady Analyze

```python
func.bitmap_min(func.build_bitmap([1, 4, 5]))

┌───────────────────────────────────────────────┐
│ func.bitmap_min(func.build_bitmap([1, 4, 5])) │
├───────────────────────────────────────────────┤
│                                             1 │
└───────────────────────────────────────────────┘
```

## Składnia SQL

```sql
BITMAP_MIN( <bitmap> )
```

## Przykłady SQL

```sql
SELECT BITMAP_MIN(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────┐
│ bitmap_min(build_bitmap([1, 4, 5])) │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘
```
