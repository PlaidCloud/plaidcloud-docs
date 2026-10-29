---
title: PERCENTILE_DISC_LC (Lakehouse v2)
description: PERCENTILE_DISC_LC：使用针对低基数优化的算法返回百分位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc-lc.md
---

使用针对低基数优化的算法返回百分位数。

## Analyze 语法

```python
func.percentile_disc_lc(0.5)
```

## Analyze 示例

```python
func.percentile_disc_lc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## SQL 语法

```sql
PERCENTILE_DISC_LC(0.5)
```

## SQL 示例

```sql
SELECT PERCENTILE_DISC_LC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
