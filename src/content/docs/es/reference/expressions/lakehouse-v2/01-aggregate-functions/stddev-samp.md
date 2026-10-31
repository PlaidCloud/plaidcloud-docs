---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP — devuelve la desviación estándar muestral.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-samp.md
---

Devuelve la desviación estándar muestral.

## Sintaxis de Analyze

```python
func.stddev_samp(get_column(table, 'score'))
```

## Ejemplos de Analyze

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## Sintaxis de SQL

```sql
STDDEV_SAMP(<score>)
```

## Ejemplos de SQL

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
