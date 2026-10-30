---
title: SUBDIVIDE_BITMAP (Lakehouse v2)
description: SUBDIVIDE_BITMAP — divide um bitmap em vários sub-bitmaps de um tamanho determinado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/subdivide-bitmap.md
---

Divide um bitmap em vários sub-bitmaps de um tamanho determinado.

## Sintaxe do Analyze

```python
func.subdivide_bitmap(<bitmap>, <size>)
```

## Exemplos do Analyze

```python
func.subdivide_bitmap(get_column(table, 'bm'), 2)
```

## Sintaxe SQL

```sql
SUBDIVIDE_BITMAP(<bitmap>, <size>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(bm) FROM TABLE(
  SUBDIVIDE_BITMAP(BITMAP_FROM_STRING('1,2,3,4'), 2));

┌──────┐
│ bm   │
├──────┤
│ 1,2  │
│ 3,4  │
└──────┘
```
