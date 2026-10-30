---
title: COVAR_SAMP (Lakehouse v2)
description: COVAR_SAMP — zwraca kowariancję próby dwóch wyrażeń.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-samp.md
---

Zwraca kowariancję próby dwóch wyrażeń.

## Składnia Analyze

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Przykłady Analyze

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## Składnia SQL

```sql
COVAR_SAMP(<y>, <x>)
```

## Przykłady SQL

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
