---
title: VARIANCE_SAMP (Lakehouse v2)
description: VARIANCE_SAMP：返回样本方差。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/variance-samp.md
---

返回样本方差。

## Analyze 语法

```python
func.variance_samp(get_column(table, 'score'))
```

## Analyze 示例

```python
func.variance_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQL 语法

```sql
VARIANCE_SAMP(<score>)
```

## SQL 示例

```sql
SELECT VARIANCE_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
