---
title: "PERCENTILE_CONT (Percentile, Lakehouse v2)"
description: PERCENTILE_CONT — 連続分布に基づいて補間したパーセンタイル値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-cont.md
---

連続分布に基づいて補間したパーセンタイル値を返します。

## Analyzeの構文

```python
func.percentile_cont(<percentile>)
```

## Analyzeの例

```python
func.percentile_cont(0.5)

┌───────┐
│ 72500  │
└───────┘
```

## SQLの構文

```sql
PERCENTILE_CONT(<percentile>)
```

## SQLの例

```sql
SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72500  │
└───────┘
```
