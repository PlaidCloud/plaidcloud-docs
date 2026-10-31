---
title: "PERCENTILE_CONT (Aggregate, Lakehouse v2)"
description: PERCENTILE_CONT：基于连续分布返回插值百分位数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-cont.md
---

基于连续分布返回插值百分位数。

## Analyze 语法

```python
func.percentile_cont(0.5)
```

## Analyze 示例

```python
func.percentile_cont(0.5)

┌──────────┐
│ 72500.00 │
└──────────┘
```

## SQL 语法

```sql
PERCENTILE_CONT(0.5)
```

## SQL 示例

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌──────────┐
│ 72500.00 │
└──────────┘
```
