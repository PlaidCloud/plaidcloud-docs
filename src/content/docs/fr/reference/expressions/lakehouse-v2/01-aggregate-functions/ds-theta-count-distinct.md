---
title: DS_THETA_COUNT_DISTINCT (Lakehouse v2)
description: "Utilisez la fonction d'agrégation DS_THETA_COUNT_DISTINCT dans PlaidCloud Lakehouse. Renvoie un nombre distinct approximatif à l'aide de l'algorithme Theta de DataSketches. Prend en charge."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-theta-count-distinct.md
---

Renvoie un nombre distinct approximatif à l'aide de l'algorithme Theta de DataSketches. Prend en charge les opérations ensemblistes comme l'intersection et la différence.

## Syntaxe Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Exemples Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10035 │
└───────┘
```

## Syntaxe SQL

```sql
DS_THETA_COUNT_DISTINCT(<expr>)
```

## Exemples SQL

```sql
SELECT DS_THETA_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10035 │
└───────┘
```
