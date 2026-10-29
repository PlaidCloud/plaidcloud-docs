---
title: BITMAP_SUBSET_LIMIT (Lakehouse v2)
description: BITMAP_SUBSET_LIMIT — retorna um subconjunto de um bitmap a partir de um deslocamento, com um limite de cardinalidade.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/bitmap-subset-limit.md
---

Retorna um subconjunto de um bitmap a partir de um deslocamento, com um limite de cardinalidade.

## Sintaxe do Analyze

```python
func.bitmap_subset_limit(<bitmap>, <offset>, <limit>)
```

## Exemplos do Analyze

```python
func.bitmap_subset_limit(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP_SUBSET_LIMIT(<bitmap>, <offset>, <limit>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(BITMAP_SUBSET_LIMIT(
  BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
