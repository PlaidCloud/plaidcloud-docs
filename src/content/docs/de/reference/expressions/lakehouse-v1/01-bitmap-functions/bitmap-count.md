---
title: BITMAP_COUNT (Lakehouse v1)
description: BITMAP_COUNT – zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-count.md
---

Zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap.

## Analyze-Syntax

```python
func.bitmap_count( <bitmap> )
```

## Analyze-Beispiele

```python
func.bitmap_count(build_bitmap([1, 4, 5]))

┌────────────────────────────────────────────┐
│ func.bitmap_count(build_bitmap([1, 4, 5])) │
├────────────────────────────────────────────┤
│                                          3 │
└────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_COUNT( <bitmap> )
```

## Aliasse

- [BITMAP_CARDINALITY](../bitmap-cardinality)

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BUILD_BITMAP([1,4,5])), BITMAP_CARDINALITY(BUILD_BITMAP([1,4,5]));

┌─────────────────────────────────────────────────────────────────────────────────────┐
│ bitmap_count(build_bitmap([1, 4, 5])) │ bitmap_cardinality(build_bitmap([1, 4, 5])) │
├───────────────────────────────────────┼─────────────────────────────────────────────┤
│                                     3 │                                           3 │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
