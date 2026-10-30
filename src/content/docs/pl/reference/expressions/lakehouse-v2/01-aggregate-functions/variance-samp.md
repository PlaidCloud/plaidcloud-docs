---
title: VARIANCE_SAMP (Lakehouse v2)
description: VARIANCE_SAMP — zwraca wariancję próby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-samp.md
---

Zwraca wariancję próby.

## Składnia Analyze

```python
func.variance_samp(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## Składnia SQL

```sql
VARIANCE_SAMP(<score>)
```

## Przykłady SQL

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
