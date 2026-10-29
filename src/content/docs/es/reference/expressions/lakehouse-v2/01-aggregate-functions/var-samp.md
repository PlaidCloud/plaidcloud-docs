---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP — devuelve la varianza muestral. Alias de `VARIANCE_SAMP`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-samp.md
---

Devuelve la varianza muestral. Alias de `VARIANCE_SAMP`.

## Sintaxis de Analyze

```python
func.var_samp(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## Sintaxis de SQL

```sql
VAR_SAMP(<score>)
```

## Ejemplos de SQL

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
