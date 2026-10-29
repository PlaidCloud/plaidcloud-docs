---
title: BITMAP_REMOVE (Lakehouse v2)
description: BITMAP_REMOVE — elimina un valor específico de un mapa de bits.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-remove.md
---

Elimina un valor específico de un mapa de bits.

## Sintaxis de Analyze

```python
func.bitmap_remove(<bitmap>, <value>)
```

## Ejemplos de Analyze

```python
func.bitmap_remove(get_column(table, 'bm'), 2)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxis de SQL

```sql
BITMAP_REMOVE(<bitmap>, <value>)
```

## Ejemplos de SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_REMOVE(BITMAP_FROM_STRING('1,2,3'), 2));

┌─────┐
│ 1,3 │
└─────┘
```
