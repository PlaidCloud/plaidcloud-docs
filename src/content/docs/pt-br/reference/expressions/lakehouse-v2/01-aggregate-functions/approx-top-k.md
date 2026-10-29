---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K — retorna os k valores mais frequentes e suas contagens aproximadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

Retorna os k valores mais frequentes e suas contagens aproximadas.

## Sintaxe do Analyze

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Exemplos do Analyze

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
