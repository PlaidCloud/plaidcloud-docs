---
title: INTERSECT_COUNT (Lakehouse v2)
description: "Utilize a função de bitmap INTERSECT_COUNT no PlaidCloud Lakehouse. Devolve a contagem de elementos na interseção de vários bitmaps filtrados por dimensão."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/intersect-count.md
---

Devolve a contagem de elementos na interseção de vários bitmaps filtrados por dimensão.

## Sintaxe do Analyze

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Exemplos do Analyze

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## Sintaxe SQL

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## Exemplos SQL

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
