---
title: STDDEV_SAMP (Lakehouse v2)
description: STDDEV_SAMP：返回样本标准差。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev-samp.md
---

返回样本标准差。

## Analyze 语法

```python
func.stddev_samp(get_column(table, 'score'))
```

## Analyze 示例

```python
func.stddev_samp(get_column(table, 'score'))

┌───────┐
│ 15.89 │
└───────┘
```

## SQL 语法

```sql
STDDEV_SAMP(<score>)
```

## SQL 示例

```sql
SELECT STDDEV_SAMP(score) FROM test_results;

┌───────┐
│ 15.89 │
└───────┘
```
