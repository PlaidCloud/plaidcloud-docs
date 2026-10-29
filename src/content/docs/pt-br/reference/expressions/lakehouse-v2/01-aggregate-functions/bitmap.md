---
title: BITMAP (Lakehouse v2)
description: BITMAP — retorna a união em bitmap de um conjunto de valores. Normalmente usada com BITMAP_AGG.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/bitmap.md
---

Retorna a união em bitmap de um conjunto de valores. Normalmente usada com BITMAP_AGG.

## Sintaxe no Analyze

```python
func.bitmap_agg(get_column(table, 'id'))
```

## Exemplos no Analyze

```python
func.bitmap_agg(get_column(table, 'id'))

┌──────────┐
│ (bitmap) │
└──────────┘
```

## Sintaxe SQL

```sql
BITMAP(<id>)
```

## Exemplos de SQL

```sql
SELECT BITMAP_COUNT(BITMAP_AGG(id)) FROM user_tags;

┌─────┐
│ 500 │
└─────┘
```
