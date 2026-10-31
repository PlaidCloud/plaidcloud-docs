---
title: BITMAP_REMOVE (Lakehouse v2)
description: BITMAP_REMOVE — remove um valor específico de um bitmap.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-remove.md
---

Remove um valor específico de um bitmap.

## Sintaxe do Analyze

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Exemplos do Analyze

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
