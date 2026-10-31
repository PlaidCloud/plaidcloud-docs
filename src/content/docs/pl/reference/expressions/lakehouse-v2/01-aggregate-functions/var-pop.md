---
title: VAR_POP (Lakehouse v2)
description: VAR_POP — zwraca wariancję populacji. Alias funkcji `VARIANCE_POP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-pop.md
---

Zwraca wariancję populacji. Alias funkcji `VARIANCE_POP`.

## Składnia Analyze

```python
func.var_pop(get_column(table, 'score'))
```

## Przykłady Analyze

```python
func.var_pop(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## Składnia SQL

```sql
VAR_POP(<score>)
```

## Przykłady SQL

```sql
SELECT VAR_POP(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
