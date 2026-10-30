---
title: PERCENTILE_APPROX_WEIGHT (Lakehouse v2)
description: PERCENTILE_APPROX_WEIGHT — 重み付きの近似パーセンタイル値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-approx-weight.md
---

重み付きの近似パーセンタイル値を返します。

## Analyzeの構文

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)
```

## Analyzeの例

```python
func.percentile_approx_weight(get_column(table, 'val'), get_column(table, 'weight'), 0.5)

┌──────┐
│ 72.5 │
└──────┘
```

## SQLの構文

```sql
PERCENTILE_APPROX_WEIGHT(<val>, <weight>, 0.5)
```

## SQLの例

```sql
SELECT PERCENTILE_APPROX_WEIGHT(val, weight, 0.5) FROM data;

┌──────┐
│ 72.5 │
└──────┘
```
