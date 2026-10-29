---
title: BITMAP_HAS_ANY (Lakehouse v2)
description: BITMAP_HAS_ANY – prüft, ob zwei Bitmaps gemeinsame Elemente haben.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-has-any.md
---

Prüft, ob zwei Bitmaps gemeinsame Elemente haben.

## Analyze-Syntax

```python
func.bitmap_has_any(<bm1>, <bm2>)
```

## Analyze-Beispiele

```python
func.bitmap_has_any(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌───┐
│ 1 │
└───┘
```

## SQL-Syntax

```sql
BITMAP_HAS_ANY(<bm1>, <bm2>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_HAS_ANY(BITMAP_FROM_STRING('1,2'), BITMAP_FROM_STRING('2,3'));

┌───┐
│ 1 │
└───┘
```
