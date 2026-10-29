---
title: DS_THETA_COUNT_DISTINCT (Lakehouse v2)
description: "Utilize a função de agregação DS_THETA_COUNT_DISTINCT no PlaidCloud Lakehouse. Devolve uma contagem distinta aproximada com o algoritmo Theta do DataSketches. Suporta."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-theta-count-distinct.md
---

Devolve uma contagem distinta aproximada com o algoritmo Theta do DataSketches. Suporta operações de conjuntos, como a interseção e a diferença.

## Sintaxe do Analyze

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Exemplos do Analyze

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
