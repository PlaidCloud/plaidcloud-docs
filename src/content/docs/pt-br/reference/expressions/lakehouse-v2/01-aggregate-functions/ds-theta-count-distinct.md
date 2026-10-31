---
title: DS_THETA_COUNT_DISTINCT (Lakehouse v2)
description: "Use a função de agregação DS_THETA_COUNT_DISTINCT no PlaidCloud Lakehouse. Retorna uma contagem distinta aproximada usando o algoritmo Theta do DataSketches. Oferece suporte."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-theta-count-distinct.md
---

Retorna uma contagem distinta aproximada usando o algoritmo Theta do DataSketches. Oferece suporte a operações de conjunto, como interseção e diferença.

## Sintaxe no Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Exemplos no Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10035 │
└───────┘
```

## Sintaxe SQL

```sql
DS_THETA_COUNT_DISTINCT(<expr>)
```

## Exemplos de SQL

```sql
SELECT DS_THETA_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10035 │
└───────┘
```
