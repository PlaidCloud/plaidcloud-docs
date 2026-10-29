---
title: BITMAP_NOT_COUNT (Lakehouse v1)
description: BITMAP_NOT_COUNT – zählt die Anzahl der auf 0 gesetzten Bits in der Bitmap, indem eine logische NOT-Operation ausgeführt wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-not-count.md
---

Zählt die Anzahl der auf 0 gesetzten Bits in der Bitmap, indem eine logische NOT-Operation ausgeführt wird.

## Analyze-Syntax

```python
func.bitmap_not_count( <bitmap> )
```

## Analyze-Beispiele

```python
func.bitmap_not_count(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────────┐
│ func.bitmap_not_count(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────────┤
│                                                3 │
└──────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_NOT_COUNT( <bitmap> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_NOT_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_not_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
