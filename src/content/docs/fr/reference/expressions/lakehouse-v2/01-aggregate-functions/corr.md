---
title: CORR (Lakehouse v2)
description: CORR — renvoie le coefficient de corrélation de Pearson entre deux expressions.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/corr.md
---

Renvoie le coefficient de corrélation de Pearson entre deux expressions.

## Syntaxe Analyze

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Exemples Analyze

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## Syntaxe SQL

```sql
CORR(<revenue>, <ad_spend>)
```

## Exemples SQL

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
