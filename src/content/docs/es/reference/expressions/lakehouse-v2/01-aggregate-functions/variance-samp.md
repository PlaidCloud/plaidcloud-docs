---
title: VARIANCE_SAMP (Lakehouse v2)
description: VARIANCE_SAMP — devuelve la varianza muestral.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-samp.md
---

Devuelve la varianza muestral.

## Sintaxis de Analyze

```python
func.variance_samp(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## Sintaxis de SQL

```sql
VARIANCE_SAMP(<score>)
```

## Ejemplos de SQL

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
