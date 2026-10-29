---
title: VARIANCE (Lakehouse v2)
description: VARIANCE — 母分散を返します。`VARIANCE_POP` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance.md
---

母分散を返します。`VARIANCE_POP` の別名です。

## Analyzeの構文

```python
func.variance(get_column(table, 'score'))
```

## Analyzeの例

```python
func.variance(get_column(table, 'score'))

┌────────┐
│ 234.72 │
└────────┘
```

## SQLの構文

```sql
VARIANCE(<score>)
```

## SQLの例

```sql
SELECT VARIANCE(score) FROM test_results;

┌────────┐
│ 234.72 │
└────────┘
```
