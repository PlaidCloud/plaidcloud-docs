---
title: SUM_MAP (Lakehouse v2)
description: SUM_MAP — sumuje wartości pogrupowane według kluczy w kolumnach typu mapa.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/sum-map.md
---

Sumuje wartości pogrupowane według kluczy w kolumnach typu mapa.

## Składnia Analyze

```python
func.sum_map(get_column(table, 'key_col'), get_column(table, 'val_col'))
```

## Przykłady Analyze

```python
func.sum_map(get_column(table, 'keys'), get_column(table, 'values'))

┌─────────────────┐
│ {'a':10,'b':20} │
└─────────────────┘
```

## Składnia SQL

```sql
SUM_MAP(<key_col>, <val_col>)
```

## Przykłady SQL

```sql
SELECT SUM_MAP(keys, values) FROM metrics;

┌─────────────────┐
│ {"a":10,"b":20} │
└─────────────────┘
```
