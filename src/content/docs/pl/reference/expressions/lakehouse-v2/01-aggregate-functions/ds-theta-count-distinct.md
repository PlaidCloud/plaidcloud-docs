---
title: DS_THETA_COUNT_DISTINCT (Lakehouse v2)
description: "Użyj funkcji agregującej DS_THETA_COUNT_DISTINCT w PlaidCloud Lakehouse. Zwraca przybliżoną liczbę unikatowych wartości przy użyciu algorytmu Theta DataSketches. Obsługuje operacje."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-theta-count-distinct.md
---

Zwraca przybliżoną liczbę unikatowych wartości przy użyciu algorytmu Theta DataSketches. Obsługuje operacje na zbiorach, takie jak część wspólna i różnica.

## Składnia Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Przykłady Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10035 │
└───────┘
```

## Składnia SQL

```sql
DS_THETA_COUNT_DISTINCT(<expr>)
```

## Przykłady SQL

```sql
SELECT DS_THETA_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10035 │
└───────┘
```
