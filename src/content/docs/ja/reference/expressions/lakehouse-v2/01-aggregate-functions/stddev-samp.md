---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP — 標本標準偏差を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-samp.md
---

標本標準偏差を返します。

## Analyzeの構文

```python
func.stddev_samp(get_column(table, 'score'))
```

## Analyzeの例

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## SQLの構文

```sql
STDDEV_SAMP(<score>)
```

## SQLの例

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
