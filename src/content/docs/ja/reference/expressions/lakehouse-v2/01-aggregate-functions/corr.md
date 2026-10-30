---
title: CORR（Lakehouse v2）
description: CORR — 2つの式の間のピアソン相関係数を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/corr.md
---

2つの式の間のピアソン相関係数を返します。

## Analyzeの構文

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))
```

## Analyzeの例

```python
func.corr(get_column(table, 'revenue'), get_column(table, 'ad_spend'))

┌───────┐
│ 0.872 │
└───────┘
```

## SQLの構文

```sql
CORR(<revenue>, <ad_spend>)
```

## SQLの例

```sql
SELECT CORR(revenue, ad_spend) FROM marketing;

┌───────┐
│ 0.872 │
└───────┘
```
