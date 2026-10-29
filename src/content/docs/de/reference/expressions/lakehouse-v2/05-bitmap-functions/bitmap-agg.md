---
title: BITMAP_AGG (Lakehouse v2)
description: BITMAP_AGG – aggregiert Ganzzahlwerte zu einer Bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-agg.md
---

Aggregiert Ganzzahlwerte zu einer Bitmap.

## Analyze-Syntax

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Analyze-Beispiele

```python
func.bitmap_agg(get_column(table, 'user_id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
BITMAP_AGG(<id>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(user_id)) FROM visits;

┌─────┐
│ 500 │
└─────┘
```
