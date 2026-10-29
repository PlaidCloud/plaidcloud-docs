---
title: CORR (Lakehouse v2)
description: CORR gibt den Pearson-Korrelationskoeffizienten zwischen zwei Ausdrücken zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/corr.md
---

Gibt den Pearson-Korrelationskoeffizienten zwischen zwei Ausdrücken zurück.

## Analyze-Syntax

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Analyze-Beispiele

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## SQL-Syntax

```sql
CORR(<revenue>, <ad_spend>)
```

## SQL-Beispiele

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
