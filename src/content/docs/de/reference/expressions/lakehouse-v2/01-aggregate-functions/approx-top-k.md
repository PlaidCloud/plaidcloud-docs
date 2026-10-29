---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K – gibt die k häufigsten Werte mit ihren ungefähren Häufigkeiten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

Gibt die k häufigsten Werte mit ihren ungefähren Häufigkeiten zurück.

## Analyze-Syntax

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Analyze-Beispiele

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## SQL-Syntax

```sql
APPROX_TOP_K(<city>, 3)
```

## SQL-Beispiele

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
