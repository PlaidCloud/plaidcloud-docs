---
title: BITMAP_INTERSECT (Lakehouse v1)
description: BITMAP_INTERSECT – zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap, indem eine logische INTERSECT-Operation ausgeführt wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-intersect.md
---

Zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap, indem eine logische INTERSECT-Operation ausgeführt wird.

## Analyze-Syntax

```python
func.bitmap_intersect( <bitmap> )
```

## Analyze-Beispiele

```python
func.bitmap_intersect(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_intersect(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│ 1,3,5                                            │
└──────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_INTERSECT( <bitmap> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_INTERSECT(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────────┐
│ bitmap_intersect(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────────┤
│ 1,3,5                                          │
└────────────────────────────────────────────────┘
```
