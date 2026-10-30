---
title: VAR_SAMP (Lakehouse v2)
description: VAR_SAMP：返回样本方差，是 `VARIANCE_SAMP` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/var-samp.md
---

返回样本方差，是 `VARIANCE_SAMP` 的别名。

## Analyze 语法

```python
func.var_samp(get_column(table, 'score'))
```

## Analyze 示例

```python
func.var_samp(get_column(table, 'score'))

┌────────┐
│ 252.48 │
└────────┘
```

## SQL 语法

```sql
VAR_SAMP(<score>)
```

## SQL 示例

```sql
SELECT VAR_SAMP(score) FROM test_results;

┌────────┐
│ 252.48 │
└────────┘
```
