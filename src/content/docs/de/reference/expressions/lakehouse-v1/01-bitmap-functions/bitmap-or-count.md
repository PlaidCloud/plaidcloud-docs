---
title: BITMAP_OR_COUNT (Lakehouse v1)
description: BITMAP_OR_COUNT – zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap, indem eine logische OR-Operation ausgeführt wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-or-count.md
---

Zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap, indem eine logische OR-Operation ausgeführt wird.

## Analyze-Syntax

```python
func.bitmap_or_count( <bitmap> )
```

## Analyze-Beispiele

```python
func.bitmap_or_count(func.to_bitmap('1, 3, 5'))

┌─────────────────────────────────────────────────┐
│ func.bitmap_or_count(func.to_bitmap('1, 3, 5')) │
├─────────────────────────────────────────────────┤
│                                               3 │
└─────────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_OR_COUNT( <bitmap> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_OR_COUNT(TO_BITMAP('1, 3, 5'));

┌───────────────────────────────────────┐
│ bitmap_or_count(to_bitmap('1, 3, 5')) │
├───────────────────────────────────────┤
│                                     3 │
└───────────────────────────────────────┘
```
