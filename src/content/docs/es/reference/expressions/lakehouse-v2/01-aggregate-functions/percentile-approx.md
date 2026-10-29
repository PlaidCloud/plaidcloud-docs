---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX — devuelve un valor de percentil aproximado mediante el algoritmo t-digest.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

Devuelve un valor de percentil aproximado mediante el algoritmo t-digest.

## Sintaxis de Analyze

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Ejemplos de Analyze

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## Sintaxis de SQL

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## Ejemplos de SQL

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
