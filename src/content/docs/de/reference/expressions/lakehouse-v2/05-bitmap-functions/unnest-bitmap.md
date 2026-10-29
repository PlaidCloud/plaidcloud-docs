---
title: UNNEST_BITMAP (Lakehouse v2)
description: UNNEST_BITMAP – erweitert eine Bitmap zu einer Menge von Zeilen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/unnest-bitmap.md
---

Erweitert eine Bitmap zu einer Menge von Zeilen.

## Analyze-Syntax

```python
func.unnest_bitmap(<bitmap>)
```

## Analyze-Beispiele

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## SQL-Syntax

```sql
UNNEST_BITMAP(<bitmap>)
```

## SQL-Beispiele

```sql
SELECT * FROM TABLE(UNNEST_BITMAP(BITMAP_FROM_STRING('1,2,3')));

┌───────┐
│ value │
├───────┤
│     1 │
│     2 │
│     3 │
└───────┘
```
