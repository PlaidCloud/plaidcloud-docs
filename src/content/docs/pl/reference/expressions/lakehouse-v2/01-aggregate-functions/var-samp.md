---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP — zwraca wariancję próby. Alias funkcji `VARIANCE_SAMP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-samp.md
---

Zwraca wariancję próby. Alias funkcji `VARIANCE_SAMP`.

## Składnia Analyze

```python
func.var_samp(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## Składnia SQL

```sql
VAR_SAMP(<score>)
```

## Przykłady SQL

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
