---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K — zwraca k najczęstszych wartości wraz z ich przybliżonymi liczebnościami.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

Zwraca k najczęstszych wartości wraz z ich przybliżonymi liczebnościami.

## Składnia w Analyze

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Przykłady w Analyze

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## Składnia SQL

```sql
APPROX_TOP_K(<city>, 3)
```

## Przykłady SQL

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
