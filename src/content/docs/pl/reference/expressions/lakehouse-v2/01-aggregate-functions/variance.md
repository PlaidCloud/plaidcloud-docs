---
title: VARIANCE (Lakehouse v2)
description: VARIANCE — zwraca wariancję populacji. Alias funkcji `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance.md
---

Zwraca wariancję populacji. Alias funkcji `VARIANCE_POP`.

## Składnia Analyze

```python
func.variance(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Składnia SQL

```sql
VARIANCE(<score>)
```

## Przykłady SQL

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
