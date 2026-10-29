---
title: PERCENTILE_APPROX (Lakehouse v2)
description: PERCENTILE_APPROX — t-digest アルゴリズムを使用して近似パーセンタイル値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx.md
---

t-digest アルゴリズムを使用して近似パーセンタイル値を返します。

## Analyzeの構文

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)
```

## Analyzeの例

```python
func.percentile_approx(get_column(table, 'response_time'), 0.95)

┌───────┐
│ 245.3 │
└───────┘
```

## SQLの構文

```sql
PERCENTILE_APPROX(<response_time>, 0.95)
```

## SQLの例

```sql
SELECT PERCENTILE_APPROX(response_time, 0.95) FROM requests;

┌───────┐
│ 245.3 │
└───────┘
```
