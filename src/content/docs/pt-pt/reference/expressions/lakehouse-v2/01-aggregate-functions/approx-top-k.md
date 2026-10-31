---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K — devolve os k valores mais frequentes e as respetivas contagens aproximadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

Devolve os k valores mais frequentes e as respetivas contagens aproximadas.

## Sintaxe no Analyze

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Exemplos no Analyze

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## Sintaxe SQL

```sql
APPROX_TOP_K(<city>, 3)
```

## Exemplos SQL

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
