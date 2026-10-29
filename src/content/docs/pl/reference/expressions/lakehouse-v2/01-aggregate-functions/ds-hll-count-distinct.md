---
title: DS_HLL_COUNT_DISTINCT (Lakehouse v2)
description: "Użyj funkcji agregującej DS_HLL_COUNT_DISTINCT w PlaidCloud Lakehouse. Zwraca przybliżoną liczbę unikatowych wartości przy użyciu algorytmu HLL DataSketches. Dokładniejsza."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-count-distinct.md
---

Zwraca przybliżoną liczbę unikatowych wartości przy użyciu algorytmu HLL DataSketches. Dokładniejsza niż `APPROX_COUNT_DISTINCT`.

## Składnia Analyze

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))
```

## Przykłady Analyze

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10042 │
└───────┘
```

## Składnia SQL

```sql
DS_HLL_COUNT_DISTINCT(<expr>)
```

## Przykłady SQL

```sql
SELECT DS_HLL_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10042 │
└───────┘
```
