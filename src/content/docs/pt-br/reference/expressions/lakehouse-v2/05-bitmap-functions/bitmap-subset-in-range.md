---
title: BITMAP_SUBSET_IN_RANGE (Lakehouse v2)
description: BITMAP_SUBSET_IN_RANGE — retorna um subconjunto de um bitmap dentro de um intervalo especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-in-range.md
---

Retorna um subconjunto de um bitmap dentro de um intervalo especificado.

## Sintaxe do Analyze

```python
func.bitmap_subset_in_range(<bitmap>, <start>, <end>)
```

## Exemplos do Analyze

```python
func.bitmap_subset_in_range(get_column(table, 'bm'), 2, 5)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_SUBSET_IN_RANGE(<bitmap>, <start>, <end>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_IN_RANGE(
  BITMAP_FROM_STRING('1,2,3,4,5,6'), 2, 5));

┌───────┐
│ 2,3,4 │
└───────┘
```
