---
title: BITMAP_AND_COUNT (Lakehouse v1)
description: BITMAP_AND_COUNT – zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap, indem eine logische AND-Operation ausgeführt wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-and-count.md
---

Zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap, indem eine logische AND-Operation ausgeführt wird.

## Analyze-Syntax

```python
func.bitmap_and_count( <bitmap> )
```

## Analyze-Beispiele

```python
func.bitmap_and_count(to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────┐
│ func.bitmap_and_count(to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────┤
│                                           3 │
└─────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_AND_COUNT( <bitmap> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_AND_COUNT(TO_BITMAP('1, 3, 5'));

┌────────────────────────────────────────┐
│ bitmap_and_count(to_bitmap('1, 3, 5')) │
├────────────────────────────────────────┤
│                                      3 │
└────────────────────────────────────────┘
```
