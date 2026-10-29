---
title: SUB_BITMAP (Lakehouse v2)
description: SUB_BITMAP – gibt eine Teil-Bitmap ab einer angegebenen Position mit einer Begrenzung der Kardinalität zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/sub-bitmap.md
---

Gibt eine Teil-Bitmap ab einer angegebenen Position mit einer Begrenzung der Kardinalität zurück.

## Analyze-Syntax

```python
func.sub_bitmap(<bitmap>, <offset>, <limit>)
```

## Analyze-Beispiele

```python
func.sub_bitmap(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## SQL-Syntax

```sql
SUB_BITMAP(<bitmap>, <offset>, <limit>)
```

## SQL-Beispiele

```sql
SELECT BITMAP_TO_STRING(SUB_BITMAP(BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
