---
title: COVAR_POP (Lakehouse v2)
description: COVAR_POP — retorna a covariância populacional de duas expressões.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-pop.md
---

Retorna a covariância populacional de duas expressões.

## Sintaxe no Analyze

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Exemplos no Analyze

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## Sintaxe SQL

```sql
COVAR_POP(<y>, <x>)
```

## Exemplos de SQL

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
