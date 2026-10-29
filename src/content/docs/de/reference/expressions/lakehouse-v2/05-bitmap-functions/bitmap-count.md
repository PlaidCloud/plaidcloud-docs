---
title: BITMAP_COUNT (Lakehouse v2)
description: BITMAP_COUNT – gibt die Anzahl der gesetzten Bits in einer Bitmap zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-count.md
---

Gibt die Anzahl der gesetzten Bits in einer Bitmap zurück.

## Analyze-Syntax

```python
func.bitmap_count(<bitmap>)
```

## Analyze-Beispiele

```python
func.bitmap_count(get_column(table, 'bm'))

┌───┐
│ 3 │
└───┘
```

## SQL-Syntax

```sql
BITMAP_COUNT(<bitmap>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_FROM_STRING('1,2,3'));

┌───┐
│ 3 │
└───┘
```
