---
title: CORR (Lakehouse v2)
description: CORR devuelve el coeficiente de correlación de Pearson entre dos expresiones.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/corr.md
---

Devuelve el coeficiente de correlación de Pearson entre dos expresiones.

## Sintaxis de Analyze

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Ejemplos de Analyze

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## Sintaxis de SQL

```sql
CORR(<revenue>, <ad_spend>)
```

## Ejemplos de SQL

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
