---
title: APPROX_COUNT_DISTINCT (Lakehouse v2)
description: APPROX_COUNT_DISTINCT — zwraca przybliżoną liczbę unikatowych wartości przy użyciu algorytmu HyperLogLog.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-count-distinct.md
---

Zwraca przybliżoną liczbę unikatowych wartości przy użyciu algorytmu HyperLogLog.

## Składnia Analyze

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Przykłady Analyze

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## Składnia SQL

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## Przykłady SQL

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
