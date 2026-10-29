---
title: "PERCENTILE_CONT (Percentile, Lakehouse v2)"
description: PERCENTILE_CONT — 基于连续分布返回插值计算的百分位值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-cont.md
---

基于连续分布返回插值计算的百分位值。

## Analyze 语法

```python
func.percentile_cont(<percentile>)
```

## Analyze 示例

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## SQL 语法

```sql
PERCENTILE_CONT(<percentile>)
```

## SQL 示例

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
