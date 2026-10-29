---
title: SUB_BITMAP (Lakehouse v2)
description: SUB_BITMAP — devolve um sub-bitmap a partir de uma posição especificada, com um limite de cardinalidade.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/sub-bitmap.md
---

Devolve um sub-bitmap a partir de uma posição especificada, com um limite de cardinalidade.

## Sintaxe do Analyze

```python
func.sub_bitmap(<bitmap>, <offset>, <limit>)
```

## Exemplos do Analyze

```python
func.sub_bitmap(get_column(table, 'bm'), 0, 3)

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
SUB_BITMAP(<bitmap>, <offset>, <limit>)
```

## Exemplos SQL

```sql
SELECT BITMAP_TO_STRING(SUB_BITMAP(BITMAP_FROM_STRING('1,2,3,4,5'), 0, 3));

┌───────┐
│ 1,2,3 │
└───────┘
```
