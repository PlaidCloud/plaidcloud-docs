---
title: COVAR_POP (Lakehouse v2)
description: COVAR_POP devuelve la covarianza poblacional de dos expresiones.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-pop.md
---

Devuelve la covarianza poblacional de dos expresiones.

## Sintaxis de Analyze

```python
func.covar_pop(get_column(table, 'y'), get_column(table, 'x'))
```

## Ejemplos de Analyze

```python
func.covar_pop(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 102.46 │
└────────┘
```

## Sintaxis de SQL

```sql
COVAR_POP(<y>, <x>)
```

## Ejemplos de SQL

```sql
SELECT COVAR_POP(height, weight) FROM measurements;

┌────────┐
│ 102.46 │
└────────┘
```
