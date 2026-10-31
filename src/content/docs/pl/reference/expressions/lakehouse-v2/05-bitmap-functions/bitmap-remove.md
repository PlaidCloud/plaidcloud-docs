---
title: BITMAP_REMOVE (Lakehouse v2)
description: BITMAP_REMOVE — usuwa określoną wartość z bitmapy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-remove.md
---

Usuwa określoną wartość z bitmapy.

## Składnia Analyze

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Przykłady Analyze

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Składnia SQL

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## Przykłady SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
