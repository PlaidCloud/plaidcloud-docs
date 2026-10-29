---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX — zwraca przybliżoną wartość percentyla przy użyciu algorytmu t-digest.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

Zwraca przybliżoną wartość percentyla przy użyciu algorytmu t-digest.

## Składnia Analyze

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Przykłady Analyze

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## Składnia SQL

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## Przykłady SQL

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
