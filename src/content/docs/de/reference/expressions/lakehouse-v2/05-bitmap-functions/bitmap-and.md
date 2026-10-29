---
title: BITMAP_AND (Lakehouse v2)
description: BITMAP_AND – gibt die Schnittmenge zweier Bitmaps zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-and.md
---

Gibt die Schnittmenge zweier Bitmaps zurück.

## Analyze-Syntax

```python
func.bitmap_and(<bm1>, <bm2>)
```

## Analyze-Beispiele

```python
func.bitmap_and(get_column(table, 'bm1'), get_column(table, 'bm2'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_AND(<bm1>, <bm2>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(BITMAP_AND(TO_BITMAP(1), TO_BITMAP(1)));

┌───┐
│ 1 │
└───┘
```
