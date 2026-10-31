---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX — devolve um valor de percentil aproximado através do algoritmo t-digest.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

Devolve um valor de percentil aproximado através do algoritmo t-digest.

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
