---
title: DS_HLL_COUNT_DISTINCT (Lakehouse v2)
description: "Utilize a função de agregação DS_HLL_COUNT_DISTINCT no PlaidCloud Lakehouse. Devolve uma contagem distinta aproximada com o algoritmo HLL do DataSketches. Mais exata."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-count-distinct.md
---

Devolve uma contagem distinta aproximada com o algoritmo HLL do DataSketches. Mais exata do que `APPROX_COUNT_DISTINCT`.

## Sintaxe do Analyze

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))
```

## Exemplos do Analyze

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10042 │
└───────┘
```

## Sintaxe SQL

```sql
DS_HLL_COUNT_DISTINCT(<expr>)
```

## Exemplos de SQL

```sql
SELECT DS_HLL_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10042 │
└───────┘
```
