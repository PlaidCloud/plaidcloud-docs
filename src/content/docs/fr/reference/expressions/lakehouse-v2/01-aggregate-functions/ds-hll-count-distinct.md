---
title: DS_HLL_COUNT_DISTINCT (Lakehouse v2)
description: "Utilisez la fonction d'agrégation DS_HLL_COUNT_DISTINCT dans PlaidCloud Lakehouse. Renvoie un nombre distinct approximatif à l'aide de l'algorithme HLL de DataSketches. Plus."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-hll-count-distinct.md
---

Renvoie un nombre distinct approximatif à l'aide de l'algorithme HLL de DataSketches. Plus précise que `APPROX_COUNT_DISTINCT`.

## Syntaxe Analyze

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))
```

## Exemples Analyze

```python
func.ds_hll_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10042 │
└───────┘
```

## Syntaxe SQL

```sql
DS_HLL_COUNT_DISTINCT(<expr>)
```

## Exemples SQL

```sql
SELECT DS_HLL_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10042 │
└───────┘
```
