---
title: COVAR_SAMP (Lakehouse v2)
description: COVAR_SAMP — retorna a covariância amostral de duas expressões.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-samp.md
---

Retorna a covariância amostral de duas expressões.

## Sintaxe no Analyze

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Exemplos no Analyze

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## Sintaxe SQL

```sql
COVAR_SAMP(<y>, <x>)
```

## Exemplos de SQL

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
