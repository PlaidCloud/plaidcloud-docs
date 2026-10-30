---
title: CORR (Lakehouse v2)
description: CORR — zwraca współczynnik korelacji Pearsona między dwoma wyrażeniami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/corr.md
---

Zwraca współczynnik korelacji Pearsona między dwoma wyrażeniami.

## Składnia Analyze

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Przykłady Analyze

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## Składnia SQL

```sql
CORR(<revenue>, <ad_spend>)
```

## Przykłady SQL

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
