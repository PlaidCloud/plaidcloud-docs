---
title: UNNEST_BITMAP (Lakehouse v2)
description: UNNEST_BITMAP — expande um bitmap num conjunto de linhas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/unnest-bitmap.md
---

Expande um bitmap num conjunto de linhas.

## Sintaxe do Analyze

```python
func.unnest_bitmap(<bitmap>)
```

## Exemplos do Analyze

```python
func.unnest_bitmap(get_column(table, 'bm'))
```

## Sintaxe SQL

```sql
UNNEST_BITMAP(<bitmap>)
```

## Exemplos SQL

```sql
SELECT * FROM TABLE(UNNEST_BITMAP(BITMAP_FROM_STRING('1,2,3')));

┌───────┐
│ value │
├───────┤
│     1 │
│     2 │
│     3 │
└───────┘
```
