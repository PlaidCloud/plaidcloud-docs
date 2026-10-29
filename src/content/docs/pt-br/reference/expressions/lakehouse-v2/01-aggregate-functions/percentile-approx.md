---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX — retorna um valor de percentil aproximado usando o algoritmo t-digest.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

Retorna um valor de percentil aproximado usando o algoritmo t-digest.

## Sintaxe do Analyze

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Exemplos do Analyze

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## Sintaxe SQL

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## Exemplos SQL

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
