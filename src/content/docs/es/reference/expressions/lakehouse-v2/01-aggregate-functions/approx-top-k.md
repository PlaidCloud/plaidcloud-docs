---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K — devuelve los k valores más frecuentes y sus recuentos aproximados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

Devuelve los k valores más frecuentes y sus recuentos aproximados.

## Analyze Syntax

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Analyze Examples

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## SQL Syntax

```sql
APPROX_TOP_K(<city>, 3)
```

## SQL Examples

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
