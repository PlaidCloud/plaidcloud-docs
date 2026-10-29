---
title: CORR (Lakehouse v2)
description: CORR — devolve o coeficiente de correlação de Pearson entre duas expressões.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/corr.md
---

Devolve o coeficiente de correlação de Pearson entre duas expressões.

## Sintaxe do Analyze

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Exemplos do Analyze

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## Sintaxe SQL

```sql
CORR(<revenue>, <ad_spend>)
```

## Exemplos de SQL

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
