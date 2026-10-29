---
title: COVAR_SAMP (Lakehouse v2)
description: COVAR_SAMP devuelve la covarianza muestral de dos expresiones.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/covar-samp.md
---

Devuelve la covarianza muestral de dos expresiones.

## Sintaxis de Analyze

```python
func.covar_samp(get_column(table, 'y'), get_column(table, 'x'))
```

## Ejemplos de Analyze

```python
func.covar_samp(get_column(table, 'height'), get_column(table, 'weight'))

┌────────┐
│ 103.01 │
└────────┘
```

## Sintaxis de SQL

```sql
COVAR_SAMP(<y>, <x>)
```

## Ejemplos de SQL

```sql
SELECT COVAR_SAMP(height, weight) FROM measurements;

┌────────┐
│ 103.01 │
└────────┘
```
