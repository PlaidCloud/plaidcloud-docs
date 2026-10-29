---
title: DS_THETA_COUNT_DISTINCT（Lakehouse v2）
description: "PlaidCloud LakehouseでDS_THETA_COUNT_DISTINCT集計関数を使用します。DataSketches Thetaアルゴリズムを使用して、異なる値のおおよその件数を返します。積集合や差集合などの集合演算をサポートします。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/ds-theta-count-distinct.md
---

DataSketches Thetaアルゴリズムを使用して、異なる値のおおよその件数を返します。積集合や差集合などの集合演算をサポートします。

## Analyzeの構文

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))
```

## Analyzeの例

```python
func.ds_theta_count_distinct(get_column(table, 'user_id'))

┌───────┐
│ 10035 │
└───────┘
```

## SQLの構文

```sql
DS_THETA_COUNT_DISTINCT(<expr>)
```

## SQLの例

```sql
SELECT DS_THETA_COUNT_DISTINCT(user_id) FROM page_views;

┌───────┐
│ 10035 │
└───────┘
```
