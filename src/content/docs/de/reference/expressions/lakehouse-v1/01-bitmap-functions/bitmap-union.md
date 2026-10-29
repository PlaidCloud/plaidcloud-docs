---
title: BITMAP_UNION (Lakehouse v1)
description: BITMAP_UNION – zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap, indem eine logische UNION-Operation ausgeführt wird.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/01-bitmap-functions/bitmap-union.md
---

Zählt die Anzahl der auf 1 gesetzten Bits in der Bitmap, indem eine logische UNION-Operation ausgeführt wird.

## Analyze-Syntax

```python
func.bitmap_union( <bitmap> )
```

## Analyze-Beispiele

```python
func.bitmap_union(func.to_bitmap('1, 3, 5'))

┌──────────────────────────────────────────────┐
│ func.bitmap_union(func.to_bitmap('1, 3, 5')) │
├──────────────────────────────────────────────┤
│ 1,3,5                                        │
└──────────────────────────────────────────────┘
```

## SQL-Syntax

```sql
BITMAP_UNION( <bitmap> )
```

## SQL-Beispiele

```sql
SELECT BITMAP_UNION(TO_BITMAP('1, 3, 5'))::String;

┌────────────────────────────────────────────┐
│ bitmap_union(to_bitmap('1, 3, 5'))::string │
├────────────────────────────────────────────┤
│ 1,3,5                                      │
└────────────────────────────────────────────┘
```
