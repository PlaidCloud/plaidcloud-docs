---
title: APPROX_COUNT_DISTINCT（Lakehouse v2）
description: APPROX_COUNT_DISTINCT — HyperLogLogを使用して、異なる値のおおよその件数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/approx-count-distinct.md
---

HyperLogLogを使用して、異なる値のおおよその件数を返します。

## Analyzeの構文

```python
func.approx_count_distinct(get_column(table, 'user_id'))
```

## Analyzeの例

```python
func.approx_count_distinct(get_column(table, 'user_id'))

┌─────┐
│ 985 │
└─────┘
```

## SQLの構文

```sql
APPROX_COUNT_DISTINCT(<user_id>)
```

## SQLの例

```sql
SELECT APPROX_COUNT_DISTINCT(user_id) FROM page_views;

┌─────┐
│ 985 │
└─────┘
```
