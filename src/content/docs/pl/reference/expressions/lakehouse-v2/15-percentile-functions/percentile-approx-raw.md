---
title: PERCENTILE_APPROX_RAW (Lakehouse v2)
description: "Użyj funkcji percentyli PERCENTILE_APPROX_RAW w PlaidCloud Lakehouse. Zwraca przybliżoną wartość percentyla z wcześniej obliczonego stanu percentyla."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-approx-raw.md
---

Zwraca przybliżoną wartość percentyla z wcześniej obliczonego stanu percentyla.

## Składnia Analyze

```python
func.percentile_approx_raw(<state>, <percentile>)
```

## Przykłady Analyze

```python
func.percentile_approx_raw(get_column(table, 'pct_state'), 0.95)

┌───────┐
│ 245.3  │
└───────┘
```

## Składnia SQL

```sql
PERCENTILE_APPROX_RAW(<state>, <percentile>)
```

## Przykłady SQL

```sql
SELECT PERCENTILE_APPROX_RAW(pct_state, 0.95) FROM agg_table;

┌───────┐
│ 245.3  │
└───────┘
```
