---
title: APPROX_TOP_K (Lakehouse v2)
description: APPROX_TOP_K — renvoie les k valeurs les plus fréquentes et leurs nombres d'occurrences approximatifs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-top-k.md
---

Renvoie les k valeurs les plus fréquentes et leurs nombres d'occurrences approximatifs.

## Syntaxe Analyze

```python
func.approx_top_k(get_column(table, 'city'), 3)
```

## Exemples Analyze

```python
func.approx_top_k(get_column(table, 'city'), 3)

┌──────────────────────────────┐
│ [{"item":"NYC","count":150}] │
└──────────────────────────────┘
```

## Syntaxe SQL

```sql
APPROX_TOP_K(<city>, 3)
```

## Exemples SQL

```sql
SELECT APPROX_TOP_K(city, 3) FROM customers;

┌───────────────────────────────────┐
│ [{"item":"New York","count":150}] │
└───────────────────────────────────┘
```
